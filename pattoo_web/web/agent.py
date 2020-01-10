"""Pattoo version routes."""

# PIP libraries
from flask import Blueprint, render_template

# Pattoo imports
from pattoo_web.web.tables import agent
from pattoo_web.web.query.agent import datapoints_agent
from pattoo_web.web.query.agent_xlate import translations

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
    xlate = translations()

    # Process the data
    if points.valid is True:
        # Get translation for agent_program
        first_point = points.datapoints()[0]
        agent_program = xlate.agent_program(first_point.agent_program())
        agent_polled_target = first_point.agent_polled_target()

        # Render data from database
        table = agent.table(points)
        return render_template(
            'agent.html',
            main_table=table,
            agent_polled_target=agent_polled_target,
            agent_program=agent_program)

    # No database
    return render_template('no-api.html')
