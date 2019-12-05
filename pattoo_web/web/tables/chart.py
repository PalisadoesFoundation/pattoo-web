#!/usr/bin/env python3
"""Create homepage table."""

# PIP libraries
from flask_table import Table, Col

# Pattoo imports
from pattoo_shared.constants import PATTOO_WEB_SITE_PREFIX
from pattoo_web import uri
from pattoo_web.constants import (
    DEFAULT_CHART_SIZE_SECONDS, SECONDS_IN_WEEK,
    SECONDS_IN_MONTH, SECONDS_IN_QUARTER, SECONDS_IN_YEAR)


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


class Table(object):
    """Class for creating a chart table."""

    def __init__(self, idx_datapoint, heading, device, secondsago):
        """Initialize the class.

        Args:
            idx_datapoint: DataPoint index
            heading: Heading for chart
            device: Device being charted
            secondsago: Time in the past from which to plot the chart

        Returns:
            None

        """
        # Initialize key variables
        self.idx_datapoint = idx_datapoint
        self.heading = heading
        self.device = device
        self.secondsago = secondsago

    def html(self):
        """Create HTML table from data.

        Args:
            None

        Returns:
            _html: FlaskTable Table object

        """
        # Initialize chart varialbes
        result = []
        restful_api_url = ('''{}/chart/{}/data?secondsago={}\
'''.format(PATTOO_WEB_SITE_PREFIX, self.idx_datapoint, self.secondsago))
        chart = ('''\
    <div id="pattoo_simple_line_chart"></div>
    <script type="text/javascript">
      SimpleLineChart("{}", "{}");
    </script>'''.format(restful_api_url, self.heading))
        timeframe = self._timeframe_links()

        # Create new HTML row
        result.append(dict(
            timeframe=timeframe,
            chart=chart,
            ))

        # Process API data
        _html = ItemTable(result)
        return _html.__html__()

    def _timeframe_links(self):
        """Create links for chart table.

        Args:
            None

        Returns:
            result: <a> links for various timeframes

        """
        # Initialize key variables
        result = ''
        timeframes = [
            ('Default', DEFAULT_CHART_SIZE_SECONDS),
            ('Week', SECONDS_IN_WEEK),
            ('Month', SECONDS_IN_MONTH),
            ('Quarter', SECONDS_IN_QUARTER),
            ('Year', SECONDS_IN_YEAR)
        ]

        # Create links
        for label, secondsago in timeframes:
            link = uri.chart_link(
                self.idx_datapoint,
                self.device,
                self.heading,
                label=label,
                secondsago=secondsago)
            result = '{}\n<p>{}</p>\n'.format(result, link)

        # Returns
        return result
