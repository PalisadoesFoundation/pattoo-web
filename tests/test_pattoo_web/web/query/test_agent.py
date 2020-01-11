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

if EXEC_DIR.endswith(
        '/pattoo-web/tests/test_pattoo_web/web/query') is True:
    # We need to prepend the path in case PattooShared has been installed
    # elsewhere on the system using PIP. This could corrupt expected results
    sys.path.insert(0, ROOT_DIR)
else:
    print('''\
This script is not installed in the "pattoo-web/tests/test_pattoo_web\
/web/query" directory. Please fix.''')
    sys.exit(2)

from tests.libraries.configuration import UnittestConfig
from pattoo_web.web.query import agent


# Create a common dataset for testing
AGENTS = {'data': {'allAgent': {'edges': [
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


class TestDataPointsAgent(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method / function __init__."""
        pass

    def test_datapoints(self):
        """Testing method / function datapoints."""
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
        """Testing method / function __init__."""
        pass

    def test_agents(self):
        """Testing method / function agents."""
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
        """Testing method / function __init__."""
        pass

    def test_id(self):
        """Testing method / function id."""
        # Test
        ids = ['QWdlbnQ6MQ==', 'QWdlbnQ6Mg==']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.id(), ids[index])
        self.assertEqual(
            self.other_tester.id(), 'polar_bear')

    def test_idx_agent(self):
        """Testing method / function idx_agent."""
        # Test
        ids = ['1', '2']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.idx_agent(), ids[index])
        self.assertEqual(
            self.other_tester.idx_agent(), '7')

    def test_agent_polled_target(self):
        """Testing method / function agent_polled_target."""
        # Test
        ids = ['localhost', 'that_host']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.agent_polled_target(), ids[index])
        self.assertEqual(
            self.other_tester.agent_polled_target(), 'teddy_bear')

    def test_agent_program(self):
        """Testing method / function agent_program."""
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
        """Testing method / function agents."""
        pass

    def test_datapoints_agent(self):
        """Testing method / function datapoints_agent."""
        pass


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
