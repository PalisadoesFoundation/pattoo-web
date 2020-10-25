#!/usr/bin/env python3
"""Pattoo classes that manage various configurations."""

# Import project libraries
from pattoo_shared import files
from pattoo_shared.configuration import search, agent_config_filename
from pattoo_shared.configuration import BaseConfig
from pattoo_web.constants import PATTOO_WEBD_NAME
from pattoo_shared import url
from pattoo_shared.constants import PATTOO_API_WEB_PREFIX


class Config(BaseConfig):
    """Class gathers all configuration information.

    Only processes the following YAML keys in the configuration file:

        The value of the PATTOO_WEBD_NAME constant

    """

    def __init__(self):
        """Initialize the class.

        Args:
            None

        Returns:
            None

        """
        # Instantiate inheritance
        BaseConfig.__init__(self)

        # Get the configuration directory
        config_file = agent_config_filename(PATTOO_WEBD_NAME)
        self._daemon_configuration = files.read_yaml_file(config_file)

    def ip_listen_address(self):
        """Get ip_listen_address.

        Args:
            None

        Returns:
            result: result

        """
        # Get result
        key = PATTOO_WEBD_NAME
        sub_key = 'ip_listen_address'
        result = search(key, sub_key, self._daemon_configuration, die=False)

        # Default to 0.0.0.0
        if result is None:
            result = '0.0.0.0'
        return result

    def ip_bind_port(self):
        """Get ip_bind_port.

        Args:
            None

        Returns:
            result: result

        """
        # Initialize key variables
        key = PATTOO_WEBD_NAME
        sub_key = 'ip_bind_port'

        # Get result
        intermediate = search(
            key, sub_key, self._daemon_configuration, die=False)
        if intermediate is None:
            result = 20200
        else:
            result = int(intermediate)
        return result

    def web_api_ip_address(self):
        """Get web_api_ip_address.

        Args:
            None

        Returns:
            result: result

        """
        # Initialize key variables
        key = 'pattoo_web_api'
        sub_key = 'ip_address'

        # Get result
        result = search(
            key, sub_key, self._daemon_configuration, die=True)
        return result

    def web_api_ip_bind_port(self):
        """Get web_api_ip_bind_port.

        Args:
            None

        Returns:
            result: result

        """
        # Initialize key variables
        key = 'pattoo_web_api'
        sub_key = 'ip_bind_port'

        # Get result
        intermediate = search(
            key, sub_key, self._daemon_configuration, die=False)
        if intermediate is None:
            result = 20202
        else:
            result = int(intermediate)
        return result

    def web_api_server_url(self, graphql=True):
        """Get pattoo server's remote URL.

        Args:
            agent_id: Agent ID

        Returns:
            result: URL.

        """
        # Create the suffix
        if bool(graphql) is True:
            suffix = '/graphql'
        else:
            suffix = '/rest/data'

        # Return
        _ip = url.url_ip_address(self.web_api_ip_address())
        result = (
            'http://{}:{}{}{}'.format(
                _ip,
                self.web_api_ip_bind_port(),
                PATTOO_API_WEB_PREFIX, suffix))
        return result
