(bi)=
(bi-tools)=
# Business Analytics and Intelligence with CrateDB

This documentation section lists business analytics applications
and frameworks, which can be used together with CrateDB.


(powerbi)=
## Microsoft Power BI

```{div}
:style: "float: right"
[![](https://upload.wikimedia.org/wikipedia/en/thumb/2/20/Power_BI_logo.svg/192px-Power_BI_logo.svg.png?20200923233425){w=180px}](https://powerbi.microsoft.com/en-us/desktop/)
```

[Power BI Desktop] is a powerful business intelligence tool that provides a set of
data analytics and visualizations. Using Power BI Desktop, users can create reports
and dashboards from large datasets.

For connecting to CrateDB with Power BI, you can use the [Power Query PostgreSQL connector].
Earlier versions used the [PostgreSQL ODBC driver]. [](inv:guide#powerbi-desktop) walks
you through the process of configuring that correctly.

[Power BI Service] is an online data analysis and visualization tool, making it
possible to publish your dashboards, in order to share them with others.
[](inv:guide#powerbi-service) has a corresponding tutorial.

![](https://cratedb.com/docs/crate/howtos/en/latest/_images/powerbi-table-navigator.png){h=160px}
![](https://cratedb.com/docs/crate/howtos/en/latest/_images/powerbi-pie-chart.png){h=160px}
![](https://cratedb.com/docs/crate/howtos/en/latest/_images/powerbi-publish-success.png){h=160px}

```{seealso}
[CrateDB and Power BI]
```


## Rill

```{div}
:style: "float: right; margin-left: 0.5em"
[![](https://github.com/rilldata/rill/blob/main/docs/static/img/rill-logo-dark.svg){w=180px}](https://www.rilldata.com/)
```

[Rill] is an open-source operational BI framework for effortlessly transforming
data sets into powerful, opinionated dashboards using SQL.

Unlike most BI tools, Rill comes with its own embedded in-memory database. Data
and compute are co-located, and queries return in milliseconds. So you can pivot,
slice, and drill-down into your data instantly.

Rill takes a modern approach to Business Intelligence (BI), which is starting to
leverage software engineering principles by implementing the concept of BI as
code.

This methodology allows for versioning and tracking, thus improving collaboration
on BI projects using code, which is more efficient and scalable than traditional
BI tools, also breaking down information and knowledge barriers.

**Rill's design principles**

- **Feels good to use** – powered by Sveltekit & DuckDB = conversation-fast, not
  wait-ten-seconds-for-result-set fast
- **Works with your local and remote datasets** – imports and exports Parquet and
  CSV (s3, gcs, https, local)
- **No more data analysis "side-quests"** – helps you build intuition about your
  dataset through automatic profiling
- **No "run query" button required** – responds to each keystroke by re-profiling
  the resulting dataset
- **Radically simple interactive dashboards** – thoughtful, opinionated, interactive
  dashboard defaults to help you quickly derive insights from your data
- **Dashboards as code** – each step from data to dashboard has versioning, Git
  sharing, and easy project rehydration

![](https://global.discourse-cdn.com/business7/uploads/crate/original/2X/a/aff8ddc9f63840a330e8bf735de3cfd1179ef354.png){h=200px}
![](https://global.discourse-cdn.com/business7/uploads/crate/original/2X/0/050718f5eb81abfc06db1f040984a53bfd95e296.png){h=200px}


(tableau)=
## Tableau

```{div}
:style: "float: right"
[![](https://upload.wikimedia.org/wikipedia/en/thumb/0/06/Tableau_logo.svg/500px-Tableau_logo.svg.png?20200509180027){w=180px}](https://www.tableau.com/)
```

[Tableau] is a visual business intelligence and analytics software platform. It expresses
data by translating drag-and-drop actions into data queries through an intuitive interface.

[Connecting to CrateDB from Tableau with JDBC] and [Using CrateDB with Tableau] will
guide you through the process of setting it up correctly with CrateDB.

![](https://cratedb.com/hs-fs/hubfs/08-index.png?width=1536&name=08-index.png){h=200px}

```{seealso}
[CrateDB and Tableau]
```


[Connecting to CrateDB from Tableau with JDBC]: https://cratedb.com/blog/connecting-to-cratedb-from-tableau-with-jdbc
[CrateDB and Tableau]: https://cratedb.com/integrations/cratedb-and-tableau
[CrateDB and Power BI]: https://cratedb.com/integrations/cratedb-and-power-bi
[PostgreSQL ODBC driver]: https://odbc.postgresql.org/
[Power BI Desktop]: https://powerbi.microsoft.com/en-us/desktop/
[Power BI Service]: https://powerbi.microsoft.com/en-us/
[Power Query PostgreSQL connector]: https://learn.microsoft.com/en-us/power-query/connectors/postgresql
[Rill]: https://www.rilldata.com/
[Tableau]: https://www.tableau.com/
[Using CrateDB with Tableau]: https://community.cratedb.com/t/using-cratedb-with-tableau/1192
