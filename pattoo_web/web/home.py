"""Pattoo version routes."""

# PIP libraries
from flask import Blueprint, render_template, abort

# Pattoo imports
from pattoo_web.phttp import get
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

    # Process the data
    if data is not None:
        # Initialize key variables
        table = home.table(data)
        return render_template('home.html', main_table=table)

    # Otherwise abort
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
