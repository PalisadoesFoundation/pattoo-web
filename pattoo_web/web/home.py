"""Pattoo version routes."""

# PIP libraries
from flask import Blueprint, render_template, abort

# Pattoo imports
from pattoo_web.web.tables import home
from pattoo_web.web.query.datapoint import datapoints

# Define the various global variables
PATTOO_WEB_HOME = Blueprint('PATTOO_WEB_HOME', __name__)


@PATTOO_WEB_HOME.route('/')
def route_data():
    """Provide data from the Data table.

    Args:
        None

    Returns:
        None

    """
    # Get data from API server
    points = datapoints()

    # Process the data
    if points.valid is True:
        # Initialize key variables
        table = home.table(points)
        return render_template('home.html', main_table=table)

    # Otherwise abort
    abort(404)


@PATTOO_WEB_HOME.route('/status')
def index():
    """Provide the status page.

    Args:
        None

    Returns:
        Home Page

    """
    # Return
    return 'The Pattoo Web is Operational.\n'
