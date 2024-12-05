(index)=
(catalog)=
(drivers)=
(frameworks)=
(integrations)=

# CrateDB Ecosystem Catalog

Database drivers, libraries, frameworks, and applications for CrateDB.


:::{rubric} About CrateDB
:::
CrateDB is a distributed and scalable open-source SQL database based on Lucene,
with PostgreSQL compatibility.
CrateDB clusters store information in the range of billions of records, and
terabytes of data, and run analytics in near real time, even with complex
queries.
CrateDB can be used for enterprise data warehouse workloads, it
works across clouds and scales with your data.

## Connectivity

The canonical set of database drivers, client- and developer-applications, and
how to configure them to connect to CrateDB.

Just to name a few, the sections below are about the CrateDB Admin UI, the
Crash CLI terminal program, connecting with PostgreSQL's psql client, the
DataGrip, and DBeaver IDE applications, the Java/JDBC/Python drivers, the
SQLAlchemy and Flink dialects, and more.

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:gutter: 1


:::{grid-item-card} {material-outlined}`code;2em` IDE
:link: guide:ide
:link-type: ref

Connect to CrateDB using a database IDE like DataGrip or DBeaver.
:::


:::{grid-item-card} {material-outlined}`terminal;2em` CLI
:link: cli
:link-type: ref

Connect to CrateDB using command-line based terminal programs.
:::

::::


::::{grid} 1 2 2 3
:margin: 4 4 0 0
:gutter: 1

:::{grid-item-card} {material-outlined}`link;2em` Drivers
:link: connect
:link-type: ref

List of HTTP and PostgreSQL client drivers, and tutorials.
:::


:::{grid-item-card} {material-outlined}`data_object;2em` ORM Libraries
:link: orm
:link-type: ref

Connectivity with ORM libraries like SQLAlchemy.
:::


:::{grid-item-card} {material-outlined}`crop_landscape;2em` DataFrame Libraries
:link: df
:link-type: ref

Connectivity with DataFrame libraries like pandas and Dask.
:::


::::


## Integrations

CrateDB integrates with a diverse set of applications and tools concerned
with analytics, visualization, and data wrangling, in the areas of data loading
and export (ETL), business intelligence (BI), metrics aggregation and monitoring,
machine learning, and more.

::::{grid} 1
:margin: 4 4 0 0
:gutter: 1

:::{grid-item-card} {material-outlined}`integration_instructions;2em` Overview
:link: https://community.cratedb.com/t/overview-of-cratedb-integration-tutorials/1015
:link-type: url

Learn how to use CrateDB with popular applications, frameworks, and tools.
All on one page.
:::

::::

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:gutter: 1


:::{grid-item-card} {material-outlined}`code;2em` Programming Frameworks
:link: framework
:link-type: ref

Connectivity with open-source programming frameworks and libraries
like Gradio, Plotly, or Streamlit.
:::


:::{grid-item-card} {material-outlined}`transform;2em` ETL
:link: etl
:link-type: ref

ETL applications and frameworks for transferring data in and out of CrateDB.
:::


:::{grid-item-card} {material-outlined}`query_stats;2em` System Metrics
:link: metrics
:link-type: ref

Integrations and long-term storage for systems monitoring tools like
Prometheus and Telegraf.
:::


:::{grid-item-card} {material-outlined}`bar_chart;2em` Data Visualization
:link: visualize
:link-type: ref

Visualize information in your CrateDB cluster.
:::


:::{grid-item-card} {material-outlined}`analytics;2em` Business Intelligence
:link: bi
:link-type: ref

Analyze information in your CrateDB cluster.
:::


:::{grid-item-card} {material-outlined}`model_training;2em` Machine Learning
:link: ml
:link-type: ref

Adapters and integrations with machine learning frameworks.
:::



::::



```{note} Contributions to the pages in this section and subsections are much welcome.
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

CLI programs <connect/cli>
Database Drivers <connect/index>
ORM Libraries <connect/orm>
DataFrame Libraries <connect/df>
```

```{toctree}
:hidden:

Programming Frameworks <integrate/framework>
Load and Export <integrate/etl>
System Metrics <integrate/metrics>
Data Visualization <integrate/visualize>
Business Intelligence <integrate/bi>
Machine Learning <integrate/ml>
```

```{toctree}
:hidden:

Build Status <status>
Legacy documentation <legacy>
```


[get in touch]: https://cratedb.com/contact
