#!/usr/bin/env python3
"""Test pattoo configuration."""

import os
import unittest
import sys
import time
from random import random

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
This script is not installed in the "pattoo-web/tests/test_pattoo_web/web/query" \
directory. Please fix.''')
    sys.exit(2)

from tests.libraries.configuration import UnittestConfig
from pattoo_web.web.query import datapoint


# Create a common dataset for testing
DATA = {
    'data': {'allDatapoints': {'edges': [
        {'node': {'agent': {'agentGroup': {'pairXlateGroup': {'idxPairXlateGroup': '1'}},
                            'agentPolledTarget': 'localhost',
                            'agentProgram': 'pattoo_agent_snmpd'},
                  'glueDatapoint': {'edges': [
                      {'node': {'pair': {'key': 'pattoo_agent_snmpd_oid',
                                         'value': '.1.3.6.1.2.1.2.2.1.10.1'}}},
                      {'node': {'pair': {'key': 'pattoo_key',
                                         'value': 'pattoo_agent_snmpd_.1.3.6.1.2.1.2.2.1.10'}}}]},
                  'id': 'RGF0YVBvaW50OjE=',
                  'idxDatapoint': '1'}},
        {'node': {'agent': {'agentGroup': {'pairXlateGroup': {'idxPairXlateGroup': '3'}},
                            'agentPolledTarget': 'myhost',
                            'agentProgram': 'pattoo_agent_test'},
                  'glueDatapoint': {'edges': [
                      {'node': {'pair': {'key': 'pattoo_agent_snmpd_oid',
                                         'value': '.1.3.6.1.2.1.2.2.1.16.3'}}},
                      {'node': {'pair': {'key': 'pattoo_key',
                                         'value': 'pattoo_agent_snmpd_.1.3.6.1.2.1.2.2.1.16'}}}]},
                  'id': 'RGF0YVBvaW50OjY=',
                  'idxDatapoint': '6'}}]}}}


class TestDataPoints(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method / function __init__."""
        # Test
        pass

    def test_datapoints(self):
        """Testing method / function datapoints."""
        # Setup test object
        tester = datapoint.DataPoints(DATA)
        result = tester.datapoints()

        # We should get two DataPoint objects
        self.assertEqual(len(result), 2)
        for item in result:
            self.assertIsInstance(item, datapoint.DataPoint)


class TestDataPoint(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    # Setup test object
    _ = datapoint.DataPoints(DATA)
    tester = _.datapoints()

    def test___init__(self):
        """Testing method / function __init__."""
        pass

    def test_id(self):
        """Testing method / function id."""
        # Test
        ids = ['RGF0YVBvaW50OjE=', 'RGF0YVBvaW50OjY=']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.id(), ids[index])

    def test_idx_datapoint(self):
        """Testing method / function idx_datapoint."""
        # Test
        expected = ['1', '6']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.idx_datapoint(), expected[index])

    def test_agent_polled_target(self):
        """Testing method / function agent_polled_target."""
        # Test
        expected = ['localhost', 'myhost']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.agent_polled_target(), expected[index])

    def test_agent_program(self):
        """Testing method / function agent_program."""
        # Test
        expected = ['pattoo_agent_snmpd', 'pattoo_agent_test']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.agent_program(), expected[index])

    def test_idx_pair_xlate_group(self):
        """Testing method / function idx_pair_xlate_group."""
        # Test
        expected = ['1', '3']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.idx_pair_xlate_group(), expected[index])

    def test_id_pair_xlate_group(self):
        """Testing method / function id_pair_xlate_group."""
        # Test
        expected = [None, None]
        for index, item in enumerate(self.tester):
            self.assertEqual(item.id_pair_xlate_group(), expected[index])

    def test_pattoo_key(self):
        """Testing method / function pattoo_key."""
        # Test
        expected = [
            'pattoo_agent_snmpd_.1.3.6.1.2.1.2.2.1.10',
            'pattoo_agent_snmpd_.1.3.6.1.2.1.2.2.1.16']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.pattoo_key(), expected[index])

    def test_key_value_pairs(self):
        """Testing method / function key_value_pairs."""
        # Test
        expected = [
            [('pattoo_agent_snmpd_oid', '.1.3.6.1.2.1.2.2.1.10.1')],
            [('pattoo_agent_snmpd_oid', '.1.3.6.1.2.1.2.2.1.16.3')]
        ]
        for index, item in enumerate(self.tester):
            self.assertEqual(item.key_value_pairs(), expected[index])

    def test__key_value_pairs(self):
        """Testing method / function _key_value_pairs."""
        pass


class TestBasicFunctions(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test_datapoints(self):
        """Testing method / function datapoints."""
        pass

    def test_datapoint(self):
        """Testing method / function datapoint."""
        pass


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
