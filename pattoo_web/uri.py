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


def prev_next(request, status, count=20):
    """Create next and previous links.

    Args:
        request: Python Flask request object
        status: constants.PageInfo object
        count: The number of items to get

    Returns:
        result: tuple of HTML <a> tags (prev, next)

    """
    # Initialize key variables
    base_uri = '{}{}'.format(request.script_root, request.path)
    pointer = integerize_arg(request.args.get('first'))
    item_count = integerize_arg(request.args.get('last'))

    # Determine where to end the selection
    if pointer is None:
        stop = count
    else:
        stop = pointer

    # Determine the length of the selection's tail
    if item_count is None:
        last = stop
    else:
        last = item_count

    # Make sure the tail isn't longer than the selection
    if last > stop:
        last = stop

    # Create links
    if status.hasPreviousPage is False:
        _prev = ''
    else:
        _prev = ('''<a href="{}?first={}&last={}">&lt; Prev</a>\
'''.format(base_uri, int(stop - count), last))

    if status.hasNextPage is False:
        _next = ''
    else:
        _next = ('''<a href="{}?first={}&last={}">Next &gt;</a>\
'''.format(base_uri, int(stop + count), last))

    # Return
    result = (_prev, _next)
    return result


def graphql_filter(request, count=20):
    """Create a GraphQL formatted pagination filter.

    Args:
        request: Python Flask request object
        count: Maximum number of results to return

    Returns:
        result: GraphQL formatted pagination filter

    """
    # Get URI arguments
    _first = integerize_arg(request.args.get('first'))
    _last = integerize_arg(request.args.get('last'))

    if _first is None:
        prefix = 'first: {}'.format(count)
    else:
        prefix = 'first: {}'.format(_first)

    if _last is None:
        suffix = 'last: {}'.format(count)
    else:
        suffix = 'last: {}'.format(_last)

    # Return
    result = '({} {})'.format(prefix, suffix)
    return result
