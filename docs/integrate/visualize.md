(visualize)=
# Visualize data in CrateDB

Dashboard and other data visualization applications and toolkits for
visualizing data stored inside CrateDB, mostly dashboarding.


::::{card} {material-outlined}`lightbulb;2em` Tutorials
:margin: 0 0 5 5
:shadow: md
:link: guide:visualization
:link-type: ref

Guidelines about data analysis and visualization with CrateDB.
+++
{tag}`DataViz` {tag}`EDA` {tag}`BI`
::::


(apache-superset)=
(preset)=
(superset)=
## Apache Superset / Preset

```{div}
:style: "float: right"
[![](https://cratedb.com/hs-fs/hubfs/Apache-Superset-Logo-392x140@2x.png?width=604&height=216&name=Apache-Superset-Logo-392x140@2x.png){w=180px}](https://superset.apache.org/)

[![](https://github.com/crate/crate-clients-tools/assets/453543/9d07da87-8aff-4569-bf2a-0a16bf89f4bc){w=180px}](https://preset.io/)
```

[Apache Superset] is an open-source modern data exploration and visualization
platform, written in Python.

[Preset] offers a managed, elevated, and enterprise-grade SaaS for open-source
Apache Superset.

![](https://superset.apache.org/img/hero-screenshot.jpg){h=200px}
![](https://github.com/crate/crate-clients-tools/assets/453543/0f8f7bd8-2e30-4aca-bcf3-61fbc81da855){h=200px}

```{seealso}
[CrateDB and Superset]
```

:::{dropdown} **Managed Superset**
```{div}
:style: "float: right"
[![](https://github.com/crate/crate-clients-tools/assets/453543/9d07da87-8aff-4569-bf2a-0a16bf89f4bc){w=180px}](https://preset.io/)
```

[Preset Cloud] is a fully-managed, open-source BI for the modern data stack,
based on Apache Superset.

- **Hassle-free setup:** There is no need to install or maintain software with Preset.
  Get the latest version of Superset in a secure, reliable, and scalable SaaS experience.
- **Up-to-date Superset, always:** Access all the latest features of Superset
  released and thoroughly tested every two weeks.
- **One-click to deploy multiple workspaces:** Give each team in your organization
  a separate Superset workspace to protect sensitive data.
- **Control user roles and access:** Easily assign roles and fine-tune data access
  using RBAC and row-level security (RLS).

```{div}
:style: "clear: both"
```
:::


## Cluvio

```{div}
:style: "float: right"
[![cluvio-logo-full_color-on_dark.svg ](https://github.com/crate/crate-clients-tools/assets/453543/cac142ef-412a-4a67-a63f-bf9d1ce92c84){w=180px}](https://www.cluvio.com/)
```

[Cluvio] is a programmable and interactive dashboarding platform — your analytics
cockpit. Run queries, filter your results, choose the most vivid way to display them,
and share them with your colleagues and partners without efforts.

Cluvio dashboards are interactive, so you can easily change aggregation, select a
specific timerange or filter dashboards by any individual attribute of your data.

Use SQL and R to analyze your data and create beautiful, interactive dashboards for
your entire company in few minutes.

![custom-filters.png](https://github.com/crate/crate-clients-tools/assets/453543/49ca6a35-239e-4915-951c-db6649fd35a4){h=200px}
![report-creator.png](https://github.com/crate/crate-clients-tools/assets/453543/844a5ffd-0b92-4c77-8cdd-0b5cc5b392b1){h=200px}


## Explo

```{div}
:style: "float: right"
[![](https://uploads-ssl.webflow.com/62f681c18d50329187681754/62f681c18d5032d0bd681785_logo.svg){w=180px}](https://www.explo.co/)
```

[Explo] is a software platform for personalized and real-time customer facing
analytics. Organizations use Explo’s platform services "Explore", "Host", "Report
builder", and "Email", to activate and share data with their customers.

[Explo Explore] integrates directly into your web portal or application and provides
your customers with a complete self-service data toolkit, which can also be used to
run white-labeled data portals.

```{div}
:style: "clear: both"
```

![](https://cratedb.com/hs-fs/hubfs/Screenshot%202023-07-21%20at%2013.17.45.png?width=2948&height=2312&name=Screenshot%202023-07-21%20at%2013.17.45.png){h=200px}
![](https://cratedb.com/hs-fs/hubfs/Screenshot%202023-07-21%20at%2013.24.01.png?width=2932&height=1716&name=Screenshot%202023-07-21%20at%2013.24.01.png){h=200px}


## Grafana

```{div}
:style: "float: right"
[![](https://cratedb.com/hs-fs/hubfs/Imported_Blog_Media/grafana-logo-1-520x126.png?width=1040&height=252&name=grafana-logo-1-520x126.png){w=180px}](https://grafana.com/grafana/)
```

[Grafana OSS] is the leading open-source metrics visualization tool that helps you
build real-time dashboards, graphs, and many other sorts of data visualizations.
[Grafana Cloud] is a fully-managed service offered by [Grafana Labs].

Grafana complements CrateDB in monitoring and visualizing large volumes of machine
data in real-time.

Connecting to a CrateDB cluster will use the Grafana PostgreSQL data source adapter.
The following tutorials outline how to configure Grafana to connect to CrateDB, and
how to run a database query. 

![image](https://github.com/crate/cratedb-guide/raw/a9c8c03384/docs/_assets/img/integrations/grafana/grafana-connection.png){h=200px}
![image](https://github.com/crate/cratedb-guide/raw/a9c8c03384/docs/_assets/img/integrations/grafana/grafana-panel1.png){h=200px}

```{seealso}
[CrateDB and Grafana]
```

:::{dropdown} **Managed Grafana**
```{div}
:style: "float: right"
[![](https://cratedb.com/hs-fs/hubfs/Imported_Blog_Media/grafana-logo-1-520x126.png?width=1040&height=252&name=grafana-logo-1-520x126.png){w=180px}](https://grafana.com/grafana/)
```

Get Grafana fully managed with [Grafana Cloud].

- Offered as a fully managed service, Grafana Cloud is the fastest way to adopt
  Grafana and includes a scalable, managed backend for metrics, logs, and traces.
- Managed and administered by Grafana Labs with free and paid options for
  individuals, teams, and large enterprises.
- Includes a robust free tier with access to 10k metrics, 50GB logs, 50GB traces,
  50GB profiles, and 500VUh of k6 testing for 3 users.

```{div}
:style: "clear: both"
```
:::


## Metabase

```{div}
:style: "float: right"
[![](https://www.metabase.com/images/logo.svg){w=180px}](https://www.metabase.com/cloud/)
```

[Metabase] is the ultimate data analysis and visualization tool that unlocks the full
potential of your data. Build for data and made for everyone, Metabase can be leveraged
with no SQL required.

Fast analytics with the friendly UX and integrated tooling to let your company explore
data on their own.

![image](https://github.com/crate/cratedb-guide/raw/a9c8c03384/docs/_assets/img/integrations/metabase/metabase-question.png){h=140px}
![image](https://github.com/crate/cratedb-guide/raw/a9c8c03384/docs/_assets/img/integrations/metabase/metabase-dashboard.png){h=140px}

```{seealso}
[CrateDB and Metabase]
```

:::{dropdown} **Managed Metabase**
```{div}
:style: "float: right"
[![](https://www.metabase.com/images/logo.svg){w=180px}](https://www.metabase.com/)
```

With [Metabase Cloud], you will get a fast, reliable, and secure deployment
with none of the work or hidden costs that come with self-hosting.

- **Save the time** needed for setup and maintenance of the platform, focusing only on the insights we can get from our data.
- **Trustworthy, production-grade deployment** by people who do this stuff for a living.
  With the infrastructure, specialists, and thousands of Metabases in our cloud, we've put a lot of thought and resources into optimizing hosting.
- **Upgrades:** Automatically upgrade to the current version, so you're always getting the latest and greatest of Metabase.
- **Backups:** The way they should be: there when you need them, out of sight and out of mind when you don't.
- **SMTP server:** Even your alerts and dashboard subscriptions covered with a preconfigured and managed SMTP server.


```{div}
:style: "clear: both"
```
:::


[Apache Superset]: https://superset.apache.org/
[Cluvio]: https://www.cluvio.com/
[CrateDB and Grafana]: https://cratedb.com/integrations/cratedb-and-grafana
[CrateDB and Superset]: https://cratedb.com/integrations/cratedb-and-apache-superset
[CrateDB and Metabase]: https://cratedb.com/integrations/cratedb-and-metabase
[Explo]: https://www.explo.co/
[Explo Explore]: https://www.explo.co/products/explore
[GeoViews]: https://geoviews.org/
[Grafana Cloud]: https://grafana.com/grafana/
[Grafana Labs]: https://grafana.com/about/team/
[Grafana OSS]: https://grafana.com/oss/grafana/
[Metabase]: https://www.metabase.com/
[Metabase Cloud]: https://www.metabase.com/cloud/
[Preset]: https://preset.io/
[Preset Cloud]: https://preset.io/product/
