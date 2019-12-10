#!/usr/bin/env python3
"""Create homepage table."""

# PIP libraries
from flask_table import Table, Col

# Pattoo imports
from pattoo_web import uri


class RawCol(Col):
    """Class to output whatever it is given without escaping."""

    def td_format(self, content):
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
    rows = _process_api_data(data)
    html = ItemTable(_flask_table_rows(rows))
    return html.__html__()


def _process_api_data(data):
    """Process GraphQL data for parsing to tables.

    Args:
        data: GraphQL dict

    Returns:
        rows: List of dicts of data to present

    """
    # Initialize key variables
    rows = []

    # Extract each datapoint
    datapoints = data['data']['allDatapoints']['edges']
    for datapoint in datapoints:
        # Initialize loop variables
        meta_row = []

        # Get the idx_datapoint
        idx_datapoint = datapoint['node']['idxDatapoint']

        # Extract the metadata
        metadata = datapoint['node']['glueDatapoint']['edges']
        data_dict = {'idx_datapoint': idx_datapoint}
        for item in metadata:
            key = item['node']['pair']['key']
            value = item['node']['pair']['value']

            # Skip entries that will clutter the output
            if key in [
                    'pattoo_agent_hostname', 'pattoo_agent_id',
                    'pattoo_agent_id', 'pattoo_agent_program']:
                continue

            if key == 'pattoo_key':
                data_dict['key'] = value
            elif key == 'pattoo_agent_polled_target':
                data_dict['target'] = value
            else:
                meta_row.append('{}: {}'.format(key, value))
        data_dict['metadata'] = meta_row

        # Convert to list of tuples
        rows.append(data_dict)

    # Print
    return rows


def _flask_table_rows(rows):
    """Create HTML table from data.

    Args:
        rows: List of dicts to put in HTML form

    Returns:
        result: List of FlaskTable table row objects

    """
    # Initialize key varialbes
    result = []

    # Assign
    for row in rows:
        # Get the key being referenced
        heading = row['key'].split(':')[0]
        target = row['target']
        metadata = row['metadata']

        # Create link to charts
        link = uri.chart_link(row['idx_datapoint'], target, heading)

        # Create new HTML row
        result.append(dict(
            target=target,
            key=row['key'],
            metadata='<p>{}</p>'.format('<br>'.join(metadata)),
            link=link
            ))
    return result
