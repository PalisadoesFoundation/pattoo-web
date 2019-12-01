"""Pattoo version routes."""

# PIP libraries
from flask import Blueprint, jsonify, request, render_template

# Define the various global variables
PATTOO_WEB_HOME = Blueprint('PATTOO_WEB_HOME', __name__)


@PATTOO_WEB_HOME.route('/')
def route_data():
    """Provide data from the Data table.

    Args:
        idx_checksum: Checksum.idx_checksum key

    Returns:
        _result: JSONify list of dicts {timestamp: value} from the Data table.

    """
    # Initialize key variables
    return render_template('index.html')


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
