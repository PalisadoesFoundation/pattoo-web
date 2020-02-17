
Basic Installation
==================

This section covers some key steps to get you started.

Prerequisites
-------------

There are some software components that need to be installed prior to starting.

#. ``pattoo`` only runs on Python 3.6 or higher

Let's install the software.

Installation
------------

Follow these steps.

#. Make sure you have a fully configured ```pattoo``` server as this is a ``pattoo-web`` pre-requisite.

Follow these steps.

#. Install ``git`` on your system.
#. Select and create the parent directory in which you want to install ``pattoo-web``.

    .. code-block:: bash

       $ mkdir -p /installation/parent/directory
       $ cd /installation/parent/directory

#. Clone the repository to the parent directory using the ``git clone`` command. You can also choose to downloading and unzip the file in the parent directory. The repository can be found at: https://github.com/PalisadoesFoundation/pattoo-web

    .. code-block:: bash

       $ cd /installation/parent/directory
       $ git clone https://github.com/PalisadoesFoundation/pattoo-web.git

#. Enter the ``/installation/parent/directory/pattoo-web`` directory with the ``pattoo-web`` files.
#. Install the required packages using the ``pip_requirements`` document in the ``pattoo-web`` root directory

   .. code-block:: bash

      $ pip3 install -r pip_requirements.txt

#. Use the :doc:`configuration` to create a working configuration.
#. Run the installation script

   .. code-block:: bash

      $ sudo setup/install.py

#. Start the ``bin/pattoo_webd.py`` daemon to accept data sent by ``pattoo-agents``. :doc:`configuration`


Configuring systemd Daemons
---------------------------

You can also setup all the ``pattoo-web`` daemons as system daemons by executing the ``setup/systemd/bin/install_systemd.py`` script.

The script requires you to specify the following parameters. Make sure you have a username and group created for running your ``pattoo-web`` services.

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

   pattoo_webd.service

   $

Testing
-------

You can test whether your ``pattoo-web`` site is operational by visiting http://pattoo.example.com:20200/pattoo where you substitute ``pattoo.example.com`` with the IP address or hostname of your server.

Use the :doc:`troubleshooting` for further steps to take if you have difficulties.
