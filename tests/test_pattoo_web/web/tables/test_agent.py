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
            os.path.abspath(os.path.join(
                EXEC_DIR, os.pardir)), os.pardir)), os.pardir)), os.pardir))

if EXEC_DIR.endswith(
        '/pattoo-web/tests/test_pattoo_web/web/tables') is True:
    # We need to prepend the path in case PattooShared has been installed
    # elsewhere on the system using PIP. This could corrupt expected results
    sys.path.insert(0, ROOT_DIR)
else:
    print('''\
This script is not installed in the "pattoo-web/tests/test_pattoo_web\
/tables/web" directory. Please fix.''')
    sys.exit(2)


from tests.libraries.configuration import UnittestConfig
from pattoo_web.web.query import agent as agent_query
from pattoo_web.web.tables import agent as agent_table


DATAPOINT_AGENT = {'data': {'agent': {'datapointAgent': {'edges': [
    {'node': {'agent': {'agentGroup': {
        'pairXlateGroup': {'id': 'UGFpclhsYXRlR3JvdXA6MQ==',
                           'idxPairXlateGroup': '1'}},
                        'agentPolledTarget': 'localhost',
                        'agentProgram': 'pattoo_agent_snmpd'},
              'glueDatapoint': {'edges': [
                  {'node': {'pair': {
                      'key': 'pattoo_agent_snmpd_oid',
                      'value': '.1.3.6.1.2.1.2.2.1.16.3'}}},
                  {'node': {'pair': {
                      'key': 'pattoo_key',
                      'value': 'pattoo_agent_snmpd_.1.3.6.1.2.1.2.2.1.16'}}}]},
              'id': 'RGF0YVBvaW50OjY=',
              'idxDatapoint': '948474',
              'idxAgent': '1'}}]}}}}


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


class TestBasicFunctions(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test_table(self):
        """Testing method / function table."""
        datapoints = agent_query.DataPointsAgent(DATAPOINT_AGENT)
        result = agent_table.table(datapoints)

        # Test
        expected = ('''\
<table cellspacing="0" class="table table-bordered" \
id="dataTable" width="100%">
<thead><tr><th>Target</th><th>DataPoint</th><th>\
Metadata</th><th>Chart</th></tr></thead>
<tbody>
<tr><td>localhost</td><td>pattoo_agent_snmpd_.1.3.6.1.2.1.2.2.1.16\
</td><td><p>Pattoo Agent: pattoo_agent_snmpd<br>pattoo_agent_snmpd_oid: \
.1.3.6.1.2.1.2.2.1.16.3</p></td><td><a href="/pattoo/chart/datapoint/\
RGF0YVBvaW50OjY=?secondsago=86400">Chart Data</a></td></tr>
</tbody>
</table>\
''')
        self.assertEqual(result, expected)

    def test__flask_table_rows(self):
        """Testing method / function _flask_table_rows."""
        datapoints = agent_query.DataPointsAgent(DATAPOINT_AGENT)
        result = agent_table._flask_table_rows(datapoints)

        # Test
        expected = [{
            'target': 'localhost',
            'key': 'pattoo_agent_snmpd_.1.3.6.1.2.1.2.2.1.16',
            'metadata': '''\
<p>Pattoo Agent: pattoo_agent_snmpd<br>pattoo_agent_snmpd_oid: \
.1.3.6.1.2.1.2.2.1.16.3</p>''',
            'link': '''\
<a href="/pattoo/chart/datapoint/RGF0YVBvaW50OjY=?secondsago=86400">\
Chart Data</a>'''}]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
