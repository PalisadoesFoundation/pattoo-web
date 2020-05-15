#!/usr/bin/env python3
"""Pattoo classes that manage GraphQL datapoint related queries."""

import sys
from pattoo_shared import log
from pattoo_web.phttp import get


class DataPoints():
    """Class to process the results of the GraphQL query below.

    {
      allDatapoints {
        edges {
          cursor
          node {
            id
            idxDatapoint
            agent {
              agentProgram
              agentPolledTarget
              idxPairXlateGroup
              pairXlateGroup{
                id
              }
            }
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
        pageInfo {
          startCursor
          endCursor
          hasNextPage
          hasPreviousPage
        }
      }
    }

    """

    def __init__(self, data):
        """Initialize the class.

        Args:
            data: Dict of results from the GraphQL query

        Returns:
            None

        """
        # Initialize the class
        self._nodes = []
        self._page_info = {}

        # Check for validity
        if bool(data) is True:
            try:
                self._nodes = data['data']['allDatapoints'].get('edges')
            except:
                log_message = ('Invalid datapoint data to process.')
                log.log2warning(80012, log_message)
            try:
                self._page_info = data['data']['allDatapoints'].get('pageInfo')
            except:
                log_message = ('Invalid pageInfo data to process.')
                log.log2warning(80013, log_message)

        self.valid = bool(self._nodes)

    def start_cursor(self):
        """Return startCursor value.

        Args:
            None

        Returns:
            result: startCursor value

        """
        # Return
        result = self._page_info.get('startCursor')
        return result

    def end_cursor(self):
        """Return endCursor value.

        Args:
            None

        Returns:
            result: endCursor value

        """
        # Return
        result = self._page_info.get('endCursor')
        return result

    def has_next_page(self):
        """Return hasNextPage value.

        Args:
            None

        Returns:
            result: hasNextPage value

        """
        # Return
        result = self._page_info.get('hasNextPage')
        return result

    def has_previous_page(self):
        """Return hasPreviousPage value.

        Args:
            None

        Returns:
            result: hasPreviousPage value

        """
        # Return
        result = self._page_info.get('hasPreviousPage')
        return result

    def datapoints(self):
        """Return a list of DataPoint objects.

        Args:
            None

        Returns:
            result: List of DataPoint objects

        """
        # Return a list of DataPoint objects
        result = []
        for item in self._nodes:
            result.append(DataPoint(item))
        return result


class DataPoint():
    """Class to process the results of the GraphQL query below.

    {
      datapoint(id: "IDENTIFIER") {
        id
        idxDatapoint
        agent {
          agentProgram
          agentPolledTarget
          idxPairXlateGroup
          pairXlateGroup{
            id
          }
        }
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

    """

    def __init__(self, _data):
        """Initialize the class.

        Args:
            _data: Dict of results from the GraphQL query


        Returns:
            None

        """
        # Initialize the class
        if 'data' in _data:
            # Result of 'datapoint' GraphQL query
            data = _data['data'].get('datapoint')
        else:
            # Result of 'allDatapoints' GraphQL query
            data = _data.get('node')

        self.valid = bool(data)
        if self.valid is True:
            self._nodes = data['glueDatapoint']['edges']
            self._datapoint = data
            self._kvps = self._key_value_pairs()

    def id(self):
        """Get GraphQL query datapoint 'id'.

        Args:
            None

        Returns:
            result: 'id' value

        """
        result = self._datapoint.get('id')
        return result

    def idx_datapoint(self):
        """Get GraphQL query datapoint 'idxDatapoint'.

        Args:
            None

        Returns:
            result: 'idxDatapoint' value

        """
        result = self._datapoint.get('idxDatapoint')
        return result

    def agent_polled_target(self):
        """Get GraphQL query datapoint 'agentPolledTarget'.

        Args:
            None

        Returns:
            result: 'agentPolledTarget' value

        """
        result = self._datapoint['agent'].get('agentPolledTarget')
        return result

    def agent_program(self):
        """Get GraphQL query datapoint 'agentProgram'.

        Args:
            None

        Returns:
            result: 'agentProgram' value

        """
        result = self._datapoint['agent'].get('agentProgram')
        return result

    def idx_pair_xlate_group(self):
        """Get GraphQL query datapoint 'idxPairXlateGroup'.

        Args:
            None

        Returns:
            result: 'idxPairXlateGroup' value

        """
        result = self._datapoint[
            'agent'].get('idxPairXlateGroup')
        return result

    def id_pair_xlate_group(self):
        """Get GraphQL query datapoint 'idxPairXlateGroup:id'.

        Args:
            None

        Returns:
            result: 'idxPairXlateGroup:id' value

        """
        result = self._datapoint[
            'agent']['pairXlateGroup'].get('id')
        return result

    def pattoo_key(self):
        """Get the pattoo_key.

        Args:
            None

        Returns:
            result: pattoo_key

        """
        # Return result
        result = self._kvps['pattoo_key']
        return result

    def key_value_pairs(self):
        """Get GraphQL query datapoint key-value pairs.

        Args:
            None

        Returns:
            result: List of tuples [(key, value), (key, value), ...]

        """
        # Return result
        result = [(key, value) for key, value in self._kvps.items() if (
            key != 'pattoo_key')]
        result.sort()
        return result

    def _key_value_pairs(self):
        """Get GraphQL query datapoint key-value pairs.

        Args:
            None

        Returns:
            result: Dict keyed by key

        """
        # Return result
        result = {}
        for node in self._nodes:
            key = node['node']['pair'].get('key')
            value = node['node']['pair'].get('value')
            result[key] = value
        return result


def datapoints():
    """Get DataPoints entry for all database datapoints.

    Args:
        None

    Returns:
        result: DataPoints object

    """
    # Initialize key variables
    query = """\
{
  allDatapoints {
    edges {
      cursor
      node {
        id
        idxDatapoint
        agent {
          agentProgram
          agentPolledTarget
          idxPairXlateGroup
          pairXlateGroup{
            id
          }
        }
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
    pageInfo {
      startCursor
      endCursor
      hasNextPage
      hasPreviousPage
    }
  }
}
"""

    # Get data from API server
    data = get(query)
    result = DataPoints(data)
    return result


def datapoint(graphql_id):
    """Get translations for the GraphQL ID of a datapoint query.

    Args:
        graphql_id: GraphQL ID

    Returns:
        result: DataPoint object

    """
    # Initialize key variables
    query = '''\
{
  datapoint(id: "IDENTIFIER") {
    id
    idxDatapoint
    agent {
      agentProgram
      agentPolledTarget
      idxPairXlateGroup
      pairXlateGroup{
        id
      }
    }
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
'''.replace('IDENTIFIER', graphql_id)

    # Get data from API server
    data = None

    # Get data from remote system
    try:
        data = get(query)
    except:
        _exception = sys.exc_info()
        log_message = ('Cannot connect to pattoo web API')
        log.log2exception(80014, _exception, message=log_message)

    # Return
    result = DataPoint(data)
    return result
