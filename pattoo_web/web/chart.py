"""Pattoo version routes."""

# PIP libraries
from flask import Blueprint, render_template, request, jsonify
import requests

# Pattoo imports
from pattoo_shared.constants import PATTOO_WEB_SITE_PREFIX
from pattoo_web.configuration import Config

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
    # Get URL for DataPoint data
    url = ('{}/chart/{}/data'.format(PATTOO_WEB_SITE_PREFIX, idx_datapoint))

    # Get heading for DataPoint
    heading = request.args.get('heading')
    if bool(heading) is False:
        heading = 'Unknown Heading'

    return render_template('chart.html', url=url, heading=heading)


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
