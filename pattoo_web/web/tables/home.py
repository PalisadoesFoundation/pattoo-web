#!/usr/bin/env python3
"""Create homepage table."""

# PIP libraries
from flask_table import Table, Col

# Pattoo imports
from pattoo_web import uri
from pattoo_web.web.query.datapoint import DataPoints


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
    target = Col('Target')
    key = Col('DataPoint')
    metadata = RawCol('Metadata')
    link = RawCol('Chart')


class Item(object):
    """Table row definition."""

    def __init__(self, target, key, metadata, link):
        """Define row contents for table.

        Args:
            target: Target name
            key: Key-value pair key
            metadata: Metadata of key
            link: Link to charted data

        Returns:
            None

        """
        self.target = target
        self.key = key
        self.metadata = metadata
        self.link = link


def table(data):
    """Process GraphQL data for parsing to tables.

    Args:
        data: GraphQL dict

    Returns:
        html: FlaskTable Table object

    """
    # Process API data
    html = ItemTable(_flask_table_rows(data))
    return html.__html__()


def _flask_table_rows(data):
    """Create HTML table from data.

    Args:
        rows: List of dicts to put in HTML form

    Returns:
        result: List of FlaskTable table row objects

    """
    # Initialize key varialbes
    result = []

    datapoints = DataPoints(data)
    for datapoint in datapoints.datapoints():
        _id = datapoint.id()
        target = datapoint.agent_polled_target()
        key = datapoint.pattoo_key()

        # Get key_value_pairs
        key_value_pairs = datapoint.key_value_pairs()
        metadata = [
            '{}: {}'.format(key, value) for key, value in key_value_pairs]

        # Create link to charts
        link = uri.chart_link(_id)

        # Create new HTML row
        result.append(dict(
            target=target,
            key=key,
            metadata='<p>{}</p>'.format('<br>'.join(metadata)),
            link=link
            ))
    return result
