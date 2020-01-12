#!/usr/bin/env python3
"""Test pattoo configuration."""

import os
import unittest
import sys

# Try to create a working PYTHONPATH
EXEC_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(
    os.path.abspath(os.path.join(
        os.path.abspath(os.path.join(
            EXEC_DIR, os.pardir)), os.pardir)), os.pardir))

if EXEC_DIR.endswith(
        '/pattoo-web/tests/test_pattoo_web/web') is True:
    # We need to prepend the path in case PattooShared has been installed
    # elsewhere on the system using PIP. This could corrupt expected results
    sys.path.insert(0, ROOT_DIR)
else:
    print('''\
This script is not installed in the "pattoo-web/tests/test_pattoo_web\
/web" directory. Please fix.''')
    sys.exit(2)

from tests.libraries.configuration import UnittestConfig
from pattoo_web.web.query import agent as agent_query
from pattoo_web.web.tables import chart
from pattoo_web.web.query.datapoint import DataPoint


# Create a common dataset for testing
DATAPOINT = {'data': {'datapoint': {
    'agent': {'agentGroup': {'pairXlateGroup': {
        'id': 'UGFpclhsYXRlR3JvdXA6MQ==',
        'idxPairXlateGroup': '10'}},
              'agentPolledTarget': 'this_pc',
              'agentProgram': 'pattoo_test_snmpd'},
    'glueDatapoint': {'edges': [
        {'node': {'pair': {'key': 'pattoo_agent_snmpd_oid',
                           'value': '.1.3.6.1.2.1.2.2.1.10.345'}}},
        {'node': {'pair': {
            'key': 'pattoo_key',
            'value': '123'}}}]},
    'id': 'RGF0YVBvaW50OjM=',
    'idxDatapoint': '3'}}}


class TestRawCol(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method / function __init__."""
        pass


class TestItemTable(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method / function __init__."""
        pass


class TestItem(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method / function __init__."""
        pass


class TestTable(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method / function __init__."""
        pass

    def test_html(self):
        """Testing method / function html."""
        secondsago = 500
        point = DataPoint(DATAPOINT)
        tester = chart.Table(point, secondsago)

        # Test
        result = tester.html()
        expected = '''\
<table cellspacing="0" class="table table-bordered" id="dataTable" \
width="100%">
<thead><tr><th>Timeframe</th><th>Chart</th></tr></thead>
<tbody>
<tr><td>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=86400">Default</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago=\
604800">Week</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago=\
2592000">Month</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago=\
7776000">Quarter</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=31536000">Year</a></p>
</td><td><div id="pattoo_simple_line_chart"></div>
<script type="text/javascript">
  SimpleLineChart("/pattoo/web/chart/3/data?secondsago=500", "this_pc");
</script></td></tr>
</tbody>
</table>\
'''
        self.assertEqual(result, expected)

    def test__timeframe_links(self):
        """Testing method / function _timeframe_links."""
        secondsago = 500
        point = DataPoint(DATAPOINT)
        tester = chart.Table(point, secondsago)

        # Test
        result = tester._timeframe_links()
        expected = '''
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=86400">Default</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=604800">Week</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=2592000">Month</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=7776000">Quarter</a></p>
<p><a href="/pattoo/web/chart/datapoint/RGF0YVBvaW50OjM=?secondsago\
=31536000">Year</a></p>
'''
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
