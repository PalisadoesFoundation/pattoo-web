#!/usr/bin/env python3
"""Pattoo classes that manage GraphQL datapoint related queries."""

from pattoo_web.configuration import Config
from pattoo_web.translate import KeyPair
from pattoo_web.phttp import get


class PairXlates(object):
    """Class to process the results of the GraphQL query below.

    {
      allPairXlateGroup {
        edges {
          node {
            idxPairXlateGroup
            pairXlatePairXlateGroup {
              edges {
                node {
                  key
                  description
                  language {
                    code
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
            self._nodes = data['data']['allPairXlateGroup']['edges']
        else:
            self._nodes = []

    def datapoints(self):
        """Return a list of PairXlate objects.

        Args:
            None

        Returns:
            result: List of PairXlate objects

        """
        # Return a list of PairXlate objects
        result = []
        for item in self._nodes:
            result.append(PairXlate(item))
        return result


class PairXlate(object):
    """Class to process the results of the GraphQL query below.

    {
      pairXlateGroup(id: "XXXXXXXXXXXXXXXXXX") {
        idxPairXlateGroup
        pairXlatePairXlateGroup {
          edges {
            node {
              key
              description
              language {
                code
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
            # Result of 'allPairXlateGroup' GraphQL query
            data = _data['data'].get('pairXlateGroup')
        else:
            # Result of 'datapoint' GraphQL query
            data = _data.get('node')

        self._idx_pair_xlate_group = data['idxPairXlateGroup']
        self._nodes = data['pairXlatePairXlateGroup']['edges']
        self._translations = self._lookup()

    def idx_pair_xlate_group(self):
        """Get the idx_pair_xlate_group of the query.

        Args:
            None

        Returns:
            result: result

        """
        result = self._idx_pair_xlate_group
        return result

    def translations(self):
        """Get GraphQL query translation key-value pairs.

        Args:
            None

        Returns:
            result: Dict keyed by idx_pair_xlate_group

        """
        result = {}
        result[self._idx_pair_xlate_group] = self._translations
        return result

    def _lookup(self):
        """Get key-value pairs that match the system language.

        Args:
            None

        Returns:
            result: Dict keyed by key

        """
        # Return result
        result = {}
        system_language_code = Config().language()
        for node in self._nodes:
            key = node['node'].get('key')
            value = node['node'].get('description')
            code = node['node']['language'].get('code')
            if code != system_language_code:
                continue
            result[key] = value
        return result


def translations():
    """Get translations for all id_pair_xlate_group GraphQL IDs.

    Args:
        None

    Returns:
        result: KeyPair object

    """
    # Initialize key variables
    query = '''\
{
  allPairXlateGroup {
    edges {
      node {
        idxPairXlateGroup
        pairXlatePairXlateGroup {
          edges {
            node {
              key
              description
              language {
                code
              }
            }
          }
        }
      }
    }
  }
}

'''
    # Get translations from API server
    query_result = get(query)
    result = KeyPair(PairXlates(query_result).datapoints())
    return result


def translation(graphql_id):
    """Get translations for the GraphQL ID of a id_pair_xlate_group.

    Args:
        None

    Returns:
        result: KeyPair object

    """
    # Initialize key variables
    xlate_query = '''\
{
  pairXlateGroup(id: "IDENTIFIER") {
    idxPairXlateGroup
    pairXlatePairXlateGroup {
      edges {
        node {
          key
          description
            language {
              code
            }
        }
      }
    }
  }
}
'''.replace('IDENTIFIER', graphql_id)

    # Get data from API server
    xlate_data = get(xlate_query)
    result = KeyPair([PairXlate(xlate_data)])
    return result
