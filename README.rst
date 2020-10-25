.. image:: docs/_static/pattoo-rtd.png
   :alt: Pattoo Logo

pattoo-web
==========

``pattoo-web`` is a web GUI to view IoT data stored on ``pattoo`` servers.

Setup and Running pattoo-web
============================

`Pattoo-web` udpated to run as ReactJS application and utilizes various
third-party ReactJS modules.

.. code-block:: bash

    cd pattoo_web
    npm install
    npm start


Introduction
============

``pattoo`` stores timeseries data in a database and makes it available for users via a GraphQL API.

Data can be collected from a number of sources. The ``pattoo-agents`` repository provides a number standard data collection agents for:

* Linux
* SNMP
* Modbus TCP
* BACnet/IP
* OPC UA

``pattoo`` was originally created to assist DevOps and building facilities management teams to monitor the performance of servers, applications and electro-mechanical systems. It is flexible enough to chart a wide variety of data that changes over time by creating custom agents.

``pattoo`` currently only runs on Linux systems.

Documentation
=============

There are a number of sets of documents that cover the ``pattoo`` portfolio.

Visit the `Pattoo website <https://palisadoesfoundation.github.io/pattoo.github.io/>`_ for details about:

#. The purpose of ``pattoo``
#. The various applications that make ``pattoo`` work.
#. How to configure the ``pattoo`` applications.
#. How to create custom data collection agents.

About The Palisadoes Foundation
===============================

``pattoo`` and its supporting applications are based on the original ``infoset`` code created by the `Palisadoes Foundation <http://www.palisadoes.org>`_ as part of its annual Calico Challenge program. Calico provides paid summer internships for  Jamaican university students to work on selected open source projects. They are mentored by software professionals and receive stipends based on the completion of predefined milestones. Calico was started in 2015.
