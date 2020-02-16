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
                EXEC_DIR,
                os.pardir)), os.pardir)), os.pardir)), os.pardir))
_EXPECTED = (
    '{0}pattoo-web{0}tests{0}test_pattoo_web{0}web{0}tables'.format(os.sep))
if EXEC_DIR.endswith(_EXPECTED) is True:
    # We need to prepend the path in case the repo has been installed
    # elsewhere on the system using PIP. This could corrupt expected results
    sys.path.insert(0, ROOT_DIR)
else:
    print('''This script is not installed in the "{0}" directory. Please fix.\
'''.format(_EXPECTED))
    sys.exit(2)

from tests.libraries.configuration import UnittestConfig
from pattoo_web.web.query import agent
from pattoo_web.web.tables import home



AGENTS = {'data': {'allAgent': {'edges': [
    {'node': {'agentPolledTarget': 'localhost',
              'agentProgram': 'pattoo_agent_snmpd',
              'id': 'QWdlbnQ6MQ==',
              'idxAgent': '1'}},
    {'node': {'agentPolledTarget': 'that_host',
              'agentProgram': 'pattoo_agent_snmp_ifmibd',
              'id': 'QWdlbnQ6Mg==',
              'idxAgent': '2'}}]}}}


class TestRawCol(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method or function named __init__."""
        pass


class TestItemTable(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method or function named __init__."""
        pass


class TestItem(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method or function named __init__."""
        pass


class TestBasicFunctions(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    data = agent.Agents(AGENTS)

    def test_table(self):
        """Testing method or function named table."""
        result = home.table(self.data)

        # Test
        expected = '''\
<table cellspacing="0" class="table table-bordered" id="dataTable" \
width="100%">
<thead><tr><th>Agent Program</th><th>Target</th></tr></thead>
<tbody>
<tr><td>pattoo_agent_snmp_ifmibd</td><td><a href="/pattoo/agent/\
QWdlbnQ6Mg==">that_host</a></td></tr>
<tr><td>pattoo_agent_snmpd</td><td><a href="/pattoo/agent/QWdlbnQ6MQ==">\
localhost</a></td></tr>
</tbody>
</table>\
'''
        self.assertEqual(result, expected)

    def test__flask_table_rows(self):
        """Testing method or function named _flask_table_rows."""
        result = home._flask_table_rows(self.data)

        # Test
        expected = [
            {'agent_program': 'pattoo_agent_snmp_ifmibd',
             'agent_polled_target': '''\
<a href="/pattoo/agent/QWdlbnQ6Mg==">that_host</a>'''},
            {'agent_program': 'pattoo_agent_snmpd',
             'agent_polled_target': '''\
<a href="/pattoo/agent/QWdlbnQ6MQ==">localhost</a>'''}]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
