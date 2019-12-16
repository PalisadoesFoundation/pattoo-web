"""Pattoo version routes."""

import sys

# PIP libraries
from flask import Blueprint, render_template, abort
import requests

# Pattoo imports
from pattoo_shared import log
from pattoo_web.configuration import Config
from pattoo_web.web.tables import home

# Define the various global variables
PATTOO_WEB_HOME = Blueprint('PATTOO_WEB_HOME', __name__)


@PATTOO_WEB_HOME.route('/')
def route_data():
    """Provide data from the Data table.

    Args:
        None

    Returns:
        None

    """
    # Initialize key variables
    success = False
    config = Config()
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
        # Initialize key variables
        data = response.json()
        table = home.table(data)
        return render_template('home.html', main_table=table)
    else:
        abort(404)


@PATTOO_WEB_HOME.route('/status')
def index():
    """Provide the status page.

    Args:
        None

    Returns:
        Home Page

    """
    # Return
    return 'The Pattoo Web is Operational.\n'
