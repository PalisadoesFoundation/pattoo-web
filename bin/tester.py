#!/usr/bin/env python3
"""Pattoo agent data cache ingester.

Used to add data to backend database

"""

# Standard libraries
import sys
import os
from pprint import pprint

import requests
from flask_table import Table, Col

# Try to create a working PYTHONPATH
_BIN_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
_ROOT_DIRECTORY = os.path.abspath(os.path.join(_BIN_DIRECTORY, os.pardir))
if _BIN_DIRECTORY.endswith('/pattoo-web/bin') is True:
    sys.path.append(_ROOT_DIRECTORY)
else:
    print(
        'This script is not installed in the "pattoo-web/bin" directory. '
        'Please fix.')
    sys.exit(2)


# Pattoo imports
from pattoo_web.configuration import Config
from pattoo_shared import log


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
    device = Col('Device')
    key = Col('DataPoint')
    metadata = RawCol('Metadata')
    link = Col('Chart')


class Item(object):
    """Table row definition."""

    def __init__(self, device, key, metadata, link):
        """Define row contents for table.

        Args:
            device: Device name
            key: Key-value pair key
            metadata: Metadata of key
            link: Link to charted data

        Returns:
            None

        """
        self.device = device
        self.key = key
        self.metadata = metadata
        self.link = link


def main():
    """Ingest data."""
    # Initialize key variables
    success = False
    config = Config()
    query = """\
{
  allDatapoints {
    edges {
      node {
        idxDatapoint
        glueDatapoint {
          edges {
            node {
              pair {
                key
                value
              }
            }
          }
        }
      }
    }
  }
}
"""
    # Get the data from the GraphQL API
    url = config.web_api_server_url()
    try:
        response = requests.get(url, params={'query': query})

        # Trigger HTTP errors if present
        response.raise_for_status()
        success = True
    except requests.exceptions.Timeout as err:
        # Maybe set up for a retry, or continue in a retry loop
        log_message = ('''\
Timeout when attempting to access {}. Message: {}\
'''.format(url, err))
        log.log2warning(80000, log_message)
    except requests.exceptions.TooManyRedirects as err:
        # Tell the user their URL was bad and try a different one
        log_message = ('''\
Too many redirects when attempting to access {}. Message: {}\
'''.format(url, err))
        log.log2warning(80001, log_message)
    except requests.exceptions.HTTPError as err:
        log_message = ('''\
HTTP error when attempting to access {}. Message: {}\
'''.format(url, err))
        log.log2warning(80002, log_message)
    except requests.exceptions.RequestException as err:
        # catastrophic error. bail.
        log_message = ('''\
Exception when attempting to access {}. Message: {}\
'''.format(url, err))
        log.log2warning(80003, log_message)
    except:
        log_message = ('''API Failure: [{}, {}, {}]\
'''.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]))
        log.log2warning(80004, log_message)

    # Process the data
    if bool(success) is True:
        data = response.json()
        rows = process(data)
        html_table = ItemTable(table(rows))
        print(html_table.__html__())


def process(data):
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
        data_dict = {'idx': idx_datapoint}
        for item in metadata:
            key = item['node']['pair']['key']
            value = item['node']['pair']['value']

            # Skip entries that will clutter the output
            if key in [
                    'pattoo_agent_hostname', 'pattoo_agent_id',
                    'pattoo_source', 'pattoo_agent_program']:
                continue

            if key == 'pattoo_key':
                data_dict['key'] = value
            elif key == 'pattoo_agent_polled_device':
                data_dict['device'] = value
            else:
                meta_row.append('{}: {}'.format(key, value))
        data_dict['metadata'] = meta_row

        # Convert to list of tuples
        rows.append(data_dict)

    # Print
    return rows


def table(rows):
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
        result.append(dict(
            device=row['device'],
            key=row['key'],
            metadata='<p>{}</p>'.format('</p><p>'.join(row['metadata'])),
            link='Link'
            ))
    return result


if __name__ == '__main__':
    log.env()
    main()
