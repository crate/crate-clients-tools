=========================
CrateDB Clients and Tools
=========================

Clients and tools for working with `CrateDB`_.


Contributing
============

This project is primarily maintained by `Crate.io`_, but we welcome community
contributions!

See the `developer docs`_ and the `contribution docs`_ for more information.


Tool Power User
===============

At Crate.io we are defining so called Power Users to ensure the integrations keep working.

Responsiblities of Power Users:

* Keep track of releases, updates and developments of the tools.
* Test integration after minor and mayor CrateDB releases.
* Test integration after tool releases.
* Have a working setup available including a quick demo.
* Being able to answer questions for the specific tool.
* Ensuring guides are up to date.


Power Users
-----------



+-----------------+-------------------+---------+-----------------+------------------------------------------------------+
| Tool            | User              | Version | CrateDB Version |                                                      |
+=================+===================+=========+=================+======================================================+
| Grafana         | `proddata`_       | *X.Y*   | *X.Y.Z*         | `Known Issues Grafana`_                              |
+-----------------+-------------------+---------+-----------------+------------------------------------------------------+
| PowerBI         | `WolfgangHerbst`_ | *X.Y*   | *X.Y.Z*         | `Known Issues PowerBI`_                              |
+-----------------+-------------------+---------+-----------------+------------------------------------------------------+
| Tableau         | `marregui`_       | *X.Y*   | *X.Y.Z*         | `Known Issues Tableau`_                              |
+-----------------+-------------------+---------+-----------------+------------------------------------------------------+
| Zeppelin        |                   |         |                 |                                                      |
+-----------------+-------------------+---------+-----------------+------------------------------------------------------+
| Looker          | `proddata`_       | *X.Y*   | *X.Y.Z*         | `Known Issues Looker`_                               |
+-----------------+-------------------+---------+-----------------+------------------------------------------------------+
| Node-Red        | `proddata`_       | *X.Y*   | *X.Y.Z*         | `Known Issues Node Red`_                             |
+-----------------+-------------------+---------+-----------------+------------------------------------------------------+
| NiFi            | `proddata`_       | *X.Y*   | *X.Y.Z*         | `Known Issues NiFi`_                                 |
+-----------------+-------------------+---------+-----------------+------------------------------------------------------+
| Telegraf        |                   |         |                 |                                                      |
+-----------------+-------------------+---------+-----------------+------------------------------------------------------+
| Prometheus      | `infoverload`_    | *X.Y*   | *X.Y.Z*         | `Known Issues Prometheus`_, `Known Issues Adapter`_  |
+-----------------+-------------------+---------+-----------------+------------------------------------------------------+
| R               | `autophagy`_      | *X.Y*   | *X.Y.Z*         | `Known Issues R`_                                    |
+-----------------+-------------------+---------+-----------------+------------------------------------------------------+
| Azure Functions | `autophagy`_      | *X.Y*   | *X.Y.Z*         | `Known Issues Azure Functions`_                      |
+-----------------+-------------------+---------+-----------------+------------------------------------------------------+

.. _proddata: https://github.com/proddata
.. _WolfgangHerbst: https://github.com/WolfgangHerbst
.. _marregui: https://github.com/marregui
.. _infoverload: https://github.com/infoverload
.. _autophagy: https://github.com/autophagy


.. _Known Issues Grafana: https://github.com/crate/crate/labels/tool%3A%20Grafana
.. _Known Issues PowerBI: https://github.com/crate/crate/labels/tool%3A%20PowerBI
.. _Known Issues Tableau: https://github.com/crate/crate/labels/tool%3A%20Tableau
.. _Known Issues Looker: https://github.com/crate/crate/labels/tool%3A%20Looker
.. _Known Issues Node Red: https://github.com/crate/crate/labels/tool%3A%20Node-Red
.. _Known Issues NiFi: https://github.com/crate/crate/labels/tool%3A%20NiFi
.. _Known Issues R: https://github.com/crate/crate/labels/tool%3A%20R
.. _Known Issues Azure Functions: https://github.com/crate/crate/labels/tool%3A%20Azure%20Functions
.. _Known Issues Prometheus: https://github.com/crate/crate/labels/tool%3A%20Prometheus
.. _Known Issues Adapter: https://github.com/crate/crate_adapter/issues

Help
====

Looking for more help?

- Read the `live docs`_
- Check out our `support channels`_


.. _contribution docs: CONTRIBUTING.rst
.. _Crate.io: http://crate.io/
.. _CrateDB: https://crate.io/products/cratedb/
.. _developer docs: DEVELOP.rst
.. _live docs: https://crate.io/docs/crate/clients-tools/en/latest/
.. _support channels: https://crate.io/support/
