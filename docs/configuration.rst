Configuration
=============

After installation, you will need to create a configuration file in a directory dedicated to ``pattoo``.

Set the  Configuration Directory Location
-----------------------------------------

You must set the location of the configuration directory by using the ``PATTOO_CONFIGDIR`` environmental variable. Here is how to do this:

.. code-block:: bash

    $ export PATTOO_CONFIGDIR=/path/to/configuration/directory

Make sure that files in this directory are readable by the user that will be running ``pattoo`` daemons or scripts.

Copy the Templates to Your Configuration Directory
--------------------------------------------------

Copy the template files in the ``examples/etc`` directory to the ``PATTOO_CONFIGDIR`` location.

**NOTE:** If a ``/path/to/configuration/directory/pattoo_web.yaml`` or ``/path/to/configuration/directory/pattoo.yaml`` file already exists in the directory then skip this step and edit the file according to the steps in following sections.

.. code-block:: bash

        $ cp examples/etc/pattoo_web.yaml.template \
            /path/to/configuration/directory/pattoo_web.yaml

        $ cp examples/etc/pattoo.yaml.template \
            /path/to/configuration/directory/pattoo.yaml

The next step is to edit the contents of both files.

Edit Your Configuration Files
-----------------------------

The ``pattoo`` server uses two configuration files:

#. ``pattoo.yaml``: Provides general configuration information for all ``pattoo`` related applications. ``pattoo.yaml`` also defines how ``pattoo`` agents should connect to the ``pattoo`` server APIs.
#. ``pattoo_webd.yaml``: Provides configuration details for all the ``pattoo-web`` server's API daemons.

Take some time to read up on ``YAML`` formatted files if you are not familiar with them. A background knowledge is always helpful.

Edit Your ``pattoo`` Communication Configuration
................................................

The ``pattoo.yaml`` file created from the template will have sections that you will need to edit with custom values. Don't worry, these sections are easily identifiable as they all start with ``PATTOO_``

**NOTE:** The indentations in the YAML configuration are important. Make sure indentations line up. Dashes '-' indicate one item in a list of items (if applicable).

.. code-block:: yaml

   pattoo:

       log_level: debug
       log_directory: PATTOO_LOG_DIRECTORY
       cache_directory: PATTOO_CACHE_DIRECTORY
       daemon_directory: PATTOO_DAEMON_DIRECTORY
       language: en

   pattoo_web_api:

      ip_address: 0.0.0.0
      ip_bind_port: 20200



``pattoo`` Communication Configuration Explanation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This table outlines the purpose of each configuration parameter.

.. list-table::
   :header-rows: 1

   * - Section
     - Config Options
     - Description
   * - ``pattoo``
     -
     -
   * -
     - ``log_directory``
     - Path to logging directory. Make sure the username running the daemons have RW access to files there.
   * -
     - ``log_level``
     - Default level of logging. ``debug`` is best for troubleshooting.
   * -
     - ``cache_directory``
     - Directory that will temporarily store data data from agents prior to be added to the ``pattoo`` database.
   * -
     - ``daemon_directory``
     - Directory used to store daemon related data that needs to be maintained between reboots
   * -
     - ``language``
     - Language spoken by the human users of ``pattoo``. Defaults to ``en`` (English)
   * - ``pattoo_web_api``
     -
     -
   * -
     - ``ip_address``
     - IP address of the ``pattoo`` server to which the ``pattoo_webd`` daemon will use to transmit and receive data.
   * -
     - ``ip_bind_port``
     - TCP port of used by the ``pattoo`` server for this purpose


Edit Your Web Configuration
..............................

The ``pattoo_webd.yaml`` file created from the template will have sections that you will need to edit with custom values. Don't worry, these sections are easily identifiable as they all start with ``PATTOO_``

**NOTE:** The indentations in the YAML configuration are important. Make sure indentations line up. Dashes '-' indicate one item in a list of items (if applicable).

.. code-block:: yaml

   pattoo_webd:

      ip_listen_address: 0.0.0.0
      ip_bind_port: 20200

Web Configuration Explanation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This table outlines the purpose of each configuration parameter.

.. list-table::
   :header-rows: 1

   * - Section
     - Config Options
     - Description
   * - ``pattoo_webd``
     -
     -
   * -
     - ``ip_listen_address``
     - IP address used by the ``pattoo_webd`` daemon for accepting data from web browser users. Default of '0.0.0.0' which indicates listening on all available network interfaces. You can also use IPv6 nomenclature such as ``::``. The ``pattoo`` APIs don't support IPv6 and IPv4 at the same time.
   * -
     - ``ip_bind_port``
     - TCP port of used by the ``pattoo_webd`` daemon for accepting data from remote ``pattoo`` agents. Default of 20202.
