===============
Developer Guide
===============


Documentation
=============

The documentation is written using `Sphinx`_ and `ReStructuredText`_.


Working on the documentation
----------------------------

Python 3.7 is required.

Change into the ``docs`` directory:

.. code-block:: console

    $ cd docs

For help, run:

.. code-block:: console

    $ make

    Crate Docs Build

    Run `make <TARGET>`, where <TARGET> is one of:

      dev     Run a Sphinx development server that builds and lints the
              documentation as you edit the source files

      html    Build the static HTML output

      check   Build, test, and lint the documentation

      reset   Reset the build cache

You must install `fswatch`_ to use the ``dev`` target.


Continuous integration and deployment
-------------------------------------

|build| |gha| |rtd|

GHA is `configured`_ to run ``make check`` from the ``docs`` directory.
Please do not merge pull requests until the tests pass.

`Read the Docs`_ automatically deploys the documentation whenever a configured
branch is updated.

To make changes to the RTD configuration (e.g., to activate or deactivate a
release version), please contact the `@crate/tech-writing`_ team.


.. _@crate/tech-writing: https://github.com/orgs/crate/teams/tech-writing
.. _configured: https://github.com/crate/crate-clients-tools/blob/main/.github/workflows/docs.yml
.. _fswatch: https://github.com/emcrisostomo/fswatch
.. _Read the Docs: https://readthedocs.org
.. _ReStructuredText: https://docutils.sourceforge.net/rst.html
.. _Sphinx: https://www.sphinx-doc.org


.. |build| image:: https://img.shields.io/endpoint.svg?color=blue&url=https%3A%2F%2Fraw.githubusercontent.com%2Fcrate%2Fcrate-clients-toolss%2Fmain%2Fdocs%2Fbuild.json
    :alt: Build version
    :target: https://github.com/crate/crate-clients-tools/blob/main/docs/build.json

.. |gha| image:: https://github.com/crate/crate-clients-tools/actions/workflows/docs.yml/badge.svg
    :alt: Travis CI status
    :scale: 100%
    :target: https://github.com/crate/crate-clients-tools/actions/workflows/docs.yml

.. |rtd| image:: https://readthedocs.org/projects/crate-clients-tools/badge/?version=latest
    :alt: Read The Docs status
    :scale: 100%
    :target: https://crate-clients-tools.readthedocs.io/en/latest/?badge=latest
