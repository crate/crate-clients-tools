(df)=
(dataframes)=
# CrateDB and DataFrame libraries

This documentation section lists DataFrame libraries and frameworks which can
be used together with CrateDB. Hands-on tutorials about them can be found
on the ["connect" section of the CrateDB Guide].


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


## Polars

```{div}
:style: "float: right; margin-left: 0.5em"
[![](https://github.com/pola-rs/polars-static/raw/master/logos/polars-logo-dark.svg){w=180px}](https://pola.rs/)
```

[Polars] is a blazingly fast DataFrames library with language bindings for
Rust, Python, Node.js, R, and SQL. Polars is powered by a multithreaded,
vectorized query engine, it is open source, and written in Rust.

- **Fast:** Written from scratch in Rust and with performance in mind,
  designed close to the machine, and without external dependencies.

- **I/O:** First class support for all common data storage layers: local,
  cloud storage & databases.

- **Intuitive API:** Write your queries the way they were intended. Polars,
  internally, will determine the most efficient way to execute using its query
  optimizer. Polars' expressions are intuitive and empower you to write
  readable and performant code at the same time.

- **Out of Core:** The streaming API allows you to process your results without
  requiring all your data to be in memory at the same time.

- **Parallel:** Polars' multi-threaded query engine utilises the power of your
  machine by dividing the workload amongst the available CPU cores without any
  additional configuration.

- **Vectorized Query Engine:** Uses [Apache Arrow], a columnar data format, to
  process your queries in a vectorized manner and SIMD to optimize CPU usage.
  This enables cache-coherent algorithms and high performance on modern processors. 

- **Open Source:** Polars is and always will be open source. Driven by an active
  community of developers. Everyone is encouraged to add new features and contribute.
  It is free to use under the MIT license.

**Data formats**

Polars supports reading and writing to many common data formats.
This allows you to easily integrate Polars into your existing data stack.
 
- Text: CSV & JSON
- Binary: Parquet, Delta Lake, AVRO & Excel
- IPC: Feather, Arrow
- Databases: MySQL, Postgres, SQL Server, Sqlite, Redshift & Oracle
- Cloud Storage: S3, Azure Blob & Azure File

```{div}
:style: "clear: both"
```



[Apache Arrow]: https://arrow.apache.org/
["connect" section of the CrateDB Guide]: inv:guide:*:label#connect
[Dask]: https://www.dask.org/
[Dask DataFrames]: https://docs.dask.org/en/latest/dataframe.html
[Dask Futures]: https://docs.dask.org/en/latest/futures.html
[pandas]: https://pandas.pydata.org/
[Polars]: https://pola.rs/
