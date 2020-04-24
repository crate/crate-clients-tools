.. _index:

=========================
CrateDB Clients and Tools
=========================

CrateDB is a distributed SQL database that makes it simple to store and analyze
massive amounts of machine data in real-time.

.. NOTE::

    If you would like to see something added to this page, please `get in
    touch`_ or `edit this page`_ on GitHub.

.. toctree::
   :hidden:

   tools/streamsets


Clients
=======

Below is a selection of CrateDB client libraries.

Pick your library, and start building!

.. list-table::
    :header-rows: 1

    * - Language
      - Maintainers
      - Official support
      - Driver
    * - C# (.NET)
      - Crate.IO
      - ✔️
      - `Npgsql`_
    * - Erlang
      - Community
      - ❌
      - `craterl`_
    * - Go
      - Community
      - ✔️
      - `pgx`_
    * - Java
      - Crate.IO
      - ✔️
      - `crate-jdbc`_
    * - Node.JS
      - Community
      - ✔️
      - `node-postgres`_
    * - Node.JS
      - Community
      - ❌
      - `crate-connect`_
    * - Node.JS
      - Community
      - ❌
      - `cratejs`_
    * - Node.JS
      - Community
      - ❌
      - `node-crate`_
    * - PHP
      - Crate.IO
      - ✔️
      - `CrateDB PDO`_
    * - Perl
      - Community
      - ❌
      - `DBD::Crate`_
    * - Python
      - Crate.IO
      - ✔️
      - `crate-python`_
    * - Python
      - Community
      - ✔️
      - `asyncpg`_
    * - Ruby
      - Community
      - ❌
      - `crate_ruby`_
    * - Scala
      - Community
      - ❌
      - `crate-scala`_

.. TIP::

    CrateDB supports the `PostgreSQL wire protocol`_. Accordingly, many clients
    that work with PostgreSQL also work with CrateDB.

    You can try this out for yourself:

    - Configure a PostgreSQL connection, but point your client to a CrateDB
      server instead of a PostgreSQL server
    - `Authenticate`_ as the ``crate`` `superuser`_ with no password
    - Specify the ``doc`` `schema`_, if you're asked for a *database name*

    Check out the `client compatibility notes`_ and `implementation
    differences`_ for information about known limitations.

    If you run into issues, please `let us know`_. We regularly update CrateDB
    to accomodate new PostgreSQL clients.


Tools
=====

CrateDB integrates with many different PostgreSQL compatible tools.

Some of our favourite tools include:

- **Pentaho**

  `Pentaho`_ prepares and blends data, delivering business analytics from any
  source. You can connect to CrateDB clusters by using `Petaho Kettle`_ and the
  standalone version of `our JDBC driver`.

- **StreamSets Data Collector**

  The `StreamSets`_ Data Collector is a lightweight, powerful engine that
  streams data in real time. `Read more`_.

.. SEEALSO::

    The `integrations`_ category on our blog.


.. _ActiveRecord: https://rubygems.org/gems/activerecord-crate-adapter
.. _asyncpg: https://github.com/MagicStack/asyncpg
.. _Authenticate: https://crate.io/docs/crate/reference/en/latest/admin/auth/index.html
.. _blog post: https://crate.io/a/visualize-crate-data-with-metabase/
.. _client compatibility notes: https://crate.io/docs/crate/reference/en/latest/interfaces/postgres.html#client-compatibility
.. _crate_ruby: https://rubygems.org/gems/crate_ruby
.. _crate-connect: https://www.npmjs.com/package/crate-connect
.. _crate-jdbc: https://crate.io/docs/clients/jdbc/en/latest/
.. _crate-python: https://crate.io/docs/clients/python/en/latest/
.. _crate-scala: https://github.com/alexanderjarvis/crate-scala
.. _Crate.Client: https://github.com/mfussenegger/crate-mono
.. _CrateDB PDO: https://crate.io/docs/clients/pdo/en/latest/
.. _cratejs: https://www.npmjs.com/package/cratejs
.. _craterl: https://github.com/crate/craterl
.. _DBAL: https://crate.io/docs/clients/dbal/en/latest/
.. _DBD::Crate: https://github.com/mamod/DBD-Crate
.. _edit this page: https://github.com/crate/crate-tutorials/blob/master/docs/getting-started/start-building/index.rst
.. _get in touch: https://crate.io/contact/
.. _GitHub: https://github.com/crate/crate-clients-tools
.. _implementation differences: https://crate.io/docs/crate/reference/en/latest/interfaces/postgres.html#implementation-differences
.. _integrations: https://crate.io/a/category/client-tools/
.. _let us know: https://crate.io/contact/
.. _Loopback: https://github.com/lovelysystems/loopback-connector-crateio
.. _Metabase: http://www.metabase.com/
.. _node-crate: https://www.npmjs.com/package/node-crate
.. _node-postgres: https://node-postgres.com/
.. _Npgsql: https://crate.io/docs/clients/npgsql/en/latest/
.. _our JDBC driver: https://crate.io/docs/reference/jdbc
.. _Pentaho: http://community.pentaho.com
.. _Petaho Kettle: https://github.com/pentaho/pentaho-kettle
.. _pgx: https://github.com/jackc/pgx
.. _PostgreSQL wire protocol: https://crate.io/docs/crate/reference/en/latest/interfaces/postgres.html
.. _read more: https://crate.io/docs/crate/guide/en/latest/tools/streamsets.html
.. _schema: https://crate.io/docs/crate/reference/en/latest/general/ddl/create-table.html#schemas
.. _SQLAlchemy: https://crate.io/docs/clients/python/en/latest/sqlalchemy.html
.. _StreamSets: https://streamsets.com/opensource
.. _superuser: https://crate.io/docs/crate/reference/en/latest/admin/user-management.html#introduction

