#!/usr/bin/env python3
"""Test pattoo configuration."""

import os
import unittest
import sys
from collections import namedtuple
from copy import deepcopy

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
This script is not installed in the "pattoo-web/tests/test_pattoo_web" \
directory. Please fix.''')
    sys.exit(2)

from tests.libraries.configuration import UnittestConfig
from pattoo_shared.constants import (
    PATTOO_WEB_SITE_PREFIX, PATTOO_API_AGENT_PREFIX)
from pattoo_web import uri
from pattoo_web.constants import PageInfo


class TestBasicFunctions(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test_chart_link(self):
        """Testing method / function chart_link."""
        # Test
        result = uri.chart_link('0', '3', '4')
        self.assertEqual(result, '''\
<a href="{}/chart/datapoint/0?secondsago=4">3</a>\
'''.format(PATTOO_WEB_SITE_PREFIX))
        result = uri.chart_link('0')
        self.assertEqual(result, '''\
<a href="{}/chart/datapoint/0?secondsago=86400">Chart Data</a>\
'''.format(PATTOO_WEB_SITE_PREFIX))

    def test_agent_link(self):
        """Testing method / function agent_link."""
        # Test
        result = uri.agent_link('0', '3')
        self.assertEqual(result, '''\
<a href="{}/agent/0">3</a>'''.format(PATTOO_WEB_SITE_PREFIX))

    def test_integerize_arg(self):
        """Testing method / function integerize_arg."""
        # Test
        test_value = '30'
        result = uri.integerize_arg(test_value)
        self.assertEqual(result, int(test_value))

        # Fail for non numeric strings and booleans
        result = uri.integerize_arg('Test')
        self.assertEqual(result, None)
        result = uri.integerize_arg(None)
        self.assertEqual(result, None)
        result = uri.integerize_arg(False)
        self.assertEqual(result, None)

    def test_prev_next(self):
        """Testing method / function prev_next."""
        # Initialize key variables
        Seed = namedtuple(
            'Seed', 'script_root path args')
        args_list = [
            {'first': 100, 'last': 20},
            {'first': 100},
            {'last': 20},
            {}
        ]

        # Test (hasNextPage=False, hasNextPage=False)
        status = PageInfo(
            endCursor='',
            startCursor='',
            hasNextPage=False,
            hasPreviousPage=False
        )
        expecteds = [
            ('', ''),
            ('', ''),
            ('', ''),
            ('', '')
        ]
        for index, args in enumerate(args_list):
            request = Seed(
                script_root='abc',
                path='xyz',
                args=args
            )
            result = uri.prev_next(request, status)
            expected = expecteds[index]
            self.assertEqual(result, expected)

        # Test (hasNextPage=True, hasNextPage=False)
        status = PageInfo(
            endCursor='',
            startCursor='',
            hasNextPage=True,
            hasPreviousPage=False
        )
        expecteds = [
            ('', '<a href="abcxyz?first=120&last=20">Next &gt;</a>'),
            ('', '<a href="abcxyz?first=120&last=100">Next &gt;</a>'),
            ('', '<a href="abcxyz?first=40&last=20">Next &gt;</a>'),
            ('', '<a href="abcxyz?first=40&last=20">Next &gt;</a>')
        ]
        for index, args in enumerate(args_list):
            request = Seed(
                script_root='abc',
                path='xyz',
                args=args
            )
            result = uri.prev_next(request, status)
            expected = expecteds[index]
            self.assertEqual(result, expected)

        # Test (hasNextPage=False, hasNextPage=True)
        status = PageInfo(
            endCursor='',
            startCursor='',
            hasNextPage=False,
            hasPreviousPage=True
        )
        expecteds = [
            ('<a href="abcxyz?first=80&last=20">&lt; Prev</a>', ''),
            ('<a href="abcxyz?first=80&last=100">&lt; Prev</a>', ''),
            ('<a href="abcxyz?first=0&last=20">&lt; Prev</a>', ''),
            ('<a href="abcxyz?first=0&last=20">&lt; Prev</a>', '')
        ]
        for index, args in enumerate(args_list):
            request = Seed(
                script_root='abc',
                path='xyz',
                args=args
            )
            result = uri.prev_next(request, status)
            expected = expecteds[index]
            self.assertEqual(result, expected)

        # Test (hasNextPage=True, hasNextPage=True)
        status = PageInfo(
            endCursor='',
            startCursor='',
            hasNextPage=True,
            hasPreviousPage=True
        )
        expecteds = [
            ('<a href="abcxyz?first=80&last=20">&lt; Prev</a>',
             '<a href="abcxyz?first=120&last=20">Next &gt;</a>'),
            ('<a href="abcxyz?first=80&last=100">&lt; Prev</a>',
             '<a href="abcxyz?first=120&last=100">Next &gt;</a>'),
            ('<a href="abcxyz?first=0&last=20">&lt; Prev</a>',
             '<a href="abcxyz?first=40&last=20">Next &gt;</a>'),
            ('<a href="abcxyz?first=0&last=20">&lt; Prev</a>',
             '<a href="abcxyz?first=40&last=20">Next &gt;</a>')
        ]
        for index, args in enumerate(args_list):
            request = Seed(
                script_root='abc',
                path='xyz',
                args=args
            )
            result = uri.prev_next(request, status)
            expected = expecteds[index]
            self.assertEqual(result, expected)

    def test_graphql_filter(self):
        """Testing method / function graphql_filter."""
        # Initialize key variables
        Seed = namedtuple(
            'Seed', 'script_root path args')
        args_list = [
            {'first': 100, 'last': 20},
            {'first': 100},
            {'last': 20},
            {}
        ]

        # Test
        expecteds = [
            '(first: 100 last: 20)',
            '(first: 100 last: 20)',
            '(first: 20 last: 20)',
            '(first: 20 last: 20)'
        ]
        for index, args in enumerate(args_list):
            request = Seed(
                script_root='abc',
                path='xyz',
                args=args
            )
            result = uri.graphql_filter(request)
            expected = expecteds[index]
            self.assertEqual(result, expected)


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
