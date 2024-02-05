(etl)=
# ETL with CrateDB

ETL / data pipeline applications and frameworks for transferring data in
and out of CrateDB.


::::{card} {material-outlined}`lightbulb;2em` Tutorials
:margin: 0 0 5 5
:shadow: md
:link: guide:etl
:link-type: ref

Learn how to integrate CrateDB with popular ETL frameworks and applications.
+++
{tag}`Extract, Transform, Load` {tag}`Data I/O, Import/Export` {tag}`ETL` {tag}`ELT`
::::


(apache-airflow)=
(airflow)=
(astronomer)=
## Apache Airflow / Astronomer

```{div}
:style: "float: right"
[![](https://19927462.fs1.hubspotusercontent-na1.net/hub/19927462/hubfs/Partner%20Logos/392x140/Apache-Airflow-Logo-392x140.png?width=784&height=280&name=Apache-Airflow-Logo-392x140.png){w=180px}](https://airflow.apache.org/)

[![](https://logowik.com/content/uploads/images/astronomer2824.jpg){w=180px}](https://www.astronomer.io/)
```
[Apache Airflow] is an open source software platform to programmatically author,
schedule, and monitor workflows, written in Python.
[Astronomer] offers managed Airflow services on the cloud of your choice, in
order to run Airflow with less overhead.

Airflow has a modular architecture and uses a message queue to orchestrate an
arbitrary number of workers. Pipelines are defined in Python, allowing for
dynamic pipeline generation and on-demand, code-driven pipeline invocation.

Pipeline parametrization is using the powerful Jinja templating engine.
To extend the system, you can define your own operators and extend libraries
to fit the level of abstraction that suits your environment.
```{div}
:style: "clear: both"
```

```{seealso}
[CrateDB and Apache Airflow]
```


:::{dropdown} **Managed Airflow**

```{div}
:style: "float: right"
[![](https://logowik.com/content/uploads/images/astronomer2824.jpg){w=180px}](https://www.astronomer.io/)
```

[Astro][Astronomer] is the best managed service in the market for teams on any step of their data
journey. Spend time where it counts.

- Astro runs on the cloud of your choice. Astro manages Airflow and gives you all the
  features you need to focus on what really matters – your data. All while connecting
  securely to any service in your network.
- Create Airflow environments with a click of a button.
- Protect production DAGs with easy Airflow upgrades and custom high-availability configs.
- Get visibility into what’s running with analytics views and easy interfaces for logs
  and alerts. Across environments.
- Take down tech-debt and learn how to drive Airflow best practices from the experts
  behind the project. Get world-class support, fast-tracked bug fixes, and same-day
  access to new Airflow versions.

```{div}
:style: "clear: both"
```
:::


## Apache Flink

```{div}
:style: "float: right"
[![](https://flink.apache.org/flink-header-logo.svg){w=180px}](https://flink.apache.org/)
```

[Apache Flink] is a framework and distributed processing engine for stateful
computations over unbounded and bounded data streams, written in Java.

Flink has been designed to run in all common cluster environments, perform
computations at in-memory speed and at any scale. It received the [2023 SIGMOD
Systems Award].

> Apache Flink greatly expanded the use of stream data-processing.

