"""Pattoo version routes."""

# PIP libraries
from flask import Blueprint, render_template

# Pattoo imports
from pattoo_web.web.tables import agent
from pattoo_web.web.query.agent import datapoints_agent

# Define the various global variables
PATTOO_WEB_AGENT = Blueprint('PATTOO_WEB_AGENT', __name__)


@PATTOO_WEB_AGENT.route('/<identifier>')
def route_agent(identifier):
    """Provide data from the DataPoint table for a specific Agent.

    Args:
        identifier: GraphQL identifier for the agent

    Returns:
        None

    """
    # Get data from API server
    points = datapoints_agent(identifier)

    # Process the data
    if points.valid is True:
        # Render data from database
        table = agent.table(points)
        return render_template('agent.html', main_table=table)

    # No database
    return render_template('no-api.html')
