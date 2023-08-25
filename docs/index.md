(index)=

# CrateDB Clients and Tools


## About CrateDB

CrateDB is a distributed and scalable open-source SQL database for storing and
analyzing massive amounts of data in near real-time, even with complex queries.
It is PostgreSQL-compatible, and based on Lucene.

Users are operating CrateDB clusters that store information in the range of
billions of records, and terabytes of data, equally accessible without any
retrieval penalty on data point age.


## Connectivity

This section introduces you to the canonical set of database drivers, client-
and developer-applications, and how to configure them to connect to CrateDB.
Just to name a few, it is about the CrateDB Admin UI, `crash`, `psql`,
DataGrip, and DBeaver applications, the Java/JDBC/Python drivers, the SQLAlchemy
and Flink dialects, and more.

::::{grid} 1 2 2 3
:margin: 4 4 0 0
:gutter: 1


:::{grid-item-card} {material-outlined}`code;2em` IDE
:link: ide
:link-type: ref

Learn how to connect to CrateDB using a database IDE like DataGrip
or DBeaver.
:::


:::{grid-item-card} {material-outlined}`terminal;2em` CLI
:link: cli
:link-type: ref

Learn how to connect to a CrateDB cluster using command-line
based terminal programs.
:::


:::{grid-item-card} {material-outlined}`link;2em` Library
:link: connect
:link-type: ref

Learn how to configure your favorite client library to connect to a
CrateDB cluster.
:::


::::


## Integrations

CrateDB integrates well with a diverse set of applications and tools concerned
with analytics, visualization, and data wrangling, in the areas of ETL, BI, 
metrics aggregation and monitoring, and more.

::::{grid} 1 2 2 4
:margin: 4 4 0 0
:gutter: 1


:::{grid-item-card} {material-outlined}`integration_instructions;2em` Overview
:link: https://community.crate.io/t/overview-of-cratedb-integration-tutorials/1015
:link-type: url

Use CrateDB with popular applications, frameworks, and tools.
:::


:::{grid-item-card} {material-outlined}`transform;2em` ETL
:link: etl
:link-type: ref

Use ETL applications and frameworks for transferring data in and out of CrateDB.
:::


:::{grid-item-card} {material-outlined}`analytics;2em` Analytics
:link: analyze
:link-type: ref

Analyze information in your CrateDB cluster.
:::


:::{grid-item-card} {material-outlined}`bar_chart;2em` Visualization
:link: visualize
:link-type: ref

Visualize information in your CrateDB cluster.
:::


::::



```{note} Contributions are welcome.

If you would like to add items about integrations with other tools to this
documentation section, please [get in touch], or directly edit this page on
GitHub. You will find corresponding links within the topmost right navigation
element.
```

```{seealso}
Looking for the previous content on this page? Visit [](#index-legacy).
```


```{toctree}
:hidden:

IDE applications <connect/ide>
CLI programs <connect/cli>
Database drivers <connect/index>

```

```{toctree}
:hidden:

Load and export data <integrate/etl>
Analyze data <integrate/analyze>
Visualize data <integrate/visualize>
```

```{toctree}
:hidden:

Legacy documentation <legacy>
```


[get in touch]: https://crate.io/contact
