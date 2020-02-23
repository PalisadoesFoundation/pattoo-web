#!/usr/bin/env python3
"""Install pattoo."""

# Main python libraries
import sys
import os


# Try to create a working PYTHONPATH
EXEC_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(EXEC_DIR, os.pardir))
if EXEC_DIR.endswith('/pattoo-web/setup') is True:
    sys.path.append(ROOT_DIR)
else:
    print(
        'This script is not installed in the "pattoo/bin" directory. '
        'Please fix.')
    sys.exit(2)


# Pattoo imports
from pattoo_shared import files, configuration
from pattoo_shared import log


def check():
    """Ensure PIP3 packages are installed correctly.

    Args:
        None

    Returns:
        None

    """
    # Initialize key variables
    config_directory = os.environ['PATTOO_CONFIGDIR']

    # Print Status
    print('??: Checking configuration parameters.')

    # Check config (pattoo.yaml)
    config_file = configuration.agent_config_filename('pattoo')
    config = files.read_yaml_file(config_file)

    # Check main keys
    keys = ['pattoo', 'pattoo_web_api', 'pattoo_agent_api']
    for key in keys:
        if key not in config:
            log_message = ('''\
Section "{}" not found in configuration file in directory {}. Please fix.\
'''.format(key, config_directory))
            log.log2die_safe(80007, log_message)

    # Check secondary keys
    secondaries = [
        'log_level', 'log_directory', 'cache_directory',
        'daemon_directory']
    secondary_key_check(config, 'pattoo', secondaries)
    secondaries = ['ip_address', 'ip_bind_port']
    secondary_key_check(config, 'pattoo_agent_api', secondaries)
    secondaries = ['ip_address', 'ip_bind_port']
    secondary_key_check(config, 'pattoo_web_api', secondaries)

    # Check config (pattoo_webd.yaml)
    config_file = configuration.agent_config_filename('pattoo_webd')
    config = files.read_yaml_file(config_file)

    # Check main keys
    keys = ['pattoo_webd']
    for key in keys:
        if key not in config:
            log_message = ('''\
Section "{}" not found in configuration file in directory {}. Please fix.\
'''.format(key, config_directory))
            log.log2die_safe(80020, log_message)

    # Check secondary keys
    secondaries = ['ip_listen_address', 'ip_bind_port']
    secondary_key_check(config, 'pattoo_webd', secondaries)

    # Print Status
    print('OK: Configuration parameter check passed.')


def secondary_key_check(config, primary, secondaries):
    """Check secondary keys.

    Args:
        config: Configuration dict
        primary: Primary key
        secondaries: List of secondary keys

    Returns:
        None

    """
    # Check keys
    for key in secondaries:
        if key not in config[primary]:
            log_message = ('''\
Configuration file's "{}" section does not have a "{}" sub-section. \
Please fix.'''.format(primary, key))
            log.log2die_safe(80009, log_message)


def main():
    """Setup pattoo.

    Args:
        None

    Returns:
        None

    """
    # Check configuration
    check()


if __name__ == '__main__':
    # Run setup
    main()
