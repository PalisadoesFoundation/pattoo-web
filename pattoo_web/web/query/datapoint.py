#!/usr/bin/env python3
"""Pattoo classes that manage GraphQL datapoint related queries."""

from pattoo_web.phttp import get


class DataPoints(object):
    """Class to process the results of the GraphQL query below.

    {
      allDatapoints {
        edges {
          node {
            id
            idxDatapoint
            agent {
              agentPolledTarget
              agentGroup {
                pairXlateGroup {
                  idxPairXlateGroup
                  id
                }
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
        if bool(data) is True:
            self._nodes = data['data']['allDatapoints']['edges']
        else:
            self._nodes = []
        self.valid = bool(self._nodes)

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


class DataPoint(object):
    """Class to process the results of the GraphQL query below.

    {
      datapoint(id: "XXXXXXXXXXXXXXXX") {
        id
        idxDatapoint
        agent {
          agentPolledTarget
          agentGroup {
            pairXlateGroup {
              idxPairXlateGroup
              id
            }
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
            # Result of 'allDatapoints' GraphQL query
            data = _data['data'].get('datapoint')
        else:
            # Result of 'datapoint' GraphQL query
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

    def idx_pair_xlate_group(self):
        """Get GraphQL query datapoint 'idxPairXlateGroup'.

        Args:
            None

        Returns:
            result: 'idxPairXlateGroup' value

        """
        result = self._datapoint[
            'agent']['agentGroup']['pairXlateGroup'].get('idxPairXlateGroup')
        return result

    def id_pair_xlate_group(self):
        """Get GraphQL query datapoint 'idxPairXlateGroup:id'.

        Args:
            None

        Returns:
            result: 'idxPairXlateGroup:id' value

        """
        result = self._datapoint[
            'agent']['agentGroup']['pairXlateGroup'].get('id')
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
      node {
        id
        idxDatapoint
        agent {
          agentPolledTarget
          agentGroup {
            pairXlateGroup {
              idxPairXlateGroup
            }
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
  }
}
"""

    # Get data from API server
    data = get(query)
    result = DataPoints(data)
    return result


def datapoint(graphql_id):
    """Get translations for the GraphQL ID of a id_pair_xlate_group.

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
      agentPolledTarget
      agentGroup {
        pairXlateGroup {
          idxPairXlateGroup
          id
        }
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
    data = get(query)
    result = DataPoint(data)
    return result