"""Module that defines URIs for web pages."""

# Pattoo imports
from pattoo_shared.constants import PATTOO_WEB_SITE_PREFIX
from pattoo_web.constants import DEFAULT_CHART_SIZE_SECONDS


def chart_link(_id, label='Chart Data', secondsago=None):
    """Return link to chart page.

    Args:
        _id: GraphQL ID for the datapoint

    Returns:
        links: Link

    """
    #
    if bool(secondsago) is False:
        secondsago = DEFAULT_CHART_SIZE_SECONDS

    # Create link to charts
    link = ('''\
<a href="{}/chart/datapoint/{}?secondsago={}">{}</a>\
'''.format(PATTOO_WEB_SITE_PREFIX, _id, secondsago, label))

    # Returns
    return link


def agent_link(_id, label='Agent Data'):
    """Return link to agent page.

    Args:
        _id: GraphQL ID for the agent

    Returns:
        link: Link

    """
    # Create link to agent
    link = ('''\
<a href="{}/agent/{}">{}</a>\
'''.format(PATTOO_WEB_SITE_PREFIX, _id, label))

    # Returns
    return link


def integerize_arg(value):
    """Convert value received as a URL arg to integer.

    Args:
        value: Value to convert

    Returns:
        result: Value converted to iteger

    """
    # Try edge case
    if value is True:
        return None
    if value is False:
        return None

    # Try conversion
    try:
        result = int(value)
    except:
        result = None

    # Return
    return result
