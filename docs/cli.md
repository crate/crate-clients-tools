(cli)=
(connect-cli)=
# Using command-line programs with CrateDB

This section provides a quick overview about a few CLI programs, and how to
use them for connecting to CrateDB clusters. We recommend to use `crash`,
`psql`, or `http` (HTTPie).


(crash)=
## crash

The [CrateDB Shell] (aka Crash) is an interactive command-line interface (CLI)
tool for working with CrateDB.

An example command to connect to your cluster will look like this:
```{code-block} console
crash --hosts 'https://<name-of-your-cluster>.cratedb.net:4200' -U 'admin' -W
```


(psql)=
## psql

`psql` is a terminal-based front-end to PostgreSQL. It enables you to type in
queries interactively, issue them to PostgreSQL, and see the query results.
For more information, see the [psql documentation].

Example command to connect to your cluster will look like this:
```{code-block} console
psql -h '<name-of-your-cluster>.cratedb.net' -U 'admin' -W
```


[CrateDB Shell]: inv:crate-crash:*:label#index
[psql documentation]: https://www.postgresql.org/docs/current/app-psql.html
