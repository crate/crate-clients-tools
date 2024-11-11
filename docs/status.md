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
on behalf of [cratedb-examples] and [academy-fundamentals-course].

<table>
<tbody>

<tr>
<td>
<b>Application</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/application-apache-kafka-flink.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/application-apache-kafka-flink.yml?branch=main&label=Apache Kafka, Apache Flink" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/application-apache-superset.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/application-apache-superset.yml?branch=main&label=Apache Superset" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Dataframe</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/dataframe-dask.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/dataframe-dask.yml?branch=main&label=Dask" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/dataframe-pandas.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/dataframe-pandas.yml?branch=main&label=pandas" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Framework</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/framework-dbt.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/framework-dbt.yml?branch=main&label=dbt" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/framework-gradio.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/framework-gradio.yml?branch=main&label=Gradio" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/framework-streamlit.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/framework-streamlit.yml?branch=main&label=Streamlit" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Language</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-npgsql.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-npgsql.yml?branch=main&label=npgsql" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-java-jooq.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-java-jooq.yml?branch=main&label=Java jOOQ" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-java-maven.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-java-maven.yml?branch=main&label=Java JDBC" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-php-amphp.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-php-amphp.yml?branch=main&label=PHP AMPHP" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-php-pdo.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-php-pdo.yml?branch=main&label=PHP PDO" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-python-dbapi.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-python-dbapi.yml?branch=main&label=Python DB API" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-python-sqlalchemy.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-python-sqlalchemy.yml?branch=main&label=Python SQLAlchemy" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-ruby.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-ruby.yml?branch=main&label=Ruby" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Testing</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/testing-testcontainers-java.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/testing-testcontainers-java.yml?branch=main&label=Testcontainers for Java" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/testing-testcontainers-python.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/testing-testcontainers-python.yml?branch=main&label=Testcontainers for Python" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/testing-native-python.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/testing-native-python.yml?branch=main&label=Native testing for Python" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Topic</b>
</td>
<td>
<div>
<b>Academy</b>
<br>
<a href="https://github.com/crate/academy-fundamentals-course/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/academy-fundamentals-course/tests.yml?branch=main&label=Fundamentals Course" loading="lazy"></a>
</div>
<div>
<b>Machine Learning</b>
<br>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/ml-automl.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/ml-automl.yml?branch=main&label=AutoML" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/ml-langchain.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/ml-langchain.yml?branch=main&label=LangChain" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/ml-llamaindex.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/ml-llamaindex.yml?branch=main&label=LlamaIndex" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/ml-mlflow.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/ml-mlflow.yml?branch=main&label=MLflow" loading="lazy"></a>
</div>
<div>
<b>Time Series</b>
<br>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/timeseries.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/timeseries.yml?branch=main&label=Time%20Series" loading="lazy"></a>
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
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-airflow-tutorial/main.yml?branch=main&label=Apache Airflow" loading="lazy"></a>
<a href="https://github.com/crate/mlflow-cratedb/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/mlflow-cratedb/main.yml?branch=main&label=MLflow for CrateDB" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Metrics</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-prometheus-adapter/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-prometheus-adapter/tests.yml?branch=main&label=CrateDB Prometheus Adapter" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Operation</b>
</td>
<td>
<a href="https://github.com/crate/crate-operator/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-operator/main.yaml?branch=master&label=CrateDB Kubernetes Operator" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>UI</b>
</td>
<td>
<a href="https://github.com/crate/crate-admin/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-admin/tests.yml?branch=main&label=CrateDB Admin UI" loading="lazy"></a>
<a href="https://github.com/crate/crash/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crash/main.yml?branch=master&label=Crash CLI" loading="lazy"></a>
<a href="https://github.com/crate/croud/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/croud/main.yml?branch=master&label=Croud CLI" loading="lazy"></a>
</td>
</tr>

</tbody>
</table>


## Drivers

