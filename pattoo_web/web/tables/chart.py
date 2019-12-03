#!/usr/bin/env python3
"""Create homepage table."""

# PIP libraries
from flask_table import Table, Col

# Pattoo imports
from pattoo_shared.constants import PATTOO_WEB_SITE_PREFIX


class RawCol(Col):
    """Class to output whatever it is given without escaping."""

    def td_format(self, content):
        return content


class ItemTable(Table):
    """Table definition."""

    # Add attributes
    classes = ['table table-bordered']
    table_id = 'dataTable'
    html_attrs = {'width': '100%', 'cellspacing': '0'}

    # Column labels
    timeframe = RawCol('Timeframe')
    chart = RawCol('Chart')


class Item(object):
    """Table row definition."""

    def __init__(self, timeframe, chart):
        """Define row contents for table.

        Args:
            timeframe: Timeframe column
            chart: Chart column

        Returns:
            None

        """
        self.timeframe = timeframe
        self.chart = chart


def table(idx_datapoint, heading):
    """Process data for parsing to tables.

    Args:
        data: GraphQL dict

    Returns:
        html: FlaskTable Table object

    """
    # Process API data
    html = ItemTable(_flask_table_rows(idx_datapoint, heading))
    return html.__html__()


def _flask_table_rows(idx_datapoint, heading):
    """Create HTML table from data.

    Args:
        idx_datapoint: idx_datapoint
        heading: Heading for chart

    Returns:
        result: List of FlaskTable table row objects

    """
    # Initialize chart varialbes
    result = []
    url = (
        '{}/chart/{}/data'.format(PATTOO_WEB_SITE_PREFIX, idx_datapoint))
    link = ('''\
<div id="pattoo_simple_line_chart"></div>
<script type="text/javascript">
  SimpleLineChart("{}", "{}");
</script>'''.format(url, heading))

    # Create new HTML row
    result.append(dict(
        timeframe='',
        chart=link,
        ))
    return result
