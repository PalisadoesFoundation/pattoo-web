"""Pattoo version routes."""

# PIP libraries
from flask import Blueprint, render_template, request, jsonify
import requests

# Pattoo imports
from pattoo_web.configuration import Config
from pattoo_web.web.tables import chart
from pattoo_web import uri
from pattoo_web.constants import SECONDS_IN_DAY

# Define the various global variables
PATTOO_WEB_CHART = Blueprint('PATTOO_WEB_CHART', __name__)


@PATTOO_WEB_CHART.route('/chart/<int:idx_datapoint>')
def route_chart(idx_datapoint):
    """Provide data from the Data table.

    Args:
        idx_datapoint: Datapoint index value to chart

    Returns:
        None

    """
    # Get heading for DataPoint
    args = {}
    args['heading'] = request.args.get('heading')
    args['device'] = request.args.get('device')
    secondsago = uri.integerize_arg(request.args.get('secondsago'))

    # Create URL args
    for key, value in args.items():
        if bool(value) is False:
            args[key] = 'Unknown {}'.format(key)

    # Get table to present
    table = chart.Table(
        idx_datapoint, args['heading'], args['device'], secondsago)
    html = table.html()

    return render_template(
        'chart.html',
        main_table=html,
        key=args['heading'],
        device=args['device'])


@PATTOO_WEB_CHART.route('/chart/<int:idx_datapoint>/data')
def route_chart_data(idx_datapoint):
    """Get API data from remote host.

    Args:
        idx_datapoint: Datapoint index value to chart

    Returns:
        None

    """
    # Initialize key variables
    config = Config()
    secondsago = uri.integerize_arg(request.args.get('secondsago'))
    if bool(secondsago) is False:
        secondsago = SECONDS_IN_DAY

    # Create URL for DataPoint data
    url = ('{}/{}?secondsago={}'.format(
        config.web_api_server_url(graphql=False),
        idx_datapoint,
        secondsago))

    # Get data
    response = requests.get(url)
    data = response.json()
    return jsonify(data)
