"""Pattoo version routes."""

# PIP libraries
from flask import Blueprint, render_template, request, jsonify
import requests

# Pattoo imports
from pattoo_web.configuration import Config
from pattoo_web.web.tables import chart

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
    for key, value in args.items():
        if bool(value) is False:
            args[key] = 'Unknown {}'.format(key)
    table = chart.table(idx_datapoint, args['heading'])
    return render_template(
        'chart.html',
        main_table=table,
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

    # Create URL for DataPoint data
    url = ('{}/{}'.format(
        config.web_api_server_url(graphql=False),
        idx_datapoint))

    # Get data
    response = requests.get(url)
    data = response.json()
    return jsonify(data)
