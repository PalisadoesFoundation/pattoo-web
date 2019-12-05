
Basic Installation
==================

This section covers some key steps to get you started.

Installation
------------

Follow these steps.

#. Make sure you have a fully configured ``pattoo`` server as this is a ``pattoo-web`` pre-requisite.
#. Install `git` on your system.
#. Select the parent directory in which you want to install `pattoo`
#. Clone the repository to the parent directory using the `git clone` command. You can also choose to download and unzip the file in the parent directory. The repository can be found at: https://github.com/PalisadoesFoundation/pattoo
#. Enter the directory with the `pattoo` files.
#. Install the required packages using the ``pip_requirements`` document in the `pattoo` root directory
#. Run the installation script

   .. code-block:: bash

      $ sudo setup/install.py

#. Start the ``bin/pattoo-webd.py`` daemon to accept data sent by `pattoo` agents. :doc:`configuration`


Configuring Agents as systemd Daemons
-------------------------------------

You can also setup all the ``patoo`` daemons as system daemons by executing the ``setup/systemd/bin/install_systemd.py`` script.

The script requires you to specify the following parameters. Make sure you have a username and group created for running your ``patoo`` services.

.. code-block:: bash

    usage: install_systemd.py [-h] -f CONFIG_DIR -i INSTALLATION_DIR -u USERNAME
                              -g GROUP

    optional arguments:
      -h, --help            show this help message and exit
      -f CONFIG_DIR, --config_dir CONFIG_DIR
                            Directory where the pattoo configuration files will be
                            located
      -i INSTALLATION_DIR, --installation_dir INSTALLATION_DIR
                            Directory where the pattoo is installed. (Must end
                            with '/pattoo')
      -u USERNAME, --username USERNAME
                            Username that will run the daemon
      -g GROUP, --group GROUP
                            User group to which username belongs

**Note** The daemons are not enabled or started by default. You will have to do this separately using the ``systemctl`` command after running the script.


.. code-block:: bash

   $ sudo setup/systemd/bin/install_systemd.py --config_dir=~/GitHub/pattoo/etc --user pattoo --group pattoo --install ~/GitHub/pattoo

   SUCCESS! You are now able to start/stop and enable/disable the following systemd services:

   pattoo-webd.service

   $
