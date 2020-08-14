"""Pattoo version routes."""

import sys

# PIP libraries
import requests

# Pattoo imports
from pattoo_shared import log
from pattoo_web.configuration import Config


def get(query):
    """Get pattoo API server GraphQL query results.

    Args:
        query: GraphQL query string

    Returns:
        result: Dict of JSON response

    """
    # Initialize key variables
    success = False
    config = Config()
    result = None

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
        result = response.json()
    return result
