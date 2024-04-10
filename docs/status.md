(build-status)=

# Build Status

The build status of relevant drivers, applications, and integrations
for CrateDB, on one page.

<style>
table td, table td * {
  vertical-align: top;
}
th, td {
  padding-right: 1em;
  padding-left: 1em;
}
/*
In `crate-docs-theme`, `src/crate/theme/rtd/crate/static/css/custom.css`
defines a style we don't want to apply here, specifically on `connect/index`.
*/
.wrapper-content-right .section img {
  margin-bottom: unset !important;
}
</style>


## Integrations

End-to-end QA integration tests against CrateDB Nightly,
on behalf of [cratedb-examples].

<table>
<tbody>

<tr>
<td>
<b>Application</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/application-apache-kafka-flink.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/application-apache-kafka-flink.yml?label=Apache Kafka, Apache Flink" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/application-apache-superset.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/application-apache-superset.yml?label=Apache Superset" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Dataframe</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/dataframe-dask.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/dataframe-dask.yml?label=Dask" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/dataframe-pandas.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/dataframe-pandas.yml?label=pandas" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Language</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-npgsql.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-npgsql.yml?label=npgsql" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-java-jooq.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-java-jooq.yml?label=Java jOOQ" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-java-maven.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-java-maven.yml?label=Java JDBC" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-php-amphp.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-php-amphp.yml?label=PHP AMPHP" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-php-pdo.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-php-pdo.yml?label=PHP PDO" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-python-sqlalchemy.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-python-sqlalchemy.yml?label=Python SQLAlchemy" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-ruby.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-ruby.yml?label=Ruby" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Testing</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/testing-testcontainers-java.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/testing-testcontainers-java.yml?label=Testcontainers for Java" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Topic</b>
</td>
<td>
<div>
<b>Time Series</b>
<br>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/timeseries.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/timeseries.yml?label=Time%20Series" loading="lazy"></a>
</div>
<div>
<b>Machine Learning</b>
<br>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/ml-automl.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/ml-automl.yml?label=AutoML" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/ml-langchain.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/ml-langchain.yml?label=LangChain" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/ml-mlflow.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/ml-mlflow.yml?label=MLflow" loading="lazy"></a>
</div>
</td>
</tr>

</tbody>
</table>


## Applications

CI outcomes for a range of applications, frameworks, and libraries connecting
to CrateDB.

<table>
<tbody>

<tr>
<td>
<b>Framework</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-airflow-tutorial/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-airflow-tutorial/main.yml?label=Apache Airflow" loading="lazy"></a>
<a href="https://github.com/crate-workbench/cratedb-toolkit/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate-workbench/cratedb-toolkit/main.yml?label=CrateDB Toolkit" loading="lazy"></a>
<a href="https://github.com/crate-workbench/cratedb-toolkit/actions/workflows/influxdb.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate-workbench/cratedb-toolkit/influxdb.yml?label=Toolkit%2BInfluxDB" loading="lazy"></a>
<a href="https://github.com/crate-workbench/cratedb-toolkit/actions/workflows//mongodb.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate-workbench/cratedb-toolkit/mongodb.yml?label=Toolkit%2BMongoDB" loading="lazy"></a>
<a href="https://github.com/crate-workbench/mlflow-cratedb/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate-workbench/mlflow-cratedb/main.yml?label=MLflow for CrateDB" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Metrics</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-prometheus-adapter/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-prometheus-adapter/tests.yml?label=CrateDB Prometheus Adapter" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Operation</b>
</td>
<td>
<a href="https://github.com/crate/crate-operator/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-operator/main.yaml?label=CrateDB Kubernetes Operator" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>UI</b>
</td>
<td>
<a href="https://github.com/crate/crate-admin/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-admin/tests.yml?label=CrateDB Admin UI" loading="lazy"></a>
<a href="https://github.com/crate/crash/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crash/main.yml?label=Crash CLI" loading="lazy"></a>
<a href="https://github.com/crate/croud/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/croud/main.yml?label=Croud CLI" loading="lazy"></a>
</td>
</tr>

</tbody>
</table>


## Drivers

CI outcomes for a range of client drivers connecting your applications to CrateDB.

### CrateDB
Drivers and dialects maintained by Crate.io.

<a href="https://github.com/crate/crate-python/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-python/tests.yml?label=crate-python" loading="lazy"></a>
<a href="https://github.com/crate/crate-pdo/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-pdo/tests.yml?label=crate-pdo" loading="lazy"></a>
<a href="https://github.com/crate/crate-dbal/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-dbal/tests.yml?label=crate-dbal" loading="lazy"></a>
<a href="https://github.com/crate/crate_ruby/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate_ruby/tests.yml?label=crate_ruby" loading="lazy"></a>
<a href="https://github.com/crate/activerecord-crate-adapter/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/activerecord-crate-adapter/tests.yml?label=activerecord-crate-adapter" loading="lazy"></a>

### PostgreSQL
Standard PostgreSQL drivers for different languages.

<a href="https://github.com/pgjdbc/pgjdbc/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/pgjdbc/pgjdbc/main.yml?label=pgjdbc" loading="lazy"></a>
<a href="https://github.com/npgsql/npgsql/actions/workflows/build.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/npgsql/npgsql/build.yml?label=npgsql" loading="lazy"></a>
<a href="https://github.com/psycopg/psycopg2/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/psycopg/psycopg2/tests.yml?label=psycopg2" loading="lazy"></a>
<a href="https://github.com/psycopg/psycopg/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/psycopg/psycopg/tests.yml?label=psycopg3" loading="lazy"></a>
<a href="https://github.com/MagicStack/asyncpg/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/MagicStack/asyncpg/tests.yml?label=asyncpg" loading="lazy"></a>
<a href="https://github.com/brianc/node-postgres/actions/workflows/ci.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/brianc/node-postgres/ci.yml?label=node-postgres" loading="lazy"></a>


```{note}
Please note that the designated status of drivers maintained by community
authors and other maintainers reflect the build status of the development
head. It does not mean integration with GA releases isn't stable. This is
reflected within the topmost section of this page.
```


[cratedb-examples]: https://github.com/crate/cratedb-examples
