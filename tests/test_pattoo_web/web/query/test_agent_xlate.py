#!/usr/bin/env python3
"""Test pattoo configuration."""

import os
import unittest
import sys
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
from pattoo_web.web.query import agent_xlate
from pattoo_shared import data

_LANGUAGE = data.hashstring(str(random()))

# Create a common dataset for testing
AGENTS = {'data': {'allAgentXlate': {'edges': [
    {'node': {'agentProgram': 'pattoo_agent_os_autonomousd',
              'description': 'Pattoo Standard OS Autonomous AgentXlate',
              'id': 'QWdlbnRYbGF0ZTox',
              'language': {'code': 'en'}}},
    {'node': {'agentProgram': 'pattoo_agent_snmpd',
              'description': 'Pattoo Standard SNMP AgentXlate',
              'id': 'QWdlbnRYbGF0ZToz',
              'language': {'code': 'en'}}}]}}}

AGENT = {'data': {'agentXlate': {
    'agentProgram': 'pattoo_agent_snmp_ifmibd',
    'description': 'Pattoo Standard IfMIB SNMP AgentXlate',
    'id': 'QWdlbnRYbGF0ZTo0',
    'language': {'code': 'en'}}}}

AGENT2 = {'data': {'agentXlate': {
    'agentProgram': 'pattoo_agent_snmp_ifmibd',
    'description': 'Pattoo Standard IfMIB SNMP AgentXlate',
    'id': 'QWdlbnRYbGF0ZTo0',
    'language': {'code': _LANGUAGE}}}}


class TestAgentXlates(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method / function __init__."""
        pass

    def test_agents(self):
        """Testing method / function agents."""
        _ = agent_xlate.AgentXlates(AGENTS)
        result = _.agents()

        # We should get two DataPoint objects
        self.assertEqual(len(result), 2)
        for item in result:
            self.assertIsInstance(item, agent_xlate.AgentXlate)


class TestAgentXlate(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    # Setup test objects
    _ = agent_xlate.AgentXlates(AGENTS)
    tester = _.agents()
    other_tester = agent_xlate.AgentXlate(AGENT)
    other_tester2 = agent_xlate.AgentXlate(AGENT2)

    def test___init__(self):
        """Testing method / function __init__."""
        pass

    def test_id(self):
        """Testing method / function id."""
        # Test
        ids = ['QWdlbnRYbGF0ZTox', 'QWdlbnRYbGF0ZToz']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.id(), ids[index])
        self.assertEqual(
            self.other_tester.id(), 'QWdlbnRYbGF0ZTo0')

    def test_language_code(self):
        """Testing method / function language_code_xlate."""
        # Test
        ids = ['en', 'en']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.language_code(), ids[index])
        self.assertEqual(
            self.other_tester.language_code(), 'en')

    def test_translation(self):
        """Testing method / function translation."""
        # Test
        ids = [
            {'pattoo_agent_os_autonomousd': 'Pattoo Standard OS Autonomous AgentXlate'},
            {'pattoo_agent_snmpd': 'Pattoo Standard SNMP AgentXlate'}]
        for index, item in enumerate(self.tester):
            self.assertEqual(item.translation(), ids[index])
        self.assertEqual(
            self.other_tester.translation(), {'pattoo_agent_snmp_ifmibd': 'Pattoo Standard IfMIB SNMP AgentXlate'})
        self.assertEqual(
            self.other_tester2.translation(), {})


class TestBasicFunctions(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test_translations(self):
        """Testing method / function agents."""
        pass

    def test_translation(self):
        """Testing method / function datapoints_agent_xlate."""
        pass


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
