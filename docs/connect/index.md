(connect)=

# Connect to a CrateDB cluster

This documentation section is about connecting your applications and drivers to CrateDB.


## Configure

CrateDB supports both the [HTTP protocol]  {tags-success}`HTTP`, 
and the [PostgreSQL wire protocol] {tags-primary}`PG`.

Accordingly, many clients that work with either HTTP, or PostgreSQL, will also
work with CrateDB. In order to connect to CrateDB, your application or driver
needs to be configured with corresponding settings.

::::::{tab-set}

:::::{tab-item} CrateDB and CrateDB Cloud

::::{grid}
:margin: 0
:padding: 0

:::{grid-item}
:columns: 5
:margin: 0
:padding: 0

**Connection properties**

Make sure to use the correct connection properties.

:Host: `<clustername>`.cratedb.net
:Port: 5432 (PostgreSQL) or 4200 (HTTP)
:User: `<username>`
:Pass: `<password>`

:::

:::{grid-item}
:columns: 7
:margin: 0
:padding: 0

**Connection-string examples**

Please note that different applications and drivers may obtain
connection properties in different formats.

A native PostgreSQL connection string.
`postgresql://<username>@<clustername>.cratedb.net/crate`

A connection string for SQLAlchemy or Apache Flink.
`crate://<username>@<clustername>.cratedb.net/crate`

An HTTP URL to visit Admin UI.
`https://<username>@<clustername>.cratedb.net:4200/`

:::

::::

:::::

:::::{tab-item} CrateDB on localhost

::::{grid}
:margin: 0
:padding: 0

:::{grid-item}
:columns: 5
:margin: 0
:padding: 0

**Connection properties**

Make sure to use the correct connection properties.

:Host: localhost
:Port: 5432 (PostgreSQL) or 4200 (HTTP)
:User: `crate`
:Pass: (empty)

:::

:::{grid-item}
:columns: 7
:margin: 0
:padding: 0

**Connection-string examples**

Please note that different applications and drivers may obtain
connection properties in different formats.

A native PostgreSQL connection string.
`postgresql://crate@localhost:5432/crate`

A connection string for SQLAlchemy or Apache Flink.
`crate://crate@localhost/crate`

An HTTP URL to visit Admin UI.
`http://crate@localhost:4200/`

:::

::::
:::::

::::::


