#!/usr/bin/env python3
"""Create homepage table."""

# PIP libraries
from flask_table import Table as _Table
from flask_table import Col

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


class ChartTable(_Table):
    """Table definition."""

    # Add attributes
    classes = ['table table-bordered']
    table_id = 'dataTable'
    html_attrs = {'width': '100%', 'cellspacing': '0'}

    # Column labels
    timeframe = RawCol('Timeframe')
    chart = RawCol('Chart')


class Table():
    """Class for creating a chart table."""

    def __init__(self, point_xlate, secondsago=DEFAULT_CHART_SIZE_SECONDS):
        """Initialize the class.

        Args:
            point_xlate: pattoo_web.constants.DataPointTranslations object
            secondsago: Time in the past from which to plot the chart

        Returns:
            None

        """
        # Initialize key variables
        self._point_xlate = point_xlate
        self._secondsago = secondsago

    def html(self):
        """Create HTML table from data.

        Args:
            None

        Returns:
            _html: FlaskTable Table object

        """
        # Initialize chart varialbes
        datapoint = self._point_xlate.datapoint
        result = []
        idx_datapoint = datapoint.idx_datapoint()
        div_id = 'pattoo_simple_line_chart_{}'.format(idx_datapoint)
        restful_api_url = ('''{}/chart/{}/data?secondsago={}\
'''.format(PATTOO_WEB_SITE_PREFIX, idx_datapoint, self._secondsago))
        chart = ('''\
<div id="{0}"></div>
<script type="text/javascript">
  SimpleLineChart("{1}", "{2}", "{3}", "#{0}");
</script>\
'''.format(div_id,
           restful_api_url,
           datapoint.agent_polled_target(),
           self._point_xlate.pattoo_key_translation.units))
        timeframe = self._timeframe_links()

        # Create new HTML row
        result.append(dict(
            timeframe=timeframe,
            chart=chart,
            ))

        # Process API data
        html_table = ChartTable(result).__html__()
        final_html = _wrapper(html_table, self._point_xlate)
        return final_html

    def _timeframe_links(self):
        """Create links for chart table.

        Args:
            None

        Returns:
            result: <a> links for various timeframes

        """
        # Initialize key variables
        datapoint = self._point_xlate.datapoint
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
                datapoint.id(),
                label=label,
                secondsago=secondsago)
            result = '{}\n<li>{}</li>'.format(result, link)
        result = '\n<ul>{}\n</ul>\n'.format(result)

        # Returns
        return result


def _wrapper(html_table, point_xlate):
    """Wrap HTML with card.

    Args:
        heading: Heading for HTML
        html_table: HTML to wrap
        point_xlate: Metadata translations

    Returns:
        result: Wrapped HTML

    """
    # Format HTML for return
    result = '''\
<!-- Table -->
<div class="card shadow mb-4">
  <div class="card-header py-3">
    <h6 class="m-0 font-weight-bold text-primary">{0}</h6>
  </div>
  <div class="card-body">
    {2}
    <hr>
    <div class="table-responsive">
        {1}
    </div>
  </div>
</div>
<!-- End Table -->\
'''.format(point_xlate.pattoo_key_translation.text,
           html_table,
           _footer(point_xlate))
    return result


def _footer(point_xlate):
    """Create a footer to use for the chart.

    Args:
        point: DataPoint object

    Returns:
        result: Footer

    """
    # Initialize key variables
    result = ''

    # Process
    for (meta, value) in point_xlate.metadata_translations:
        # Translate key
        text = meta.text
        result = '{}{}: {}<br>'.format(result, text, value)

    # Return
    result = '<p>{}</p>'.format(result)
    return result
