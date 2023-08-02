(ide)=

# Using database IDEs with CrateDB

Mostly through its PostgreSQL interface, CrateDB supports working with popular
database IDE (Integrated Development Environment) applications.


## DataGrip

```{div}
:style: "float: right"
[![](https://blog.jetbrains.com/wp-content/uploads/2019/01/datagrip_icon.svg){w=120px}](https://www.jetbrains.com/datagrip/)
```

[DataGrip] is a cross-platform database IDE that is tailored to suit the specific needs
of professional SQL developers.

Connecting DataGrip to CrateDB uses the vanilla PostgreSQL JDBC Driver,
the blog article [Blog: Use CrateDB With DataGrip] explains how it works.

![image](https://19927462.fs1.hubspotusercontent-na1.net/hub/19927462/hubfs/13-Datagrip.png?width=1536&name=CrateDB-DataGrip.png){h=200px}
![image](https://www.pgadmin.org/static/COMPILED/assets/img/screenshots/pgadmin4-welcome-light.png){h=200px}

:::{caution}
Please note while the query console works well, you will notice that many UI
actions do not work yet. We are tracking corresponding gaps at [Tool: DataGrip],
and appreciate any contributions to improve the situation.
:::


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



[Blog: Use CrateDB With DataGrip]: https://cratedb.com/blog/use-cratedb-with-datagrip-an-advanced-database-ide
[Blog: Use CrateDB With DBeaver]: https://cratedb.com/blog/cratedb-dbeaver
[DataGrip]: https://www.jetbrains.com/datagrip/
[DBeaver]: https://dbeaver.io/
[Tool: DataGrip]: https://github.com/crate/crate/labels/tool%3A%20DataGrip
