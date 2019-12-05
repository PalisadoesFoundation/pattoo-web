"""Module that defines universal constants used only by pattoo.

The aim is to have a single location for constants that may be used across
agents to prevent the risk of duplication.

"""

###############################################################################
# Constants for pattoo Web API
###############################################################################

PATTOO_WEBD_EXECUTABLE = 'pattoo-webd'
PATTOO_WEBD_PROXY = '{}-gunicorn'.format(
    PATTOO_WEBD_EXECUTABLE)

FOLDER_WEB_STATIC = 'theme/static'
FOLDER_WEB_TEMPLATE = 'theme/templates'
SECONDS_IN_DAY = 3600 * 24
SECONDS_IN_WEEK = SECONDS_IN_DAY * 7
SECONDS_IN_MONTH = SECONDS_IN_DAY * 30
SECONDS_IN_QUARTER = SECONDS_IN_DAY * 90
SECONDS_IN_YEAR = SECONDS_IN_DAY * 365
DEFAULT_CHART_SIZE_SECONDS = SECONDS_IN_DAY
