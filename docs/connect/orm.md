(orm)=
# Use CrateDB with ORM libraries

This documentation section lists ORM libraries and frameworks which can
be used together with CrateDB, and outlines how to use them optimally.


## SQLAlchemy

```{div}
:style: "float: right"
[![](https://www.sqlalchemy.org/img/sqla_logo.png){w=180px}](https://www.sqlalchemy.org/)
```

[SQLAlchemy] is the Python SQL toolkit and Object Relational Mapper that
gives application developers the full power and flexibility of SQL.

It plays an important role, because popular Python-based [DataFrame](df.md)
and [ML](../integrate/ml.md) libraries, and a few [ETL](../integrate/etl.md)
frameworks, are using SQLAlchemy as data abstraction library when connecting to
[RDBMS].

```{div}
:style: "clear: both"
```

**See also**
- [SQLAlchemy support]
- [SQLAlchemy by example]
- [Code examples]



[Code examples]: https://github.com/crate/cratedb-examples/tree/main/by-language/python-sqlalchemy
[RDBMS]: https://en.wikipedia.org/wiki/RDBMS
[SQLAlchemy]: https://www.sqlalchemy.org/
[SQLAlchemy by example]: https://cratedb.com/docs/python/en/latest/by-example/index.html#sqlalchemy-by-example
[SQLAlchemy support]: https://cratedb.com/docs/python/en/latest/sqlalchemy.html