![](https://flink.apache.org/img/flink-home-graphic.png){h=200px}

:::{dropdown} **Managed Flink**
A few companies are specializing in offering managed Flink services.

- [Aiven] offers their managed [Aiven for Apache Flink] solution.
- [Immerok Cloud]'s offering is being converged into [Flink managed by Confluent].
:::


## Apache Hop

```{div}
:style: "float: right; margin-left: 0.3em"
[![](https://hop.apache.org/img/hop-logo.svg){w=180px}](https://hop.apache.org/)
```

[Apache Hop] aims to be a modern, open source data integration platform that is
easy to use, fast, and flexible. It facilitates all aspects of data and metadata
orchestration.

- **Visual development** enables developers to be more productive than they can
  be through code.

- **Workflows and pipelines** can be designed in the Hop Gui and run on the Hop
  native engine (local or remote), or on Spark, Flink, Google Dataflow or AWS EMR
  through Beam. _Design once, run anywhere._

- **Lifecycle Management** enables developers and administrators to switch between
  projects, environments and purposes without leaving your train of thought.

![](https://github.com/crate/crate-clients-tools/assets/453543/da6baf11-8430-4a0f-b2df-55717ce02802){h=120px}
![](https://github.com/crate/crate-clients-tools/assets/453543/60cfc82a-db0a-49f1-8e26-a37b774b3614){h=120px}
![](https://github.com/crate/crate-clients-tools/assets/453543/2bd59577-b664-45ae-a71e-36a130d36739){h=120px}

```{seealso}
[CrateDB and Apache Hop]
```


## Apache Kafka

```{div}
:style: "float: right"
[![](https://kafka.apache.org/logos/kafka_logo--simple.png){w=180px}](https://kafka.apache.org/)
```

[Apache Kafka] is an open-source distributed event streaming platform used by
thousands of companies for high-performance data pipelines, streaming analytics,
data integration, and mission-critical applications. 

```{seealso}
[CrateDB and Apache Kafka]
```

:::{dropdown} **Managed Kafka**
A few companies are specializing in offering managed Kafka services. We can't list
them all, see the [overview about more managed Kafka offerings].

- [Aiven for Apache Kafka]
- [Amazon Managed Streaming for Apache Kafka (MSK)]
- [Apache Kafka on Azure]
- [Azure Event Hubs for Apache Kafka]
- [Confluent Cloud]
- [DoubleCloud Managed Service for Apache Kafka]
:::


## dbt

```{div}
:style: "float: right"
[![](https://www.getdbt.com/ui/img/logos/dbt-logo.svg){w=180px}](https://www.getdbt.com/)
```

[dbt] is an open source tool for transforming data in data warehouses using Python and
SQL. It is an SQL-first transformation workflow platform that lets teams quickly and
collaboratively deploy analytics code following software engineering best practices
like modularity, portability, CI/CD, and documentation.

> dbt enables data analysts and engineers to transform their data using the same
> practices that software engineers use to build applications.

With dbt, anyone on your data team can safely contribute to production-grade data
pipelines.

The idea is that data engineers make source data available to an environment where
dbt projects run, for example with [Debezium](#debezium) or with [Airflow](#apache-airflow).
Afterwards, data analysts can run their dbt projects against this data to produce models
(tables and views) that can be used with a number of [BI tools](#bi-tools).

![](https://www.getdbt.com/ui/img/products/what-is-dbt-main-image.png){h=120px}
![](https://www.getdbt.com/ui/img/products/what-is-dbt-deploy.svg){h=120px}
![](https://www.getdbt.com/ui/img/products/what-is-dbt-eliminate-silos.svg){h=120px}

:::{dropdown} **Managed dbt**
```{div}
:style: "float: right"
[![](https://www.getdbt.com/ui/img/hero-dbt-cloud-features-2x5.png){w=180px}](https://www.getdbt.com/product/dbt-cloud/)
```

With [dbt Cloud], you can ditch time-consuming setup, and the struggles
of scaling your data production. dbt Cloud is a full-suite service that is built for
scale.

- Start building data products quickly using the dbt Cloud IDE with integrated security
  and governance controls.
- Schedule, deploy, and monitor your data products using the scalable and reliable dbt
  Cloud Scheduler.
- Help your data teams discover and reuse data products using hosted docs or integrations
  with the powerful Discovery API.
- Extend your workflow beyond dbt Cloud with 30+ seamless integrations covering a range
  of use cases across the Modern Data Stack, from observability and data quality to
  visualization, reverse ETL, and much more.
- Ship more high-quality data and scale your development like the 1000s of companies that
  use dbt Cloud. They’ve used its convenient and collaboration-friendly interface to
  eliminate the bottlenecks that keep growth limited.

```{div}
:style: "clear: both"
```
:::


## Debezium

```{div}
:style: "float: right"
[![](https://debezium.io/assets/images/color_white_debezium_type_600px.svg){w=180px}](https://debezium.io/)
```

[Debezium] is an open source distributed platform for change data capture. After
pointing it at your databases, you are able to subscribe to the event stream of
all database update operations.


## Kestra

```{div}
:style: "float: right"
[![](https://kestra.io/logo.svg){w=180px}](https://kestra.io/)
```

[Kestra] is an open source workflow automation and orchestration toolkit with a rich
plugin ecosystem. It enables users to automate and manage complex workflows in a
streamlined and efficient manner, defining them both declaratively, or imperatively
using any scripting language like Python, Bash, or JavaScript.

Kestra comes with a user-friendly web-based interface including a live-updating DAG
view, allowing users to create, modify, and manage scheduled and event-driven flows
without the need for any coding skills.

Plugins are at the core of Kestra's extensibility. Many plugins are available from
the Kestra core team, and creating your own is easy. With plugins, you can add new
functionality to Kestra.

![](https://kestra.io/landing/features/declarative1.svg){h=120px}
![](https://kestra.io/landing/features/flowable.svg){h=120px}
![](https://kestra.io/landing/features/monitor.svg){h=120px}

```{seealso}
[CrateDB and Kestra]
```


## Node-RED

```{div}
:style: "float: right"
[![](https://global.discourse-cdn.com/business6/uploads/nodered/original/1X/778549404735e222c89ce5449482a189ace8cdae.png){w=180px}](https://nodered.org/)
```

[Node-RED] is a programming tool for wiring together hardware devices, APIs
and online services within a low-code programming environment for event-driven
applications. It allows orchestrating message flows and transformations through
an intuitive web interface.

It provides a browser-based editor that makes it easy to wire together flows
using the wide range of elements called "nodes" from the palette that can be
deployed to its runtime in a single-click.

```{seealso}
[CrateDB and Node-RED]
```

:::{dropdown} **Managed Node-RED**
```{div}
:style: "float: right"
[![](https://github.com/crate/crate-clients-tools/assets/453543/200d1a92-1e38-453a-89bf-d8b727451fab){w=180px}](https://flowfuse.com/)
```

With [FlowFuse], and [FlowFuse Cloud], essentially unmanaged and managed DevOps
for Node-RED, you can reliably deliver Node-RED applications in a continuous,
collaborative, and secure manner.

- **Collaborative Development:** FlowFuse adds team collaboration to Node-RED,
  allowing multiple developers to work together on a single instance. With
  FlowFuse, developers can easily share projects, collaborate in real-time and
  streamline workflow for faster development and deployment.
- **Manage Remote Deployments:** Many organizations deploy Node-RED instances to
  remote servers or edge devices. FlowFuse automates this process by creating
  snapshots on Node-RED instances that can be deployed to multiple remote targets.
  It also allows for rollback in cases where something might not have gone correctly.
- **Streamline Application Delivery:** FlowFuse simplifies the software development
  lifecycle of Node-RED applications. You can now set up DevOps delivery pipelines
  to support development, test and production environments for Node-RED application
  delivery, see [Introduction to FlowFuse].
- **Flexible FlowFuse Deployment:** We want to make it easy for you to use FlowFuse,
  so we offer FlowFuse Cloud, a managed cloud service, or a self-hosted solution.
  You have the freedom to choose the deployment method that works best for your
  organization.

```{div}
:style: "clear: both"
```
:::


## Singer / Meltano

```{div}
:style: "float: right; margin-left: 0.3em"
[![](https://www.singer.io/img/singer_logo_full_black.svg){w=180px}](https://www.singer.io/)

[![](https://github.com/crate/crate-clients-tools/assets/453543/0c01e995-d7c2-4a4d-8e90-c6697fe2a85d){w=180px}](https://meltano.com/)
```

[Singer] is a composable open source ETL framework and specification, including powerful
data extraction and consolidation elements. [Meltano] is a declarative code-first data
integration engine adhering to the Singer specification.

[Meltano Hub] is the single source of truth to find any Meltano plugins as well
as Singer taps and targets.

```{div}
:style: "clear: both"
```


## SQL Server Integration Services

```{div}
:style: "float: right; margin-left: 0.3em"
[![](https://github.com/crate/crate-clients-tools/assets/453543/a93a0fdb-1a1e-451e-abcb-8f705e2b03f4){w=180px}](https://www.microsoft.com/)

[![](https://github.com/crate/crate-clients-tools/assets/453543/6317965a-0b69-4d8e-bc77-e12dfc8ed338){w=180px}](https://learn.microsoft.com/en-us/sql/)
```

Microsoft [SQL Server Integration Services] (SSIS) is a component of the Microsoft
SQL Server database software that can be used to perform a broad range of data
migration tasks. 

[SSIS] is a platform for data integration and workflow applications. It features a
data warehousing tool used for data extraction, transformation, and loading (ETL).
The tool may also be used to automate maintenance of SQL Server databases and
updates to multidimensional cube data. 

Integration Services can extract and transform data from a wide variety of sources
such as XML data files, flat files, and relational data sources, and then load the
data into one or more destinations.

Integration Services includes a rich set of built-in [tasks][ssis-tasks] and
[transformations][ssis-transformations], graphical tools for building packages, and
an SSIS Catalog database to store, run, and manage packages.

```{div}
:style: "clear: both"
```


[2023 SIGMOD Systems Award]: https://sigmod.org/2023-sigmod-systems-award/
[Aiven]: https://aiven.io/
[Aiven for Apache Flink]: https://aiven.io/flink
[Aiven for Apache Kafka]: https://aiven.io/kafka
[Amazon Managed Streaming for Apache Kafka (MSK)]: https://aws.amazon.com/msk/
[Apache Airflow]: https://airflow.apache.org/
[Apache Flink]: https://flink.apache.org/
[Apache Hop]: https://hop.apache.org/
[Apache Kafka]: https://kafka.apache.org/
[Apache Kafka on Azure]: https://azuremarketplace.microsoft.com/marketplace/consulting-services/canonical.0001-com-ubuntu-managed-kafka
[Astronomer]: https://www.astronomer.io/
[Azure Event Hubs for Apache Kafka]: https://learn.microsoft.com/en-us/azure/event-hubs/azure-event-hubs-kafka-overview
[Confluent Cloud]: https://www.confluent.io/confluent-cloud/
[CrateDB and Apache Airflow]: https://cratedb.com/integrations/cratedb-and-apache-airflow
[CrateDB and Apache Kafka]: https://cratedb.com/integrations/cratedb-and-kafka
[CrateDB and Kestra]: https://cratedb.com/integrations/cratedb-and-kestra
[CrateDB and Node-RED]: https://cratedb.com/integrations/cratedb-and-node-red
[dbt]: https://www.getdbt.com/
[dbt Cloud]: https://www.getdbt.com/product/dbt-cloud/
[Debezium]: https://debezium.io/
[DoubleCloud Managed Service for Apache Kafka]: https://double.cloud/services/managed-kafka/
[Flink managed by Confluent]: https://www.datanami.com/2023/05/17/confluents-new-cloud-capabilities-address-data-streaming-hurdles/
[FlowFuse]: https://flowfuse.com/
[FlowFuse Cloud]: https://app.flowforge.com/
[Immerok Cloud]: https://web.archive.org/web/20230602085618/https://www.immerok.io/product
[Introduction to FlowFuse]: https://flowfuse.com/webinars/2023/introduction-to-flowforge/
[Kestra]: https://kestra.io/
[Meltano]: https://meltano.com/
[Meltano Hub]: https://hub.meltano.com/
[Node-RED]: https://nodered.org/
[Overview about more managed Kafka offerings]: https://keen.io/blog/managed-apache-kafka-vs-diy/
[Singer]: https://www.singer.io/
[SQL Server Integration Services]: https://learn.microsoft.com/en-us/sql/integration-services/sql-server-integration-services
[SSIS]: https://en.wikipedia.org/wiki/SQL_Server_Integration_Services
[ssis-tasks]: https://learn.microsoft.com/en-us/sql/integration-services/control-flow/integration-services-tasks
[ssis-transformations]: https://learn.microsoft.com/en-us/sql/integration-services/data-flow/transformations/integration-services-transformations