```{tip}
- Specify the [schema] name `doc`, if you are asked for a *database name*.
- The default [superuser] on a vanilla CrateDB cluster is called `crate`,
  without a password.
- When aiming to authenticate properly, please learn about the available
  [authentication] options. 
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
```{sd-item} .NET
```
```{sd-item}
[Npgsql](https://www.npgsql.org/)
```
```{sd-item}
An open source ADO.NET Data Provider for PostgreSQL, for program written in C#,
Visual Basic, and F#.
```
```{sd-item}
{tags-primary}`PG`
```
:::

:::{sd-row}
```{sd-item} .NET
```
```{sd-item}
[CrateDB Npgsql fork](https://crate.io/docs/npgsql/)
```
```{sd-item}
This fork of the official driver was needed prior to CrateDB 4.2.
```
```{sd-item}
{tags-primary}`PG`
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
[CrateDB PgJDBC fork](https://crate.io/docs/jdbc/)
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
```{sd-item} Node.js
```
```{sd-item}
[node-postgres](https://node-postgres.com/)
```
```{sd-item}
A collection of Node.js modules for interfacing with a PostgreSQL database
using JavaScript or TypeScript. [^node-postgres]
```
```{sd-item}
{tags-primary}`PG`
```
:::

:::{sd-row}
```{sd-item} PHP
```
```{sd-item}
[CrateDB PDO driver](https://crate.io/docs/pdo/)
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
[CrateDB DBAL adapter](https://crate.io/docs/dbal/)
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
[CrateDB Python driver](https://crate.io/docs/python/)
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

:::{sd-row}
```{sd-item} Ruby
```
```{sd-item}
[CrateDB Ruby driver](https://github.com/crate/crate_ruby)
```
```{sd-item}
A Ruby client library for CrateDB.
```
```{sd-item}
{tags-success}`HTTP`
```
:::

:::{sd-row}
```{sd-item} Ruby
```
```{sd-item}
[CrateDB ActiveRecord adapter](https://github.com/crate/activerecord-crate-adapter)
```
```{sd-item}
Ruby on Rails ActiveRecord adapter for CrateDB.
```
```{sd-item}
{tags-success}`HTTP`
```
:::

::::

```{note}
While we generally recommend the PostgreSQL interface (PG) for maximum compatibility
in PostgreSQL environments, the HTTP interface supports [CrateDB bulk operations]
and [CrateDB BLOBs], which are not supported by the PostgreSQL protocol.
```


## Examples and guides

This section enumerates a few client libraries and frameworks by example, demonstrating
how to use them to connect to your CrateDB cluster.

### Starter guides

A few basic examples and tutorials about how to connect to CrateDB, and how to run basic
database operations.

::::{sd-table}
:widths: 2 10
:row-class: top-border

:::{sd-row}
```{sd-item}
**Language/
Framework**
```
```{sd-item} **Guideline and code example**
```
:::

:::{sd-row}
```{sd-item}
.NET/C#
```
```{sd-item}
[Connect to CrateDB from .NET (C#) (runnable)](https://github.com/crate/cratedb-examples/tree/main/by-language/csharp-npgsql)
```
:::

:::{sd-row}
```{sd-item}
Java
```
```{sd-item}
[Connect to CrateDB from Java using JDBC](#java)
<br>
[Connect to CrateDB from Java using JDBC (runnable)](https://github.com/crate/cratedb-examples/tree/main/by-language/java-jdbc)
```
:::

:::{sd-row}
```{sd-item}
Node.js
```
```{sd-item}
[Connect to CrateDB from Node.js/JavaScript/TypeScript using `node-postgres`
or `node-crate`](#javascript)
```
:::

:::{sd-row}
```{sd-item}
PHP
```
```{sd-item}
[Connect to CrateDB from PHP using PDO and DBAL drivers](#php)
<br>
[Connect to CrateDB from PHP using PDO (runnable)](https://github.com/crate/cratedb-examples/tree/main/by-language/php-pdo)
<br>
[Connect to CrateDB from PHP using AMPHP (runnable)](https://github.com/crate/cratedb-examples/tree/main/by-language/php-amphp)
```
:::

:::{sd-row}
```{sd-item}
Python
```
```{sd-item}
[Connect to CrateDB from Python using different kinds of drivers](#python)
```
:::

:::{sd-row}
```{sd-item}
Ruby
```
```{sd-item}
[Connect to CrateDB from Ruby](#ruby)
<br>
[Connect to CrateDB from Ruby (runnable)](https://github.com/crate/cratedb-examples/tree/main/by-language/ruby)
```
:::

::::


### Advanced guides

A few more advanced uses cases by example.

::::{sd-table}
:widths: 2 10
:row-class: top-border

:::{sd-row}
```{sd-item}
**Language/
Framework**
```
```{sd-item} **Guideline and code example**
```
:::

:::{sd-row}
```{sd-item}
Java
```
```{sd-item}
[Use CrateDB with Apache Flink and Apache Kafka](https://github.com/crate/cratedb-examples/tree/main/stacks/kafka-flink)
```
:::

:::{sd-row}
```{sd-item}
Java
```
```{sd-item}
[Use CrateDB with JDBC and jOOQ](https://github.com/crate/cratedb-examples/tree/main/by-language/java-jooq)
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


[Authentication]: https://crate.io/docs/crate/reference/en/latest/admin/auth/index.html
[CrateDB BLOBs]: https://crate.io/docs/crate/reference/en/latest/general/blobs.html
[CrateDB bulk operations]: https://crate.io/docs/crate/reference/en/latest/interfaces/http.html#bulk-operations
[HTTP protocol]: https://en.wikipedia.org/wiki/HTTP
[PostgreSQL wire protocol]: https://crate.io/docs/crate/reference/en/latest/interfaces/postgres.html
[schema]: https://crate.io/docs/crate/reference/en/latest/general/ddl/create-table.html#schemas
[superuser]: https://crate.io/docs/crate/reference/en/latest/admin/user-management.html

[^asyncio-support]: Has support for Python's `asyncio`.
[^blob-support]: Has support for [CrateDB BLOBs].
[^node-postgres]: Has support for callbacks, promises, async/await, connection pooling, prepared statements, cursors, streaming results, C/C++ bindings, rich type parsing, and more.
