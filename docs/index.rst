.. _index:

=========================
CrateDB Clients and Tools
=========================

CrateDB is a distributed SQL database that makes it simple to store and analyze
massive amounts of machine data in real-time.


.. seealso::

    We are also maintaining a more up-to-date list of `CrateDB integration tutorials`_.

.. TIP::

    CrateDB supports the `PostgreSQL wire protocol`_. Accordingly, many clients
    that work with PostgreSQL also work with CrateDB.

    You can try this out for yourself:

    - Configure a PostgreSQL connection, but point your client to a CrateDB
      server instead of a PostgreSQL server
    - `Authenticate`_ as the ``crate`` `superuser`_ with no password
    - Specify the ``doc`` `schema`_, if you are asked for a *database name*
    - For example, your connection string to a local database might look like
      ``postgresql://crate@localhost:5432/doc``

    Check out the `client compatibility notes`_ and `implementation
    differences`_ for information about known limitations.

    If you run into issues, please let us know using the *Feedback* section at
    the bottom of this page. We regularly update CrateDB to accomodate new
    PostgreSQL clients.


Clients
=======

Below is a selection of CrateDB client libraries.

Pick your library, and start building!

.. list-table::
    :header-rows: 1

    * - Language
      - Name
      - Maintainer
      - Official support
    * - C# (.NET)
      - `Npgsql`_
      - Community
      - ✔️ (>= CrateDB 4.2.0)
    * - C# (.NET)
      - `CrateDB Npgsql fork`_
      - Crate.IO
      - ✔️
    * - Erlang
      - `craterl`_
      - Crate.IO
      -
    * - Go
      - `pgx`_
      - Community
      - ✔️
    * - Java
      - `PostgreSQL JDBC`_
      - Community
      - ✔️  (>= CrateDB 4.2, `with known issues`_)
    * - Java
      - `crate-jdbc`_
      - Crate.IO
      - ✔️
    * - Node.JS
      - `node-postgres`_
      - Community
      - ✔️
    * - Node.JS
      - `crate-connect`_
      - Community
      -
    * - Node.JS
      - `cratejs`_
      - Community
      -
    * - Node.JS
      - `node-crate`_
      - Community
      -
    * - Perl
      - `DBD::Crate`_
      - Community
      -
    * - PHP
      - `CrateDB PDO`_
      - Crate.IO
      - ✔️
    * - PHP
      - `CrateDB DBAL`_
      - Crate.IO
      - ✔️
    * - PHP
      - `CrateDB driver for Laravel`_
      - Community
      -
    * - Python
      - `crate-python`_
      - Crate.IO
      - ✔️
    * - Python
      - `asyncpg`_
      - Community
      - ✔️
    * - Ruby
      - `crate_ruby`_
      - Crate.IO
      -
    * - Ruby
      - `activerecord-crate-adaptor`_
      - Crate.IO
      -
    * - Scala
      - `crate-scala`_
      - Community
      -
    * - Scala
      - `crate-connector`_
      - Community
      -


Tools
=====

CrateDB integrates with many different tools. Some of these are:

- **Azure Functions**

  An `Azure Function`_ is a short-lived, serverless computation that is
  triggered by external events. Learn how to `create a data enrichment
  pipeline`_ in our tutorial.

- **Grafana**

  `Grafana`_ allows you to query, visualize, alert on and understand your
  metrics and time series data. Read our tutorial on how to `pair CrateDB
  with Grafana`_.

- **Pentaho**

  `Pentaho`_ prepares and blends data, delivering business analytics from any
  source. You can connect to CrateDB clusters by using `Petaho Kettle`_ and the
  standalone version of `our JDBC driver`_.

- **R**

  `R`_  is a programming language and software environment geared towards
  statistical computing. Read our guide on how to `create a Machine
  Learning pipeline`_.

- **SQLPad**

  `SQLPad`_ is a web app for writing, running, and visualizing queries. Read
  our tutorial on how to `set up CrateDB with SQLPad`_.

- **StreamSets Data Collector**

  The `StreamSets`_ Data Collector is a lightweight and powerful engine that
  streams data in real time. Read our guide on `building data stream pipelines`_.


.. SEEALSO::

    For more tools and tutorials on how to use CrateDB with them, refer to the
    `integrations`_ category on our blog or the `integrations section`_ in our
    documentation.

