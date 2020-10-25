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
    '{0}pattoo-web{0}tests{0}test_pattoo_web{0}web{0}query'.format(os.sep))
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


# Create a common dataset for testing
AGENTS = {'data': {'allAgent': {
    'pageInfo': {
        'endCursor': 'YXJyYXljb25uZWN0aW9uOjM1NTQ=',
        'hasNextPage': False,
        'hasPreviousPage': False,
        'startCursor': 'YXJyYXljb25uZWN0aW9uOjA='
    },
    'edges': [
        {'node': {'agentPolledTarget': 'localhost',
                  'agentProgram': 'pattoo_agent_snmpd',
                  'id': 'QWdlbnQ6MQ==',
                  'idxAgent': '1'}},
        {'node': {'agentPolledTarget': 'that_host',
                  'agentProgram': 'pattoo_agent_snmp_ifmibd',
                  'id': 'QWdlbnQ6Mg==',
                  'idxAgent': '2'}}]}}}

AGENT = {'data': {
    'agent': {'id': 'polar_bear',
              'idxAgent': '7',
              'agentPolledTarget': 'teddy_bear',
              'agentProgram': 'koala_bear'}}}


DATAPOINT_AGENT = {'data': {'agent': {'datapointAgent': {
    'pageInfo': {
        'endCursor': 'AAYXJyYXljb25uZWN0aW9uOjM1NTQ=',
        'hasNextPage': False,
        'hasPreviousPage': False,
        'startCursor': 'AAYXJyYXljb25uZWN0aW9uOjA='
    },
    'edges': [
        {'node': {'agent': {'pairXlateGroup': {
            'id': 'UGFpclhsYXRlR3JvdXA6MQ=='},
                            'agentPolledTarget': 'localhost',
                            'idxPairXlateGroup': '1',
                            'agentProgram': 'pattoo_agent_snmpd'},
                  'glueDatapoint': {'edges': [
                      {'node': {'pair': {
                          'key': 'pattoo_agent_snmpd_oid',
                          'value': '.1.3.6.1.2.1.2.2.1.16.3'}}},
                      {'node': {'pair': {
                          'key': 'pattoo_key',
                          'value': '''\
pattoo_agent_snmpd_.1.3.6.1.2.1.2.2.1.16'''}}}]},
                  'id': 'RGF0YVBvaW50OjY=',
                  'idxDatapoint': '948474',
                  'idxAgent': '1'}}]}}}}


