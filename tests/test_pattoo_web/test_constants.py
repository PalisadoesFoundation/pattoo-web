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
from pattoo_web.constants import PATTOO_WEBD_NAME
from pattoo_web.constants import PATTOO_WEBD_PROXY
from pattoo_web.constants import FOLDER_WEB_STATIC
from pattoo_web.constants import FOLDER_WEB_TEMPLATE
from pattoo_web.constants import SECONDS_IN_DAY
from pattoo_web.constants import SECONDS_IN_WEEK
from pattoo_web.constants import SECONDS_IN_MONTH
from pattoo_web.constants import SECONDS_IN_QUARTER
from pattoo_web.constants import SECONDS_IN_YEAR
from pattoo_web.constants import DEFAULT_CHART_SIZE_SECONDS
from pattoo_web.constants import Translation
from pattoo_web.constants import DataPointTranslations
from pattoo_web.constants import PageInfo


class TestBasicFunctions(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    def test_all(self):
        """Testing method or function named __init__."""
        # Test
        self.assertEqual(PATTOO_WEBD_NAME, 'pattoo_webd')
        self.assertEqual(PATTOO_WEBD_PROXY, 'pattoo_webd-gunicorn')
        self.assertEqual(FOLDER_WEB_STATIC, 'theme/static')
        self.assertEqual(FOLDER_WEB_TEMPLATE, 'theme/templates')
        self.assertEqual(SECONDS_IN_DAY, 86400)
        self.assertEqual(SECONDS_IN_WEEK, 604800)
        self.assertEqual(SECONDS_IN_MONTH, 2592000)
        self.assertEqual(SECONDS_IN_QUARTER, 7776000)
        self.assertEqual(SECONDS_IN_YEAR, 31536000)
        self.assertEqual(DEFAULT_CHART_SIZE_SECONDS, 86400)

        # Assign namedtuple without errors
        _ = Translation(
            text='',
            units=''
        )
        _ = DataPointTranslations(
            datapoint='',
            metadata_translations='',
            pattoo_key_translation=''
        )
        _ = PageInfo(
            endCursor='',
            hasNextPage='',
            hasPreviousPage='',
            startCursor=''
        )


if __name__ == '__main__':
    # Make sure the environment is OK to run unittests
    UnittestConfig().create()

    # Do the unit test
    unittest.main()
