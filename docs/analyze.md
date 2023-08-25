(bi-tools)=
(analyze)=
# Analytics with CrateDB

This documentation section enumerates analytics applications and frameworks for
analyzing data in CrateDB.


## Business analytics with Microsoft Power BI

```{div}
:style: "float: right"
[![](https://upload.wikimedia.org/wikipedia/en/thumb/2/20/Power_BI_logo.svg/192px-Power_BI_logo.svg.png?20200923233425){w=180px}](https://powerbi.microsoft.com/en-us/desktop/)
```

[Power BI Desktop] is a powerful business intelligence tool that provides a set of
data analytics and visualizations. Using Power BI Desktop, users can create reports
and dashboards from large datasets.

For connecting to CrateDB with Power BI, you can use the [Power Query PostgreSQL connector].
Earlier versions used the [PostgreSQL ODBC driver]. [](#cratedb-powerbi-desktop) walks
you through the process of configuring that correctly.

The [Power BI Service] is an online data analysis and visualization tool, making it
possible to publish your dashboards, in order to share them with others.
[](#cratedb-powerbi-service) has a corresponding tutorial.

![](https://crate.io/docs/crate/howtos/en/latest/_images/powerbi-table-navigator.png){h=160px}
![](https://crate.io/docs/crate/howtos/en/latest/_images/powerbi-pie-chart.png){h=160px}
![](https://crate.io/docs/crate/howtos/en/latest/_images/powerbi-publish-success.png){h=160px}

```{seealso}
[CrateDB and Power BI]
```


## Business intelligence with Tableau

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


## Data analysis with pandas and scikit-learn 

```{div}
:style: "float: right"
[![](https://pandas.pydata.org/static/img/pandas.svg){w=180px}](https://pandas.pydata.org/)
<br>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/240px-Scikit_learn_logo_small.svg.png){w=180px}](https://scikit-learn.org/)
<br>
[![](https://jupyter.org/assets/logos/rectanglelogo-greytext-orangebody-greymoons.svg){w=180px}](https://jupyter.org/)
```


Using [pandas] and [scikit-learn] to run a regression analysis within a [Jupyter Notebook].

- [Machine Learning and CrateDB: An introduction]
- [Machine Learning and CrateDB: Getting Started With Jupyter]
- [Machine Learning and CrateDB: Experiment Design & Linear Regression]

More resources:

- [Automating financial data collection and storage in CrateDB with Python and pandas 2.0.0]
- [From data storage to data analysis: Tutorial on CrateDB and pandas]


## Machine Learning and CrateDB

Using pandas, NumPy, Matplotlib, Merlion, and MLFlow, to analyze timeseries anomalies.

- [Running Time Series Models in Production using CrateDB]


[Automating financial data collection and storage in CrateDB with Python and pandas 2.0.0]: https://community.crate.io/t/automating-financial-data-collection-and-storage-in-cratedb-with-python-and-pandas-2-0-0/916
[Connecting to CrateDB from Tableau with JDBC]: https://crate.io/blog/connecting-to-cratedb-from-tableau-with-jdbc
[CrateDB and Tableau]: https://crate.io/integrations/cratedb-and-tableau
[CrateDB and Power BI]: https://crate.io/integrations/cratedb-and-power-bi
[From data storage to data analysis: Tutorial on CrateDB and pandas]: https://community.crate.io/t/from-data-storage-to-data-analysis-tutorial-on-cratedb-and-pandas/1440/1
[Jupyter Notebook]: https://jupyter.org/
[Machine Learning and CrateDB: An introduction]: https://crate.io/blog/machine-learning-and-cratedb-part-one
[Machine Learning and CrateDB: Getting Started With Jupyter]: https://crate.io/blog/machine-learning-cratedb-jupyter
[Machine Learning and CrateDB: Experiment Design & Linear Regression]: https://crate.io/blog/machine-learning-and-cratedb-part-three-experiment-design-and-linear-regression
[pandas]: https://pandas.pydata.org/
[PostgreSQL ODBC driver]: https://odbc.postgresql.org/
[Power BI Desktop]: https://powerbi.microsoft.com/en-us/desktop/
[Power BI Service]: https://powerbi.microsoft.com/en-us/
[Power Query PostgreSQL connector]: https://learn.microsoft.com/en-us/power-query/connectors/postgresql
[Running Time Series Models in Production using CrateDB]: https://github.com/crate/ml-sandbox/blob/main/timeseries-blog/timeseries-blog.md
[scikit-learn]: https://scikit-learn.org/
[Tableau]: https://www.tableau.com/
[Using CrateDB with Tableau]: https://community.crate.io/t/using-cratedb-with-tableau/1192
