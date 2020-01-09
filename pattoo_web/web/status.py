"""Pattoo version routes."""

# PIP libraries
from flask import Blueprint

# Define the various global variables
PATTOO_WEB_STATUS = Blueprint('PATTOO_WEB_STATUS', __name__)


@PATTOO_WEB_STATUS.route('')
def index():
    """Provide the status page.

    Args:
        None

    Returns:
        Home Page

    """
    # Return
    return 'The Pattoo Web is Operational.\n'
