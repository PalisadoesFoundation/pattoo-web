#!/usr/bin/env python3
"""Test pattoo configuration."""

import os
import unittest
import sys
from pprint import pprint

# Try to create a working PYTHONPATH
EXEC_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(
    os.path.abspath(os.path.join(EXEC_DIR, os.pardir)), os.pardir))
if EXEC_DIR.endswith(
        '/pattoo-web/tests/test_pattoo_web') is True:
    # We need to prepend the path in case PattooShared has been installed
    # elsewhere on the system using PIP. This could corrupt expected results
    sys.path.insert(0, ROOT_DIR)
else:
    print('''\
This script is not installed in the "pattoo-web/tests/test_pattoo_web" directory. Please fix.''')
    sys.exit(2)

from tests.libraries.configuration import UnittestConfig
from pattoo_web.translate import AgentPair, KeyPair
from pattoo_web.web.query.agent_xlate import AgentXlates
from pattoo_web.web.query.pair_xlate import PairXlates


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

PAIRS = {'data': {'allPairXlateGroup': {'edges': [
    {'node': {'id': 'UGFpclhsYXRlR3JvdXA6MQ==',
              'idxPairXlateGroup': '1',
              'pairXlatePairXlateGroup': {'edges': []}}},
    {'node': {'id': 'UGFpclhsYXRlR3JvdXA6Mg==',
              'idxPairXlateGroup': '2',
              'pairXlatePairXlateGroup': {'edges': [
                  {'node': {
                      'description': (
                          'Interface Broadcast Packets (HC inbound)'),
                      'key': 'pattoo_agent_snmpd_.1.3.6.1.2.1.31.1.1.1.9',
                      'language': {'code': 'en'}}},
                  {'node': {
                      'description': (
                          'Interface Multicast Packets (HC inbound)'),
                      'key': 'pattoo_agent_snmpd_.1.3.6.1.2.1.31.1.1.1.8',
                      'language': {'code': 'en'}}}]}}},
    {'node': {'id': 'UGFpclhsYXRlR3JvdXA6NA==',
              'idxPairXlateGroup': '4',
              'pairXlatePairXlateGroup': {'edges': [
                  {'node': {
                      'description': 'Supply Air Temperature (F)',
                      'key': 'pattoo_agent_modbustcpd_input_register_30486',
                      'language': {'code': 'en'}}},
                  {'node': {
                      'description': 'Return Air Temperature (F)',
                      'key': 'pattoo_agent_modbustcpd_input_register_30488',
                      'language': {'code': 'en'}}}]}}}]}}}


class TestKeyPair(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method / function __init__."""
        pass

    def test_key(self):
        """Testing method / function key."""
        translator = KeyPair(PairXlates(PAIRS).datapoints())
        for item in PAIRS['data']['allPairXlateGroup']['edges']:
            ipxg = item['node'].get('idxPairXlateGroup')
            for next_item in item['node']['pairXlatePairXlateGroup']['edges']:
                key = next_item['node'].get('key')
                expected = next_item['node'].get('description')
                self.assertEqual(translator.key(key, ipxg), expected)


class TestAgentPair(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method / function __init__."""
        pass

    def test_agent_program(self):
        """Testing method / function agent_program."""
        translator = AgentPair(AgentXlates(AGENTS).agents())
        for item in AGENTS['data']['allAgentXlate']['edges']:
            agent_program = item['node'].get('agentProgram')
            expected = item['node'].get('description')
            self.assertEqual(translator.agent_program(agent_program), expected)


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
