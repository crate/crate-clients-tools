(connect)=

# Connect to a CrateDB cluster


## Introduction

CrateDB supports both the [HTTP protocol], and the [PostgreSQL wire protocol].
Accordingly, many clients that work with either HTTP, or PostgreSQL, will also
work with CrateDB.

```{tip}
- Specify the [schema] name `doc`, if you are asked for a *database name*.
- The default [superuser] on a vanilla CrateDB cluster is called `crate`,
  without a password.
- When aiming to authenticate properly, please learn about the available
  [authentication] options. 
```

### Command-line

This section outlines a few test flight commands which can be used to validate
PostgreSQL connectivity using the `psql` program, and HTTP connectivity using
the `curl` and [HTTPie] programs.


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


### Starter guides

This section enumerates a few client libraries by example, demonstrating
how to connect to your CrateDB cluster correspondingly.

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
[Connect to CrateDB from .NET (C#)](https://github.com/crate/cratedb-examples/tree/main/by-language/csharp-npgsql)
<br>
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
JavaScript, TypeScript
```
```{sd-item}
[Connect to CrateDB from Node.js using `node-postgres` or `node-crate`](#javascript)
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

This section enumerates a few more advanced uses cases by example.

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
[HTTPie]: https://httpie.io/
[PostgreSQL wire protocol]: https://crate.io/docs/crate/reference/en/latest/interfaces/postgres.html
[schema]: https://crate.io/docs/crate/reference/en/latest/general/ddl/create-table.html#schemas
[superuser]: https://crate.io/docs/crate/reference/en/latest/admin/user-management.html

[^asyncio-support]: Has support for Python's `asyncio`.
[^blob-support]: Has support for [CrateDB BLOBs].
[^node-postgres]: Has support for callbacks, promises, async/await, connection pooling, prepared statements, cursors, streaming results, C/C++ bindings, rich type parsing, and more.
