#!/usr/bin/env python3
"""Pattoo classes that manage GraphQL agent translation related queries."""

from pattoo_web.configuration import Config
from pattoo_web.translate import AgentPair
from pattoo_web.phttp import get


class AgentXlates():
    """Class to process the results of the GraphQL query below.

    {
      allAgentXlate {
        edges {
          node {
            id
            agentProgram
            translation
            language {
              code
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
            self._nodes = data['data']['allAgentXlate']['edges']
        else:
            self._nodes = []

    def agents(self):
        """Return a list of AgentXlate objects.

        Args:
            None

        Returns:
            result: List of AgentXlate objects

        """
        # Return a list of AgentXlate objects
        result = []
        for item in self._nodes:
            result.append(AgentXlate(item))
        return result


class AgentXlate():
    """Class to process the results of the GraphQL query below.

    {
      agentXlate(id: "XXXXXXXXXXXXXXXXXX") {
        id
        agentProgram
        translation
        language {
          code
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
            # Result of 'allAgentXlate' GraphQL query
            self._data = _data['data'].get('agentXlate')
        else:
            # Result of 'datapoint' GraphQL query
            self._data = _data.get('node')

    def id(self):
        """Get the id of the query.

        Args:
            None

        Returns:
            result: result

        """
        result = self._data.get('id')
        return result

    def language_code(self):
        """Get the language_code of the query.

        Args:
            None

        Returns:
            result: result

        """
        result = self._data['language'].get('code')
        return result

    def translation(self):
        """Get GraphQL query translation key-value pairs.

        Args:
            None

        Returns:
            result: Dict keyed by agent_program

        """
        # Return results for configured language
        result = {}
        language_code = Config().language()
        if self.language_code() == language_code:
            _translation = self._data.get('translation')
            agent_program = self._data.get('agentProgram')
            result[agent_program] = _translation
        return result


def translations():
    """Get translations for all id_pair_xlate_group GraphQL IDs.

    Args:
        None

    Returns:
        result: AgentPair object

    """
    # Initialize key variables
    query = '''\
{
  allAgentXlate {
    edges {
      node {
        id
        agentProgram
        translation
        language {
          code
        }
      }
    }
  }
}
'''
    # Get translations from API server
    query_result = get(query)
    result = AgentPair(AgentXlates(query_result).agents())
    return result


def translation(graphql_id):
    """Get translations for the GraphQL ID of a id_pair_xlate_group.

    Args:
        None

    Returns:
        result: AgentPair object

    """
    # Initialize key variables
    xlate_query = '''\
{
  agentXlate(id: "IDENTIFIER") {
    id
    agentProgram
    translation
    language {
      code
    }
  }
}
'''.replace('IDENTIFIER', graphql_id)

    # Get data from API server
    xlate_data = get(xlate_query)
    result = AgentPair([AgentXlate(xlate_data)])
    return result
