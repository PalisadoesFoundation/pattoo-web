#!/usr/bin/env python3
"""Script to install pattoo web."""
from inspect import ismethod
import textwrap
import argparse
import sys
import os
import getpass
print(sys.path)
# Set up python path
EXEC_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
ROOT_DIR = os.path.abspath(os.path.join(EXEC_DIR, os.pardir))
_EXPECTED = '{0}pattoo-web{0}setup'.format(os.sep)
DAEMON_DIRECTORY = '/opt/pattoo-daemon/.python'
if EXEC_DIR.endswith(_EXPECTED) is True:
    sys.path.append(ROOT_DIR)
    sys.path.append(DAEMON_DIRECTORY)
    # Set pattoo config dir if it had not been set already
    try:
        os.environ['PATTOO_CONFIGDIR']
    except KeyError:
        os.environ['PATTOO_CONFIGDIR'] = '/etc/pattoo'
else:
    print('''\
This script is not installed in the "{}" directory. Please fix.\
'''.format(_EXPECTED))
    sys.exit(2)

# Attempt to import pattoo shared
try:
    import pattoo_shared
except ModuleNotFoundError:
    print('Pattoo shared is missing, please run\
"python3 -m pip install PattooShared" to continue')

# Import pattoo related libraries
from pattoo_shared.installation import packages, shared, systemd
from _pattoo_web import configure


class _Parser(argparse.ArgumentParser):
    """Class gathers all CLI information."""

    def error(self, message):
        """Override the default behavior of the error method.
        Will print the help message whenever the error method is triggered.
        Args:
            None
        Returns:
            _args: Namespace() containing all of our CLI arguments as objects
                - filename: Path to the configuration file
        """
        sys.stderr.write('\nERROR: {}\n\n'.format(message))
        self.print_help()
        sys.exit(2)


class Parser():
    """Class gathers all CLI information."""

    def __init__(self, additional_help=None):
        """Intialize the class."""
        # Create a number of here-doc entries
        if additional_help is not None:
            self._help = additional_help
        else:
            self._help = ''

    def args(self):
        """Return all the CLI options.
        Args:
            None
        Returns:
            _args: Namespace() containing all of our CLI arguments as objects
                - filename: Path to the configuration file
        """
        # Initialize key variables
        width = 80

        # Header for the help menu of the application
        parser = _Parser(
            description=self._help,
            formatter_class=argparse.RawTextHelpFormatter)

        # Add subparser
        subparsers = parser.add_subparsers(dest='action')

        # Parse "install", return object used for parser
        _Install(subparsers, width=width)

        # Install help if no arguments
        if len(sys.argv) == 1:
            parser.print_help(sys.stderr)
            sys.exit(1)

        # Return the CLI arguments
        _args = parser.parse_args()

        # Return our parsed CLI arguments
        return (_args, parser)


class _Install():
    """Class gathers all CLI 'install' information."""

    def __init__(self, subparsers, width=80):
        """Intialize the class."""
        # Initialize key variables
        parser = subparsers.add_parser(
            'install',
            help=textwrap.fill('Install pattoo web.', width=width)
        )
        # Add subparser
        self.subparsers = parser.add_subparsers(dest='qualifier')

        # Execute all methods in this Class
        for name in dir(self):
            # Get all attributes of Class
            attribute = getattr(self, name)

            # Determine whether attribute is a method
            if ismethod(attribute):

                # Ignore if method name is reserved (eg. __Init__)
                if name.startswith('_'):
                    continue

                # Execute
                attribute(width=width)

    def all(self, width=80):
        """CLI command to install all pattoo components.
        Args:
            width: Width of the help text string to STDIO before wrapping
        Returns:
            None
        """
        # Initialize key variables
        parser = self.subparsers.add_parser(
            'all',
            help=textwrap.fill('Install all pattoo components', width=width)
        )

        # Add arguments
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Enable verbose mode.')

    def pip(self, width=80):
        """CLI command to install the necessary pip3 packages.
        Args:
            width: Width of the help text string to STDIO before wrapping
        Returns:
            None
        """
        # Initialize key variables
        parser = self.subparsers.add_parser(
            'pip',
            help=textwrap.fill('Install pip packages', width=width)
        )

        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Enable verbose mode.')

    def configuration(self, width=80):
        """CLI command to configure pattoo.
        Args:
            width: Width of the help text string to STDIO before wrapping
        Returns:
            None
        """
        # Initialize key variables
        _ = self.subparsers.add_parser(
            'configuration',
            help=textwrap.fill('Configure pattoo web', width=width)
        )

    def systemd(self, width=80):
        """CLI command to install and start the system daemons.

        Args:
            width: Width of the help text string to STDIO before wrapping

        Returns:
            None

        """
        # Initialize key variables
        _ = self.subparsers.add_parser(
            'systemd',
            help=textwrap.fill('Install and run system daemons', width=width)
        )


def check_user():
    """Validate conditions needed to start installation.
    Prevents installation if the script is not run as root
    Args:
        None
    Returns:
        True: If conditions for installation are satisfied
    """
    if getpass.getuser() != 'travis':
        if getpass.getuser() != 'root':
            shared.log('You are currently not running the script as root.\
Run as root to continue')
    return True


def main():
    """Pattoo CLI script.

    Args:
        None

    Returns:
        None

    """
    # Initialize key variables
    _help = 'This program is the CLI interface to configuring pattoo web'
    template_dir = os.path.join(ROOT_DIR, 'setup/systemd/system')
    daemon_list = ['pattoo_webd']

    # Ensure user is running as root or travis
    check_user()

    # Process the CLI
    _parser = Parser(additional_help=_help)
    (args, parser) = _parser.args()

    # Process CLI options
    if args.action == 'install':

        # Installs all pattoo webd agent components
        if args.qualifier == 'all':
            print('Installing everything')
            configure.install()
            packages.install(ROOT_DIR)
            systemd.install(daemon_list=daemon_list,
                            template_dir=template_dir,
                            installation_dir=ROOT_DIR)

        # Sets up configuration for agent
        elif args.qualifier == 'configuration':
            print('Installing configuration')
            configure.install()

        # Installs pip packages
        elif args.qualifier == 'pip':
            print('Installing pip packages')
            packages.install(ROOT_DIR, args.verbose)

        # Installs and runs system daemons in the daemon list
        elif args.qualifier == 'systemd':
            print('Installing and running system daemons')
            systemd.install(daemon_list=daemon_list,
                            template_dir=template_dir,
                            installation_dir=ROOT_DIR)

        else:
            parser.print_help(sys.stderr)
            sys.exit(1)

        # Done
        print('Done')


if __name__ == '__main__':
    main()
