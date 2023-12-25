(df)=
(dataframes)=
# Use CrateDB with DataFrame libraries

This documentation section lists DataFrame libraries and frameworks which can
be used together with CrateDB, and outlines how to use them optimally.


## Dask

[Dask] is a parallel computing library for analytics with task scheduling.
It is built on top of the Python programming language, making it easy to scale
the Python libraries that you know and love, like NumPy, pandas, and scikit-learn.

```{div}
:style: "float: right"
[![](https://github.com/crate/crate-clients-tools/assets/453543/99bd2234-c501-479b-ade7-bcc2bfc1f288){w=180px}](https://www.dask.org/)
```

- [Dask DataFrames] help you process large tabular data by parallelizing pandas,
  either on your laptop for larger-than-memory computing, or on a distributed
  cluster of computers.

- [Dask Futures], implementing a real-time task framework, allow you to scale
  generic Python workflows across a Dask cluster with minimal code changes,
  by extending Python's `concurrent.futures` interface.

```{div}
:style: "clear: both"
```

**See also**
- [Guide to efficient data ingestion to CrateDB with pandas and Dask]
- [Efficient batch/bulk INSERT operations with pandas, Dask, and SQLAlchemy]
- [Code examples]

## pandas

```{div}
:style: "float: right"
[![](https://pandas.pydata.org/static/img/pandas.svg){w=180px}](https://pandas.pydata.org/)
```

[pandas] is a fast, powerful, flexible, and easy to use open source data analysis
and manipulation tool, built on top of the Python programming language. 

```{div}
:style: "clear: both"
```

**See also**
- [Importing Parquet files into CrateDB using Apache Arrow and SQLAlchemy]
- [Guide to efficient data ingestion to CrateDB with pandas]
- [Guide to efficient data ingestion to CrateDB with pandas and Dask]
- [Efficient batch/bulk INSERT operations with pandas, Dask, and SQLAlchemy]
- [Code examples]


[Code examples]: https://github.com/crate/cratedb-examples/tree/main/by-language/python-sqlalchemy
[Dask]: https://www.dask.org/
[Dask DataFrames]: https://docs.dask.org/en/latest/dataframe.html
[Dask Futures]: https://docs.dask.org/en/latest/futures.html
[Efficient batch/bulk INSERT operations with pandas, Dask, and SQLAlchemy]: https://cratedb.com/docs/python/en/latest/by-example/sqlalchemy/dataframe.html
[Importing Parquet files into CrateDB using Apache Arrow and SQLAlchemy]: https://community.crate.io/t/importing-parquet-files-into-cratedb-using-apache-arrow-and-sqlalchemy/1161
[pandas]: https://pandas.pydata.org/
[Guide to efficient data ingestion to CrateDB with pandas]: https://community.crate.io/t/guide-to-efficient-data-ingestion-to-cratedb-with-pandas/1541
[Guide to efficient data ingestion to CrateDB with pandas and Dask]: https://community.crate.io/t/guide-to-efficient-data-ingestion-to-cratedb-with-pandas-and-dask/1482
