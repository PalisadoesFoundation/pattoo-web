#!/usr/bin/env python3
"""Create homepage table."""

# Standard imports
from operator import itemgetter

# PIP libraries
from flask_table import Table, Col

# Pattoo imports
from pattoo_web import uri
from pattoo_web.web.query.agent_xlate import translations


class RawCol(Col):
    """Class to output whatever it is given without escaping."""

    def td_format(self, content):
        """Override td_format."""
        return content


class ItemTable(Table):
    """Table definition."""

    # Add attributes
    classes = ['table table-bordered']
    table_id = 'dataTable'
    html_attrs = {'width': '100%', 'cellspacing': '0'}

    # Column labels
    agent_program = Col('Agent Program')
    agent_polled_target = RawCol('Target')


class Item():
    """Table row definition."""

    def __init__(self, agent_program, agent_polled_target):
        """Define row contents for table.

        Args:
            agent_program: Key-value pair key
            agent_polled_target: Target polled by agent

        Returns:
            None

        """
        self.agent_program = agent_program
        self.agent_polled_target = agent_polled_target


def table(_agents):
    """Process GraphQL data for parsing to tables.

    Args:
        _agents: GraphQL query DataPoints object

    Returns:
        html: FlaskTable Table object

    """
    # Process API data
    html = ItemTable(_flask_table_rows(_agents))
    return html.__html__()


def _flask_table_rows(_agents):
    """Create HTML table from data.

    Args:
        _agents: GraphQL query DataPoints object

    Returns:
        result: List of FlaskTable table row objects

    """
    # Initialize key varialbes
    result = []
    rows = []

    # Get agent_program translations
    translate = translations()

    # Process the DataPoints
    for _agent in _agents.agents():
        _id = _agent.id()
        agent_polled_target = _agent.agent_polled_target()
        agent_program = translate.agent_program(_agent.agent_program())
        rows.append(
            dict(
                _id=_id,
                agent_polled_target=agent_polled_target,
                agent_program=agent_program))

    # Sort by agent_program then target
    for row in sorted(
            rows, key=itemgetter('agent_program', 'agent_polled_target')):
        # Create link to charts
        link = uri.agent_link(
            row.get('_id'), label=row.get('agent_polled_target'))

        # Create new HTML row
        result.append(dict(
            agent_program=row.get('agent_program'),
            agent_polled_target=link
            ))

    # Return sorted result
    return result
