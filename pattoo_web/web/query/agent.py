#!/usr/bin/env python3
"""Pattoo classes that manage GraphQL datapoint related queries."""

import sys

from pattoo_shared import log
from pattoo_web.phttp import get
from .datapoint import DataPoint


class DataPointsAgent():
    """Class to process the results of the GraphQL query below.

    {
      agent(id: "IDENTIFIER") {
        datapointAgent {
          edges {
            cursor
            node {
              id
              idxDatapoint
              idxAgent
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
                self._nodes = data[
                    'data']['agent']['datapointAgent'].get('edges')
            except:
                log_message = ('Invalid agent data to process.')
                log.log2warning(80015, log_message)
            try:
                self._page_info = data[
                    'data']['agent']['datapointAgent'].get('pageInfo')
            except:
                log_message = ('Invalid pageInfo data to process.')
                log.log2warning(80019, log_message)
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


class Agents():
    """Class to process the results of the GraphQL query below.

    {
      allAgent {
        edges {
          node {
            id
            idxAgent
            agentPolledTarget
            agentProgram
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
                self._nodes = data['data']['allAgent']['edges']
            except:
                log_message = ('Invalid agent data to process.')
                log.log2warning(80017, log_message)
            try:
                self._page_info = data[
                    'data']['allAgent'].get('pageInfo')
            except:
                log_message = ('Invalid pageInfo data to process.')
                log.log2warning(80018, log_message)

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

    def agents(self):
        """Return a list of Agent objects.

        Args:
            None

        Returns:
            result: List of DataPoint objects

        """
        # Return a list of Agent objects
        result = []
        for item in self._nodes:
            result.append(Agent(item))
        return result


class Agent():
    """Class to process the nodes of the GraphQL query below.

    {
      agent(id: "XXXXXXXXXXXXXXXX") {
        id
        idxAgent
        agentPolledTarget
        agentProgram
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
            # Result of 'agent' GraphQL query
            self._data = _data['data'].get('agent')
        else:
            # Result of 'allAgents' GraphQL query
            self._data = _data.get('node')

    def id(self):
        """Get GraphQL query datapoint 'id'.

        Args:
            None

        Returns:
            result: 'id' value

        """
        result = self._data.get('id')
        return result

    def idx_agent(self):
        """Get GraphQL query datapoint 'idxAgent'.

        Args:
            None

        Returns:
            result: 'idxAgent' value

        """
        result = self._data.get('idxAgent')
        return result

    def agent_polled_target(self):
        """Get GraphQL query datapoint 'agentPolledTarget'.

        Args:
            None

        Returns:
            result: 'agentPolledTarget' value

        """
        result = self._data.get('agentPolledTarget')
        return result

    def agent_program(self):
        """Get GraphQL query datapoint 'agentProgram'.

        Args:
            None

        Returns:
            result: 'agentProgram' value

        """
        result = self._data.get('agentProgram')
        return result


def agents():
    """Process an allAgent query.

    Args:
        None

    Returns:
        result: DataPoints object

    """
    # Initialize key variables
    query = """\
{
  allAgent {
    edges {
      node {
        id
        idxAgent
        agentPolledTarget
        agentProgram
        pairXlateGroup{
          id
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
    result = Agents(data)
    return result


def datapoints_agent(graphql_id, screen=None):
    """Get translations for the GraphQL ID of a datapointAgent query.

    Args:
        graphql_id: GraphQL ID
        screen: GraphQL filter for screening results

    Returns:
        result: DataPoint object

    """
    # Initialize key variables
    query = '''\
{
  agent(id: "IDENTIFIER") {
    datapointAgent SCREEN {
      edges {
        cursor
        node {
          id
          idxDatapoint
          idxAgent
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
}
'''.replace('IDENTIFIER', graphql_id)

    if screen is None:
        query = query.replace('SCREEN', '')
    else:
        query = query.replace('SCREEN', screen)

    # Get data from API server
    data = None

    # Get data from remote system
    try:
        data = get(query)
    except:
        _exception = sys.exc_info()
        log_message = ('Cannot connect to pattoo web API')
        log.log2exception(80016, _exception, message=log_message)

    # Return
    result = DataPointsAgent(data)
    return result