.. NOTE::

    If you would like to add to this page, please `get in touch`_ or
    `edit this page`_ on GitHub.


.. _activerecord-crate-adaptor: https://rubygems.org/gems/activerecord-crate-adapter
.. _asyncpg: https://github.com/MagicStack/asyncpg
.. _Authenticate: https://crate.io/docs/crate/reference/en/latest/admin/auth/index.html
.. _Azure Function: https://azure.microsoft.com/en-in/services/functions/
.. _building data stream pipelines: https://crate.io/docs/crate/howtos/en/latest/integrations/streamsets.html
.. _client compatibility notes: https://crate.io/docs/crate/reference/en/latest/interfaces/postgres.html#client-compatibility
.. _crate-connect: https://www.npmjs.com/package/crate-connect
.. _CrateDB Npgsql fork: https://crate.io/docs/clients/npgsql/en/latest/
.. _CrateDB PDO: https://crate.io/docs/clients/pdo/en/latest/
.. _CrateDB DBAL: https://crate.io/docs/clients/dbal/en/latest/
.. _CrateDB driver for Laravel: https://github.com/RatkoR/laravel-crate.io
.. _CrateDB integration tutorials: https://community.crate.io/t/overview-of-cratedb-integration-tutorials/1015
.. _crate-jdbc: https://crate.io/docs/clients/jdbc/en/latest/
.. _cratejs: https://www.npmjs.com/package/cratejs
.. _crate-python: https://crate.io/docs/clients/python/en/latest/
.. _craterl: https://github.com/crate/craterl
.. _crate_ruby: https://rubygems.org/gems/crate_ruby
.. _crate-scala: https://github.com/alexanderjarvis/crate-scala
.. _crate-connector: https://github.com/LiamHaworth/crate-connector
.. _create a data enrichment pipeline: https://crate.io/docs/crate/howtos/en/latest/integrations/azure-functions.html
.. _create a Machine Learning pipeline: https://crate.io/docs/crate/howtos/en/latest/integrations/r.html
.. _DBD::Crate: https://github.com/mamod/DBD-Crate
.. _edit this page: https://github.com/crate/crate-clients-tools/blob/master/docs/index.rst
.. _get in touch: https://crate.io/contact
.. _GitHub: https://github.com/crate/crate-clients-tools
.. _Grafana: https://grafana.com
.. _implementation differences: https://crate.io/docs/crate/reference/en/latest/interfaces/postgres.html#implementation-differences
.. _integrations: https://crate.io/blog/tag/integrations
.. _integrations section: https://crate.io/docs/crate/howtos/en/latest/integrations/index.html
.. _let us know: https://crate.io/contact
.. _node-crate: https://www.npmjs.com/package/node-crate
.. _node-postgres: https://node-postgres.com/
.. _Npgsql: https://www.npgsql.org/
.. _our JDBC driver: https://crate.io/docs/reference/jdbc
.. _pair CrateDB with Grafana: https://crate.io/blog/visualizing-time-series-data-with-grafana-and-cratedb
.. _Pentaho: http://www.pentaho.com
.. _Petaho Kettle: https://github.com/pentaho/pentaho-kettle
.. _pgx: https://github.com/jackc/pgx
.. _PostgreSQL JDBC: https://jdbc.postgresql.org/
.. _PostgreSQL wire protocol: https://crate.io/docs/crate/reference/en/latest/interfaces/postgres.html
.. _R: https://www.r-project.org
.. _schema: https://crate.io/docs/crate/reference/en/latest/general/ddl/create-table.html#schemas
.. _set up CrateDB with SQLPad: https://crate.io/blog/use-cratedb-with-sqlpad-as-a-self-hosted-query-tool-and-visualizer
.. _SQLAlchemy: https://crate.io/docs/clients/python/en/latest/sqlalchemy.html
.. _SQLPad: https://github.com/sqlpad/sqlpad
.. _StreamSets: https://streamsets.com/opensource
.. _superuser: https://crate.io/docs/crate/reference/en/latest/admin/user-management.html
.. _with known issues: https://github.com/crate/crate/issues?q=is%3Aopen+is%3Aissue+label%3A%22client%3A+PostgreSQL+JDBC%22
