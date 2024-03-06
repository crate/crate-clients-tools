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

![](https://crate.io/docs/crate/howtos/en/latest/_images/powerbi-table-navigator.png){h=160px}
![](https://crate.io/docs/crate/howtos/en/latest/_images/powerbi-pie-chart.png){h=160px}
![](https://crate.io/docs/crate/howtos/en/latest/_images/powerbi-publish-success.png){h=160px}

```{seealso}
[CrateDB and Power BI]
```


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

![](https://crate.io/hs-fs/hubfs/08-index.png?width=1536&name=08-index.png){h=200px}

```{seealso}
[CrateDB and Tableau]
```


[Connecting to CrateDB from Tableau with JDBC]: https://crate.io/blog/connecting-to-cratedb-from-tableau-with-jdbc
[CrateDB and Tableau]: https://crate.io/integrations/cratedb-and-tableau
[CrateDB and Power BI]: https://crate.io/integrations/cratedb-and-power-bi
[PostgreSQL ODBC driver]: https://odbc.postgresql.org/
[Power BI Desktop]: https://powerbi.microsoft.com/en-us/desktop/
[Power BI Service]: https://powerbi.microsoft.com/en-us/
[Power Query PostgreSQL connector]: https://learn.microsoft.com/en-us/power-query/connectors/postgresql
[Tableau]: https://www.tableau.com/
[Using CrateDB with Tableau]: https://community.crate.io/t/using-cratedb-with-tableau/1192
