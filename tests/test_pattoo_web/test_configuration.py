#!/usr/bin/env python3
"""Test pattoo configuration."""

import os
import unittest
import sys

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
from pattoo_web import configuration


class TestConfiguration(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    config = configuration.Config()

    def test___init__(self):
        """Testing method / function __init__."""
        pass

    def test_api_listen_address(self):
        """Testing method / function api_listen_address."""
        # Test
        result = self.config.api_listen_address()
        self.assertEqual(result, '127.0.0.1')

    def test_api_ip_bind_port(self):
        """Testing method / function api_ip_bind_port."""
        # Test
        result = self.config.api_ip_bind_port()
        self.assertEqual(result, 20200)

    def test_web_api_ip_address(self):
        """Testing method / function web_api_ip_address."""
        # Test
        result = self.config.web_api_ip_address()
        self.assertEqual(result, '127.0.0.3')

    def test_web_api_ip_bind_port(self):
        """Testing method / function web_api_ip_bind_port."""
        # Test
        result = self.config.web_api_ip_bind_port()
        self.assertEqual(result, 20202)

    def test_web_api_uses_https(self):
        """Testing method / function web_api_uses_https."""
        # Test
        result = self.config.web_api_uses_https()
        self.assertEqual(result, False)

    def test_web_api_server_url(self):
        """Testing method / function web_api_server_url."""
        # Test
        result = self.config.web_api_server_url()
        self.assertEqual(
            result, 'http://127.0.0.3:20202/pattoo/api/v1/web/graphql')


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
