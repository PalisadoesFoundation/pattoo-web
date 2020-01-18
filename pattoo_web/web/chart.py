"""Pattoo version routes."""

# Standard imports
import sys

# PIP libraries
from flask import Blueprint, render_template, request, jsonify, abort
import requests

# Pattoo imports
from pattoo_shared import log
from pattoo_web.configuration import Config
from pattoo_web.web.tables import chart
from pattoo_web import uri
from pattoo_web.constants import SECONDS_IN_DAY
from pattoo_web.web.query.pair_xlate import translation
from pattoo_web.web.query.datapoint import datapoint
from pattoo_web.translate import datapoint_translations

# Define the various global variables
PATTOO_WEB_CHART = Blueprint('PATTOO_WEB_CHART', __name__)


@PATTOO_WEB_CHART.route('/datapoint/<identifier>')
def route_chart(identifier):
    """Provide data from the Data table.

    Args:
        identifier: GraphQL identifier for the datapoint

    Returns:
        None

    """
    # Get heading for DataPoint
    secondsago = uri.integerize_arg(request.args.get('secondsago'))

    # Get data from API server
    point = datapoint(identifier)

    if point.valid is True:
        # Get translations from API server
        key_pair_translator = translation(point.id_pair_xlate_group())
        point_xlate = datapoint_translations(point, key_pair_translator)

        # Get table to present
        table = chart.Table(point_xlate, secondsago)
        html = table.html()

        # Get footer
        footer = _footer(point_xlate)

        return render_template(
            'chart.html',
            main_table=html,
            key=point_xlate.pattoo_key_translation.text,
            footer=footer,
            target=point.agent_polled_target())

    # Otherwise abort
    abort(404)


@PATTOO_WEB_CHART.route('/<int:idx_datapoint>/data')
def route_chart_data(idx_datapoint):
    """Get API data from remote host.

    Args:
        idx_datapoint: Datapoint index value to chart

    Returns:
        None

    """
    # Initialize key variables
    success = False
    response = False
    data = []
    config = Config()

    # Get URL parameters
    secondsago = uri.integerize_arg(request.args.get('secondsago'))
    if bool(secondsago) is False:
        secondsago = SECONDS_IN_DAY

    # Create URL for DataPoint data
    url = ('{}/{}?secondsago={}'.format(
        config.web_api_server_url(graphql=False),
        idx_datapoint,
        secondsago))

    # Get data
    try:
        result = requests.get(url)
        response = True
    except:
        # Most likely no connectivity or the TCP port is unavailable
        error = sys.exc_info()[:2]
        log_message = (
            'Error contacting URL {}: ({} {})'
            ''.format(url, error[0], error[1]))
        log.log2info(80010, log_message)

    # Define success
    if response is True:
        if result.status_code == 200:
            success = True
        else:
            log_message = ('''\
HTTP {} error for receiving data from server {}\
'''.format(result.status_code, url))
            log.log2warning(80011, log_message)

    # Present the data
    if success is True:
        data = result.json()
    return jsonify(data)


def _footer(point_xlate):
    """Create a footer to use for the chart.

    Args:
        point: DataPoint object

    Returns:
        result: Footer

    """
    # Initialize key variables
    result = ''

    # Process
    for (meta, value) in point_xlate.metadata_translations:
        # Translate key
        text = meta.text
        result = '{}{}: {}<br>'.format(result, text, value)

    # Return
    result = '<p>{}</p>'.format(result)
    return result
