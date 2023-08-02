(ide)=

# Using database IDEs with CrateDB

Mostly through its PostgreSQL interface, CrateDB supports working with popular
database IDE (Integrated Development Environment) applications.


## DBeaver

```{div}
:style: "float: right"
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/DBeaver_logo.svg/512px-DBeaver_logo.svg.png){w=120px}](https://dbeaver.io/)
```

[DBeaver] is a multipurpose database tool for developers and database administrators.
Because CrateDB provides a JDBC driver, you can access CrateDB with any client tool that supports JDBC drivers.

Connecting DBeaver to CrateDB uses the legacy PostgreSQL JDBC Driver, the blog
article [Blog: Use CrateDB With DBeaver] explains how it works. 

![image](https://19927462.fs1.hubspotusercontent-na1.net/hub/19927462/hubfs/Screen-Shot-2019-04-05-at-17.13.21.png?width=1600&name=CrateDB-DBeaver.png){h=200px}
![image](https://19927462.fs1.hubspotusercontent-na1.net/hub/19927462/hubfs/Screen-Shot-2019-04-05-at-17.15.13.png?width=1600&name=Screen-Shot-2019-04-05-at-17.15.13.png){h=200px}


## pgAdmin

```{div}
:style: "float: right"
[![](https://www.pgadmin.org/static/docs/pgadmin4-7.5-docs/_images/logo-right-128.png){w=120px}](https://www.pgadmin.org/)
```

[pgAdmin] is the most popular and feature rich Open Source administration and
development platform for PostgreSQL.

Connecting pgAdmin to CrateDB works natively and without further ado.

![image](https://www.pgadmin.org/static/COMPILED/assets/img/screenshots/pgadmin4-welcome-light.png){h=200px}
![image](https://www.pgadmin.org/static/COMPILED/assets/img/screenshots/pgadmin4-viewdata.png){h=200px}


[Blog: Use CrateDB With DataGrip]: https://crate.io/blog/use-cratedb-with-datagrip-an-advanced-database-ide
[Blog: Use CrateDB With DBeaver]: https://crate.io/blog/cratedb-dbeaver
[DBeaver]: https://dbeaver.io/
[pgAdmin]: https://www.pgadmin.org/
