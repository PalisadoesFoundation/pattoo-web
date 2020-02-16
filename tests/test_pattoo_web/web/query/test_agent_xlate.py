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
from pattoo_web.web.query import agent_xlate
from pattoo_shared import data

_LANGUAGE = data.hashstring(str(random()))

# Create a common dataset for testing
AGENTS = {'data': {'allAgentXlate': {'edges': [
    {'node': {'agentProgram': 'pattoo_agent_os_autonomousd',
              'translation': 'Pattoo Standard OS Autonomous AgentXlate',
              'id': 'QWdlbnRYbGF0ZTox',
              'language': {'code': 'en'}}},
    {'node': {'agentProgram': 'pattoo_agent_snmpd',
              'translation': 'Pattoo Standard SNMP AgentXlate',
              'id': 'QWdlbnRYbGF0ZToz',
              'language': {'code': 'en'}}}]}}}

AGENT = {'data': {'agentXlate': {
    'agentProgram': 'pattoo_agent_snmp_ifmibd',
    'translation': 'Pattoo Standard IfMIB SNMP AgentXlate',
    'id': 'QWdlbnRYbGF0ZTo0',
    'language': {'code': 'en'}}}}

AGENT2 = {'data': {'agentXlate': {
    'agentProgram': 'pattoo_agent_snmp_ifmibd',
    'translation': 'Pattoo Standard IfMIB SNMP AgentXlate',
    'id': 'QWdlbnRYbGF0ZTo0',
    'language': {'code': _LANGUAGE}}}}


class TestAgentXlates(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method or function named __init__."""
        pass

    def test_agents(self):
        """Testing method or function named agents."""
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
        """Testing method or function named __init__."""
        pass

    def test_id(self):
        """Testing method or function named id."""
        # Test
        ids = ['QWdlbnRYbGF0ZTox', 'QWdlbnRYbGF0ZToz']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.id(), ids[index])
        self.assertEqual(
            self.other_tester.id(), 'QWdlbnRYbGF0ZTo0')

    def test_language_code(self):
        """Testing method or function named language_code."""
        # Test
        ids = ['en', 'en']
        for index, item in enumerate(self.tester):
            self.assertEqual(item.language_code(), ids[index])
        self.assertEqual(
            self.other_tester.language_code(), 'en')
        self.assertEqual(
            self.other_tester2.language_code(), _LANGUAGE)

    def test_translation(self):
        """Testing method or function named translation."""
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
        """Testing method or function named translations."""
        pass

    def test_translation(self):
        """Testing method or function named translation."""
        pass


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
