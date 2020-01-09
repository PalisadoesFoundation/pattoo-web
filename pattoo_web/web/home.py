"""Pattoo version routes."""

# PIP libraries
from flask import Blueprint, render_template, abort

# Pattoo imports
from pattoo_web.web.tables import home
from pattoo_web.web.query.agent import agents

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
    _agents = agents()

    # Process the data
    if _agents.valid is True:
        # Render data from database
        table = home.table(_agents)
        return render_template('home.html', main_table=table)

    # No database
    return render_template('no-api.html')
