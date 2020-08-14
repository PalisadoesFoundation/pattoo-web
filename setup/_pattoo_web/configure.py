"""Configure pattoo web."""
import os
from pattoo_shared.installation import configure, shared
from pattoo_shared import files


def install(pattoo_home):
    """Start configuration process.

    Args:
        None

    Returns:
        None

    """
    # Initialize key variables
    if os.environ.get('PATTOO_CONFIGDIR') is None:
        os.environ['PATTOO_CONFIGDIR'] = '{0}etc{0}pattoo'.format(os.sep)
    config_dir = os.environ.get('PATTOO_CONFIGDIR')

    pattoo_webd_dict = {
        'pattoo_webd': {
            'ip_listen_address': '0.0.0.0',
            'ip_bind_port': 20200,
        },
        'pattoo_web_api': {
            'ip_address': '::1',
            'ip_bind_port': 20202
        },
    }

    # Attempt to create configuration directory
    files.mkdir(config_dir)

    # Create the pattoo user and group
    configure.create_user('pattoo', pattoo_home, ' /bin/false', True)

    # Attempt to change the ownership of the config and pattoo-home directories
    shared.chown(config_dir)
    shared.chown(pattoo_home)

    # Configure pattoo web
    configure.configure_component('pattoo_webd', config_dir, pattoo_webd_dict)

    # Done
