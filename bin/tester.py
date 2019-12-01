#!/usr/bin/env python3
"""Pattoo agent data cache ingester.

Used to add data to backend database

"""

# Standard libraries
import sys
import os
from pprint import pprint

import requests

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


def main():
    """Ingest data."""
    # Initialize key variables
    rows = []
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
    response = requests.get(url, params={'query': query})
    data = response.json()
    datapoints = data['data']['allDatapoints']['edges']

    for datapoint in datapoints:
        idx_datapoint = datapoint['node']['idxDatapoint']
        metadata = datapoint['node']['glueDatapoint']['edges']
        data_dict = {'idx': idx_datapoint}
        _metadata = []
        for item in metadata:
            key = item['node']['pair']['key']
            value = item['node']['pair']['value']

            # Skip entries that will clutter the output
            if key in [
                    'pattoo_agent_hostname', 'pattoo_agent_id',
                    'pattoo_source', 'pattoo_agent_program']:
                continue

            if key == 'pattoo_key':
                data_dict['Key'] = value
            elif key == 'pattoo_agent_polled_device':
                data_dict['Device'] = value
            else:
                _metadata.append((key, value))
        data_dict['metadata'] = _metadata

        # Convert to list of tuples
        rows.append(data_dict)

        # Print
        pprint(rows)
        # print('\tkey: {}'.format(key))
        # print('\tvalue: {}'.format(value))


if __name__ == '__main__':
    main()
