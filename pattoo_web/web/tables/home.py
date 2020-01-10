#!/usr/bin/env python3
"""Create homepage table."""

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
    index = Col('#')
    agent_program = Col('Agent Program')
    agent_polled_target = RawCol('Target')


class Item(object):
    """Table row definition."""

    def __init__(self, index, agent_program, agent_polled_target):
        """Define row contents for table.

        Args:
            index: Agent table idx_agent
            agent_program: Key-value pair key
            agent_polled_target: Target polled by agent

        Returns:
            None

        """
        self.index = index
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

    # Get agent_program translations
    translate = translations()

    # Process the DataPoints
    for _agent in _agents.agents():
        _id = _agent.id()
        index = _agent.idx_agent()
        agent_polled_target = _agent.agent_polled_target()
        agent_program = translate.agent_program(_agent.agent_program())

        # Create link to charts
        link = uri.agent_link(_id, label=agent_polled_target)

        # Create new HTML row
        result.append(dict(
            index=index,
            agent_program=agent_program,
            agent_polled_target=link
            ))

    return result
