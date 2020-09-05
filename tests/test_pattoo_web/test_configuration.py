#!/usr/bin/env python3
"""Test pattoo configuration."""

import os
import unittest
import sys

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
from pattoo_web import configuration


class TestConfiguration(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    config = configuration.Config()

    def test___init__(self):
        """Testing method or function named __init__."""
        pass

    def test_ip_listen_address(self):
        """Testing method or function named ip_listen_address."""
        # Test
        result = self.config.ip_listen_address()
        self.assertEqual(result, '127.0.0.1')

    def test_ip_bind_port(self):
        """Testing method or function named ip_bind_port."""
        # Test
        result = self.config.ip_bind_port()
        self.assertEqual(result, 40200)

    def test_web_api_ip_address(self):
        """Testing method or function named web_api_ip_address."""
        # Test
        result = self.config.web_api_ip_address()
        self.assertEqual(result, '127.0.0.3')

    def test_web_api_ip_bind_port(self):
        """Testing method or function named web_api_ip_bind_port."""
        # Test
        result = self.config.web_api_ip_bind_port()
        self.assertEqual(result, 30303)

    def test_web_api_server_url(self):
        """Testing method or function named web_api_server_url."""
        # Test
        result = self.config.web_api_server_url()
        self.assertEqual(
            result, 'http://127.0.0.3:30303/pattoo/api/v1/web/graphql')


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
