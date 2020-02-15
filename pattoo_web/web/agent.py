"""Pattoo version routes."""

# PIP libraries
from flask import Blueprint, render_template, request

# Pattoo imports
from pattoo_web.web.query.agent import datapoints_agent
from pattoo_web.web.query.agent_xlate import translations as agent_translations
from pattoo_web.web.query.pair_xlate import translation as pair_translation
from pattoo_web import uri
from pattoo_web.constants import PageInfo
from pattoo_web.translate import datapoint_translations
from pattoo_web.web.tables import chart

from pattoo_shared import log

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
    # Initialize key variables
    rows = []
    screen = uri.graphql_filter(request)

    # Get data from API server
    points = datapoints_agent(identifier, screen=screen)
    agent_xlate = agent_translations()

    # Get URLs
    page_info = PageInfo(
        endCursor=points.end_cursor(),
        hasNextPage=points.has_next_page(),
        hasPreviousPage=points.has_previous_page(),
        startCursor=points.start_cursor()
    )
    (_next, _prev) = uri.prev_next(request, page_info)

    if points.valid is True:
        # Get translation for agent_program
        first_point = points.datapoints()[0]
        agent_program = agent_xlate.agent_program(first_point.agent_program())
        agent_polled_target = first_point.agent_polled_target()

        for point in points.datapoints():
            # Get translations from API server
            key_pair_translator = pair_translation(point.id_pair_xlate_group())
            point_xlate = datapoint_translations(point, key_pair_translator)

            # Get table to present
            table = chart.Table(point_xlate)
            rows.append(table.html())

        # Create the body of tables
        table = '\n'.join(rows)

        # Render data from database
        return render_template(
            'agent.html',
            main_table=table,
            next=_next,
            prev=_prev,
            agent_polled_target=agent_polled_target,
            agent_program=agent_program)

    # No database
    return render_template('no-api.html')
