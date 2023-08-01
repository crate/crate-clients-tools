(connect)=

# Connect to a CrateDB cluster


## Getting started

CrateDB supports both the HTTP protocol, and the [PostgreSQL wire protocol].
Accordingly, many clients that work with PostgreSQL will also work with CrateDB.

### PostgreSQL

You can try this out for yourself:

- Using your favorite tool of choice, configure a PostgreSQL connection,
  but point your client to a CrateDB server instead of a PostgreSQL server.
- [Authenticate] as the ``crate`` [superuser] with no password.
- Specify the ``doc`` [schema], if you are asked for a *database name*.

For example, your connection string to a CrateDB cluster instance
might look like:
```text
# CrateDB Cloud
postgresql://<username>@<name-of-your-cluster>.cratedb.net
crate://<username>@<name-of-your-cluster>.cratedb.net:5432/

# Self-Managed
postgresql://crate@localhost:5432/doc
```


## Client libraries

We recommend to use those drivers and adapters for the corresponding languages and frameworks.

### Overview

::::{sd-table}
:widths: 2 3 5 2
:row-class: top-border

:::{sd-row}
```{sd-item} **Language**
```
```{sd-item} **Driver/Adapter**
```
```{sd-item} **Description**
```
```{sd-item} **Properties**
```
:::

:::{sd-row}
```{sd-item} Golang
```
```{sd-item}
[pgx](https://github.com/jackc/pgx)
```
```{sd-item}
A pure Go driver and toolkit for PostgreSQL.
```
```{sd-item}
{tags-primary}`PG`
```
:::

:::{sd-row}
```{sd-item} Java
```
```{sd-item}
[PostgreSQL JDBC](https://jdbc.postgresql.org/)
```
```{sd-item}
For connecting to CrateDB from any environment that supports it.
```
```{sd-item}
{tags-primary}`PG`
```
:::

:::{sd-row}
```{sd-item} Java
```
```{sd-item}
[CrateDB legacy JDBC driver](https://crate.io/docs/jdbc/)
```
```{sd-item}
For connecting to CrateDB within special scenarios, in order to leverage more
features of its type system, and to ignore the `ROLLBACK` statement.
```
```{sd-item}
{tags-primary}`PG`
```
:::

:::{sd-row}
```{sd-item} JavaScript, TypeScript
```
```{sd-item}
[node-postgres](https://node-postgres.com/)
```
```{sd-item}
A collection of Node.js modules for interfacing with a PostgreSQL database. [^node-postgres]
```
```{sd-item}
{tags-primary}`PG`
```
:::

:::{sd-row}
```{sd-item} PHP
```
```{sd-item}
[PHP PDO driver](https://crate.io/docs/pdo/)
```
```{sd-item}
For connecting to CrateDB from PHP.
```
```{sd-item}
{tags-success}`HTTP`
```
:::

:::{sd-row}
```{sd-item} PHP
```
```{sd-item}
[PHP DBAL adapter](https://crate.io/docs/dbal/)
```
```{sd-item}
For connecting to CrateDB from PHP, using DBAL and Doctrine.
```
```{sd-item}
{tags-success}`HTTP`
```
:::

:::{sd-row}
```{sd-item} Python
```
```{sd-item}
[DB-API driver](https://crate.io/docs/python/)
```
```{sd-item}
For connecting to CrateDB from Python. [^blob-support].
```
```{sd-item}
{tags-success}`HTTP`
```
:::

:::{sd-row}
```{sd-item} Python
```
```{sd-item}
[SQLAlchemy dialect](https://crate.io/docs/python/en/latest/sqlalchemy.html)
```
```{sd-item}
For connecting to CrateDB from Python, using SQLAlchemy.
```
```{sd-item}
{tags-success}`HTTP`
```
:::

