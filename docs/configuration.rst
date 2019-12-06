Configuration
=============

After installation, you will need to create a configuration file in a directory dedicated to ``pattoo``.

Set the  Configuration Directory Location
-----------------------------------------

You must set the location of the configuration directory by using the ``PATTOO_CONFIGDIR`` environmental variable. Here is how to do this:

.. code-block:: bash

    $ export PATTOO_CONFIGDIR=/path/to/configuration/directory

``pattoo`` will read any ``.yaml`` files found in this directory for configuration parameters.

Beginners should use a single file. For the purposes of this document we will assume this file is called ``etc/config.yaml``.

Make sure that files in this directory are editable by the user that will be running ``pattoo`` daemons.

Copy the Template to Your Configuration Directory
-------------------------------------------------

Copy the template file in the ``examples/etc`` directory to the ``PATTOO_CONFIGDIR`` location.

.. code-block:: bash

    $ cp examples/etc/config.yaml.template \
      /path/to/configuration/directory/config.yaml

The next step is to edit the contents of ``config.yaml``

Edit Your Configuration
-----------------------

Take some time to read up on ``YAML`` formatted files if you are not familiar with them. A background knowledge is always helpful.

The ``config.yaml`` file created from the template will have sections that you will need to edit with custom values. Don't worry, these sections are easily identifiable as they all start with ``PATTOO_``

**NOTE:** The indentations in the YAML configuration are important. Make sure indentations line up. Dashes '-' indicate one item in a list of items (if applicable).

.. code-block:: yaml

   main:
       log_level: debug
       log_directory: PATTOO_LOG_DIRECTORY
       cache_directory: PATTOO_CACHE_DIRECTORY
       daemon_directory: PATTOO_DAEMON_DIRECTORY

   pattoo_webd:

      ip_listen_address: 127.0.0.1
      ip_bind_port: 20200

  pattoo:
      ip_address: 127.0.0.1
      ip_bind_port: 20202


Configuration Explanation
^^^^^^^^^^^^^^^^^^^^^^^^^

This table outlines the purpose of each configuration parameter.

.. list-table::
   :header-rows: 1

   * - Section
     - Config Options
     - Description
   * - ``main``
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
   * - ``pattoo_webd``
     -
     -
   * -
     - ``ip_listen_address``
     - IP address used by the ``pattoo_webd`` daemon for accepting data from remote ``pattoo`` agents. Default of '0.0.0.0' which indicates listening on all available network interfaces.
   * -
     - ``ip_bind_port``
     - TCP port of used by the ``pattoo_webd`` daemon for accepting data from remote ``pattoo`` agents. Default of 20202.
   * - ``pattoo``
     -
     -
   * -
     - ``ip_address``
     - The ``pattoo`` server's IP address used to provide data for ``pattoo-web``.
   * -
     - ``ip_bind_port``
     - The TCP port that the ``pattoo`` server is using to provide data for ``pattoo-web``.


Notes
-----

Here are some additional tips.

#. You can create a separate configuration file for each section. If you are doing this, make sure there is only one file per agent section. Keep the mandtatory configurations sections in a separate file for simplicity. Practice on a test system before doing this. *Start with a single file first to gain confidence.*