class TestDataPointsAgent(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method or function named __init__."""
        pass

    def test_start_cursor(self):
        """Testing method or function named start_cursor."""
        # Setup test object
        expected = 'AAYXJyYXljb25uZWN0aW9uOjA='
        tester = agent.DataPointsAgent(DATAPOINT_AGENT)
        result = tester.start_cursor()

        # Test
        self.assertEqual(result, expected)

    def test_end_cursor(self):
        """Testing method or function named end_cursor."""
        # Setup test object
        expected = 'AAYXJyYXljb25uZWN0aW9uOjM1NTQ='
        tester = agent.DataPointsAgent(DATAPOINT_AGENT)
        result = tester.end_cursor()

        # Test
        self.assertEqual(result, expected)

    def test_has_next_page(self):
        """Testing method or function named has_next_page."""
        # Setup test object
        expected = False
        tester = agent.DataPointsAgent(DATAPOINT_AGENT)
        result = tester.has_next_page()

        # Test
        self.assertEqual(result, expected)

    def test_has_previous_page(self):
        """Testing method or function named has_previous_page."""
        # Setup test object
        expected = False
        tester = agent.DataPointsAgent(DATAPOINT_AGENT)
        result = tester.has_previous_page()

        # Test
        self.assertEqual(result, expected)

    def test_datapoints(self):
        """Testing method or function named datapoints."""
        _ = agent.DataPointsAgent(DATAPOINT_AGENT)
        result = _.datapoints()

        # Test
        self.assertEqual(len(result), 1)
        datapoint = result[0]

        self.assertEqual(datapoint.id(), 'RGF0YVBvaW50OjY=')
        self.assertEqual(datapoint.agent_polled_target(), 'localhost')
        self.assertEqual(datapoint.agent_program(), 'pattoo_agent_snmpd')
        self.assertEqual(datapoint.idx_pair_xlate_group(), '1')
        self.assertEqual(
            datapoint.id_pair_xlate_group(), 'UGFpclhsYXRlR3JvdXA6MQ==')
        self.assertEqual(
            datapoint.pattoo_key(), 'pattoo_agent_snmpd_.1.3.6.1.2.1.2.2.1.16')
        self.assertEqual(
            datapoint.key_value_pairs(),
            [('pattoo_agent_snmpd_oid', '.1.3.6.1.2.1.2.2.1.16.3')])
        self.assertEqual(datapoint.idx_datapoint(), '948474')


class TestAgents(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method or function named __init__."""
        pass

    def test_start_cursor(self):
        """Testing method or function named start_cursor."""
        # Setup test object
        expected = 'YXJyYXljb25uZWN0aW9uOjA='
        tester = agent.Agents(AGENTS)
        result = tester.start_cursor()

        # Test
        self.assertEqual(result, expected)

    def test_end_cursor(self):
        """Testing method or function named end_cursor."""
        # Setup test object
        expected = 'YXJyYXljb25uZWN0aW9uOjM1NTQ='
        tester = agent.Agents(AGENTS)
        result = tester.end_cursor()

        # Test
        self.assertEqual(result, expected)

    def test_has_next_page(self):
        """Testing method or function named has_next_page."""
        # Setup test object
        expected = False
        tester = agent.Agents(AGENTS)
        result = tester.has_next_page()

        # Test
        self.assertEqual(result, expected)

    def test_has_previous_page(self):
        """Testing method or function named has_previous_page."""
        # Setup test object
        expected = False
        tester = agent.Agents(AGENTS)
        result = tester.has_previous_page()

        # Test
        self.assertEqual(result, expected)

    def test_agents(self):
        """Testing method or function named agents."""
        _ = agent.Agents(AGENTS)
        result = _.agents()

        # We should get two DataPoint objects
        self.assertEqual(len(result), 2)
        for item in result:
            self.assertIsInstance(item, agent.Agent)


class TestAgent(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    # Setup test objects
    _ = agent.Agents(AGENTS)
    tester = _.agents()
    other_tester = agent.Agent(AGENT)

    def test___init__(self):
        """Testing method or function named __init__."""
        pass

    def test_id(self):
        """Testing method or function named id."""
        # Test
        ids = ['QWdlbnQ6MQ==', 'QWdlbnQ6Mg==']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.id(), ids[index])
        self.assertEqual(
            self.other_tester.id(), 'polar_bear')

    def test_idx_agent(self):
        """Testing method or function named idx_agent."""
        # Test
        ids = ['1', '2']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.idx_agent(), ids[index])
        self.assertEqual(
            self.other_tester.idx_agent(), '7')

    def test_agent_polled_target(self):
        """Testing method or function named agent_polled_target."""
        # Test
        ids = ['localhost', 'that_host']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.agent_polled_target(), ids[index])
        self.assertEqual(
            self.other_tester.agent_polled_target(), 'teddy_bear')

    def test_agent_program(self):
        """Testing method or function named agent_program."""
        # Test
        ids = ['pattoo_agent_snmpd', 'pattoo_agent_snmp_ifmibd']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.agent_program(), ids[index])
        self.assertEqual(
            self.other_tester.agent_program(), 'koala_bear')


class TestBasicFunctions(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test_agents(self):
        """Testing method or function named agents."""
        pass

    def test_datapoints_agent(self):
        """Testing method or function named datapoints_agent."""
        pass


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
