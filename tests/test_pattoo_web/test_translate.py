#!/usr/bin/env python3
"""Test pattoo configuration."""

import os
import unittest
import sys
from random import random

# Try to create a working PYTHONPATH
EXEC_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(
    os.path.abspath(os.path.join(EXEC_DIR, os.pardir)), os.pardir))
_EXPECTED = '{0}pattoo-web{0}tests{0}test_pattoo_web'.format(os.sep)
if EXEC_DIR.endswith(_EXPECTED) is True:
    # We need to prepend the path in case the repo has been installed
    # elsewhere on the system using PIP. This could corrupt expected results
    sys.path.insert(0, ROOT_DIR)
else:
    print('''This script is not installed in the "{0}" directory. Please fix.\
'''.format(_EXPECTED))
    sys.exit(2)

from tests.libraries.configuration import UnittestConfig
from pattoo_web.translate import AgentPair, KeyPair, datapoint_translations
from pattoo_web.web.query.agent_xlate import AgentXlates
from pattoo_web.web.query.pair_xlate import PairXlates
from pattoo_web.constants import Translation
from pattoo_web.web.query import datapoint as lib_datapoint


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

PAIRS = {'data': {'allPairXlateGroup': {'edges': [
    {'node': {'id': 'UGFpclhsYXRlR3JvdXA6MQ==',
              'idxPairXlateGroup': '1',
              'pairXlatePairXlateGroup': {'edges': []}}},
    {'node': {'id': 'UGFpclhsYXRlR3JvdXA6Mg==',
              'idxPairXlateGroup': '2',
              'pairXlatePairXlateGroup': {'edges': [
                  {'node': {
                      'translation': (
                          'Interface Broadcast Packets (HC inbound)'),
                      'key': 'pattoo_agent_snmpd_.1.3.6.1.2.1.31.1.1.1.9',
                      'units': 'teddy_bear',
                      'language': {'code': 'en'}}},
                  {'node': {
                      'translation': (
                          'Interface Multicast Packets (HC inbound)'),
                      'key': 'pattoo_agent_snmpd_.1.3.6.1.2.1.31.1.1.1.8',
                      'units': 'koala_bear',
                      'language': {'code': 'en'}}}]}}},
    {'node': {'id': 'UGFpclhsYXRlR3JvdXA6NA==',
              'idxPairXlateGroup': '4',
              'pairXlatePairXlateGroup': {'edges': [
                  {'node': {
                      'translation': 'Supply Air Temperature (F)',
                      'key': 'pattoo_agent_modbustcpd_input_register_30486',
                      'units': 'grizzly_bear',
                      'language': {'code': 'en'}}},
                  {'node': {
                      'translation': 'Return Air Temperature (F)',
                      'key': 'pattoo_agent_modbustcpd_input_register_30488',
                      'language': {'code': 'en'}}}]}}}]}}}

DATAPOINT = {'data': {'datapoint': {
    'agent': {'pairXlateGroup': {
        'id': 'UGFpclhsYXRlR3JvdXA6MQ=='},
              'agentPolledTarget': 'this_pc',
              'idxPairXlateGroup': '2',
              'agentProgram': 'pattoo_test_snmpd'},
    'glueDatapoint': {'edges': [
        {'node': {'pair': {'key': 'pattoo_agent_snmpd_oid',
                           'value': '.1.3.6.1.2.1.2.2.1.10.345'}}},
        {'node': {'pair': {
            'key': 'pattoo_key',
            'value': 'pattoo_agent_snmpd_.1.3.6.1.2.1.31.1.1.1.8'}}}]},
    'id': 'RGF0YVBvaW50OjM=',
    'idxDatapoint': '3'}}}


class TestKeyPair(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method or function named __init__."""
        pass

    def test_key(self):
        """Testing method or function named key."""
        # Test with values that have translations from the pattoo server
        translator = KeyPair(PairXlates(PAIRS).datapoints())
        for item in PAIRS['data']['allPairXlateGroup']['edges']:
            ipxg = item['node'].get('idxPairXlateGroup')
            for next_item in item['node']['pairXlatePairXlateGroup']['edges']:
                key = next_item['node'].get('key')
                _translation = next_item['node'].get('translation')
                _units = next_item['node'].get('units')
                self.assertEqual(
                    translator.key(key, ipxg),
                    Translation(text=_translation, units=_units))

        # Test with values that have no translations
        for key in [
                str(random()), str(random()), str(random()), str(random())]:
            result = translator.key(key, ipxg)
            self.assertEqual(result, Translation(text=key, units=''))


class TestAgentPair(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test___init__(self):
        """Testing method or function named __init__."""
        pass

    def test_agent_program(self):
        """Testing method or function named agent_program."""
        translator = AgentPair(AgentXlates(AGENTS).agents())
        for item in AGENTS['data']['allAgentXlate']['edges']:
            agent_program = item['node'].get('agentProgram')
            expected = item['node'].get('translation')
            self.assertEqual(translator.agent_program(agent_program), expected)


class TestBasicFunctions(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test_datapoint_translations(self):
        """Testing method or function named datapoint_translations."""
        _dp = lib_datapoint.DataPoint(DATAPOINT)
        translator = KeyPair(PairXlates(PAIRS).datapoints())
        result = datapoint_translations(_dp, translator)
        self.assertEqual(result.datapoint, _dp)
        self.assertEqual(
            result.pattoo_key_translation,
            Translation(
                text='Interface Multicast Packets (HC inbound)',
                units='koala_bear'))
        self.assertEqual(
            result.metadata_translations,
            [(Translation(text='pattoo_agent_snmpd_oid', units=''),
              '.1.3.6.1.2.1.2.2.1.10.345')])


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
