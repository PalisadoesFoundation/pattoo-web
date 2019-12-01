#!/usr/bin/env python3
"""Pattoo classes that manage various configurations."""

# Import project libraries
from pattoo_shared.configuration import Config as ConfigShared
from pattoo_shared.configuration import search
from pattoo_shared.constants import PATTOO_API_WEB_PREFIX
from pattoo_web.constants import PATTOO_WEBD_EXECUTABLE


class Config(ConfigShared):
    """Class gathers all configuration information.

    Only processes the following YAML keys in the configuration file:

        The value of the PATTOO_WEBD_EXECUTABLE constant

    """

    def __init__(self):
        """Initialize the class.

        Args:
            None

        Returns:
            None

        """
        # Instantiate the Config parent
        ConfigShared.__init__(self)

    def api_listen_address(self):
        """Get api_listen_address.

        Args:
            None

        Returns:
            result: result

        """
        # Get result
        key = PATTOO_WEBD_EXECUTABLE
        sub_key = 'api_listen_address'
        result = search(key, sub_key, self._configuration, die=False)

        # Default to 0.0.0.0
        if result is None:
            result = '0.0.0.0'
        return result

    def api_ip_bind_port(self):
        """Get api_ip_bind_port.

        Args:
            None

        Returns:
            result: result

        """
        # Initialize key variables
        key = PATTOO_WEBD_EXECUTABLE
        sub_key = 'api_ip_bind_port'

        # Get result
        intermediate = search(key, sub_key, self._configuration, die=False)
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
        key = PATTOO_WEBD_EXECUTABLE
        sub_key = 'web_api_ip_address'

        # Get result
        result = search(key, sub_key, self._configuration, die=True)
        return result

    def web_api_ip_bind_port(self):
        """Get web_api_ip_bind_port.

        Args:
            None

        Returns:
            result: result

        """
        # Initialize key variables
        key = PATTOO_WEBD_EXECUTABLE
        sub_key = 'web_api_ip_bind_port'

        # Get result
        intermediate = search(key, sub_key, self._configuration, die=False)
        if intermediate is None:
            result = 20202
        else:
            result = int(intermediate)
        return result

    def web_api_uses_https(self):
        """Get web_api_uses_https.

        Args:
            None

        Returns:
            result: result

        """
        # Initialize key variables
        key = PATTOO_WEBD_EXECUTABLE
        sub_key = 'web_api_uses_https'

        # Get result
        result = search(key, sub_key, self._configuration, die=False)
        if result is None:
            result = False
        return result

    def web_api_server_url(self, graphql=True):
        """Get pattoo server's remote URL.

        Args:
            agent_id: Agent ID

        Returns:
            result: URL.

        """
        # Construct URL for server
        if self.web_api_uses_https() is True:
            prefix = 'https://'
        else:
            prefix = 'http://'

        # Create the suffix
        if bool(graphql) is True:
            suffix = '/graphql'
        else:
            suffix = '/rest/data'

        # Return
        result = (
            '{}{}:{}{}{}'.format(
                prefix, self.web_api_ip_address(),
                self.web_api_ip_bind_port(), PATTOO_API_WEB_PREFIX, suffix))
        return result