CI outcomes for a range of client drivers connecting your applications to CrateDB.

### CrateDB
Adapters, drivers, dialects, and support utilities maintained by CrateDB.

<a href="https://github.com/crate/crate-python/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-python/tests.yml?branch=main&label=crate-python" loading="lazy"></a>
<a href="https://github.com/crate/sqlalchemy-cratedb/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/sqlalchemy-cratedb/tests.yml?branch=main&label=sqlalchemy-cratedb" loading="lazy"></a>
<a href="https://github.com/crate/micropython-cratedb/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/micropython-cratedb/tests.yml?branch=main&label=micropython-cratedb" loading="lazy"></a>
<a href="https://github.com/crate/pytest-cratedb/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/pytest-cratedb/tests.yml?branch=master&label=pytest-cratedb" loading="lazy"></a>
<br>
<a href="https://github.com/crate/cratedb-sqlparse/actions/workflows/python.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-sqlparse/python.yml?branch=main&label=cratedb-sqlparse (python)" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-sqlparse/actions/workflows/javascript.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-sqlparse/javascript.yml?branch=main&label=cratedb-sqlparse (javascript)" loading="lazy"></a>
<br>
<a href="https://github.com/crate/cratedb-toolkit/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-toolkit/main.yml?branch=main&label=CrateDB Toolkit" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-toolkit/actions/workflows/dynamodb.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-toolkit/dynamodb.yml?branch=main&label=CTK%2BDynamoDB" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-toolkit/actions/workflows/influxdb.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-toolkit/influxdb.yml?branch=main&label=CTK%2BInfluxDB" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-toolkit/actions/workflows/mongodb.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-toolkit/mongodb.yml?branch=main&label=CTK%2BMongoDB" loading="lazy"></a>
<br>
<a href="https://github.com/crate/crate-pdo/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-pdo/tests.yml?branch=main&label=crate-pdo" loading="lazy"></a>
<a href="https://github.com/crate/crate-dbal/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-dbal/tests.yml?branch=main&label=crate-dbal" loading="lazy"></a>
<a href="https://github.com/crate/crate_ruby/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate_ruby/tests.yml?branch=main&label=crate_ruby" loading="lazy"></a>
<a href="https://github.com/crate/activerecord-crate-adapter/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/activerecord-crate-adapter/tests.yml?branch=main&label=activerecord-crate-adapter" loading="lazy"></a>

<br>
<br>

### PostgreSQL
Standard PostgreSQL drivers for different languages.

<a href="https://github.com/pgjdbc/pgjdbc/actions/workflows/main.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/pgjdbc/pgjdbc/main.yml?branch=master&label=pgjdbc" loading="lazy"></a>
<a href="https://github.com/npgsql/npgsql/actions/workflows/build.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/npgsql/npgsql/build.yml?branch=main&label=npgsql" loading="lazy"></a>
<a href="https://github.com/psycopg/psycopg2/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/psycopg/psycopg2/tests.yml?branch=master&label=psycopg2" loading="lazy"></a>
<a href="https://github.com/psycopg/psycopg/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/psycopg/psycopg/tests.yml?branch=master&label=psycopg3" loading="lazy"></a>
<a href="https://github.com/MagicStack/asyncpg/actions/workflows/tests.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/MagicStack/asyncpg/tests.yml?branch=master&label=asyncpg" loading="lazy"></a>
<a href="https://github.com/brianc/node-postgres/actions/workflows/ci.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/brianc/node-postgres/ci.yml?branch=master&label=node-postgres" loading="lazy"></a>

<br><br>


```{note}
Please note that the designated status of drivers maintained by community
authors and other maintainers reflect the build status of the development
head. It does not mean integration with GA releases isn't stable. This is
reflected within the topmost section of this page.
```


[academy-fundamentals-course]: https://github.com/crate/academy-fundamentals-course
[cratedb-examples]: https://github.com/crate/cratedb-examples