:::{sd-row}
```{sd-item} Python
```
```{sd-item}
[asyncpg](https://github.com/MagicStack/asyncpg)
```
```{sd-item}
For connecting to CrateDB from Python. [^asyncio-support]
```
```{sd-item}
{tags-primary}`PG`
```
:::

:::{sd-row}
```{sd-item} Python
```
```{sd-item}
[psycopg3](https://www.psycopg.org/psycopg3/docs/)
```
```{sd-item}
For connecting to CrateDB from Python. [^asyncio-support]
```
```{sd-item}
{tags-primary}`PG`
```
:::

::::

```{note}
While we generally recommend the PostgreSQL interface (PG) for maximum compatibility
in PostgreSQL environments, the HTTP interface supports [CrateDB bulk operations]
and [CrateDB BLOBs], which are not supported by the PostgreSQL protocol.
```


### Examples and Tutorials

This section enumerates a few client libraries by example, and demonstrates
how to connect to your CrateDB cluster.

::::{sd-table}
:widths: 2 10
:row-class: top-border

:::{sd-row}
```{sd-item}
**Language/
Framework**
```
```{sd-item} **Getting started tutorial / Basic code example**
```
:::

:::{sd-row}
```{sd-item}
.NET/C#
```
```{sd-item}
[Basic example for connecting to CrateDB and CrateDB Cloud using .NET (C#)](https://github.com/crate/cratedb-examples/tree/main/by-language/csharp-npgsql)
```
:::

:::{sd-row}
```{sd-item}
Java
```
```{sd-item}
[A basic connection example code](#java)
```
:::

:::{sd-row}
```{sd-item}
Java
```
```{sd-item}
[Basic example for connecting to CrateDB and CrateDB Cloud using JDBC](https://github.com/crate/cratedb-examples/tree/main/by-language/java-jdbc)
```
:::

:::{sd-row}
```{sd-item}
Java
```
```{sd-item}
[Apache Kafka, Apache Flink, and CrateDB](https://github.com/crate/cratedb-examples/tree/main/stacks/kafka-flink)
```
:::

:::{sd-row}
```{sd-item}
Java
```
```{sd-item}
[jOOQ example application with CrateDB and JDBC connectivity](https://github.com/crate/cratedb-examples/tree/main/by-language/java-jooq)
```
:::

:::{sd-row}
```{sd-item}
JavaScript
```
```{sd-item}
[How to connect using node-postgres or node-crate](#javascript)
```
:::

:::{sd-row}
```{sd-item}
PHP
```
```{sd-item}
[Connect to CrateDB using PHP PDO and DBAL drivers](#php)
```
:::

:::{sd-row}
```{sd-item}
Python
```
```{sd-item}
[How to connect to CrateDB using different kinds of Python drivers](#python)
```
:::

:::{sd-row}
```{sd-item}
Ruby
```
```{sd-item}
[Connect to CrateDB using Ruby](#ruby)
```
:::

::::


```{toctree}
:maxdepth: 1
:hidden:

java
javascript
php
python
ruby
```


[Authenticate]: https://crate.io/docs/crate/reference/en/latest/admin/auth/index.html
[CrateDB BLOBs]: https://crate.io/docs/crate/reference/en/latest/general/blobs.html
[CrateDB bulk operations]: https://crate.io/docs/crate/reference/en/latest/interfaces/http.html#bulk-operations
[PostgreSQL wire protocol]: https://crate.io/docs/crate/reference/en/latest/interfaces/postgres.html
[schema]: https://crate.io/docs/crate/reference/en/latest/general/ddl/create-table.html#schemas
[superuser]: https://crate.io/docs/crate/reference/en/latest/admin/user-management.html

[^asyncio-support]: Has support for Python's `asyncio`.
[^blob-support]: Has support for [CrateDB BLOBs].
[^node-postgres]: Has support for callbacks, promises, async/await, connection pooling, prepared statements, cursors, streaming results, C/C++ bindings, rich type parsing, and more.
