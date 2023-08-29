# Backlog


## Iteration +1
- [ ] Add item about Admin UI
- [ ] Add item about `psycopg3`
- [ ] Connect: Add more properties, like `schema`
- [ ] ETL: There is pandas, but not Dask/Coiled
- [ ] Add Prometheus
  - https://crate.io/integrations/cratedb-and-prometheus
  - https://community.crate.io/t/storing-long-term-metrics-with-prometheus-in-cratedb/1012
  - https://github.com/crate/cratedb-prometheus-adapter

## Iteration +2
- [ ] Refer to more artefacts/resources
  - Prometheus (Server Metrics/Monitoring)
  - Terraform (Administration)
- [ ] Add section about testing frameworks
- [ ] Add section "highlights", or "awesome", bundling corresponding resources.
  - https://community.crate.io/t/how-we-scaled-ingestion-to-one-million-rows-per-second/1069
- [ ] Add [HTTPie Desktop]
  Screenshot: https://github.com/crate/crate-clients-tools/assets/453543/9f724518-ee83-43ac-9ea1-7be63e7c9805

## Iteration +3
- [ ] Drivers: Outline multiple dimensions
  - protocol: http vs. pg
  - maintained/unmaintained
  - recommended
- [ ] Drivers: Layout overview list/table differently, to better convey more detailed
  information per item. Maybe use [Info Card].

## Evaluate

- Via https://getsqlpad.com/en/introduction/#alternatives
  - [Querybook](https://www.querybook.org/) (open source)
  - [Superset](https://github.com/apache/superset) (open source) / [Preset](https://preset.io/) (company)
  - [Chartbrew](https://github.com/chartbrew/chartbrew) (open source) / [Chartbrew](https://chartbrew.com/) (company)
  - [Lightdash](https://github.com/lightdash/lightdash) (open source) / [Lightdash](https://www.lightdash.com/) (company)
  - [CloudBeaver](https://github.com/dbeaver/cloudbeaver) (open source)
  - [Awesome DB tools GUIs](https://github.com/mgramin/awesome-db-tools#gui)

- Via https://github.com/crate/crate-clients-tools/issues
  - [Looker](https://cloud.google.com/looker)
  - [Metabase](https://github.com/metabase/metabase)
  - [pgweb](https://sosedoff.github.io/pgweb/)
  - [Redash](https://github.com/getredash/redash)
  - [usql](https://github.com/xo/usql)

- Re-evaluate
  - Add [DataGrip]
  - Add [pgAdmin]


## Done
- [x] CLI: Dedicated section per program, with code examples
- [x] Connect: Improve "Configure" section about connection properties
- [x] .NET driver got lost
- [x] Remove DataGrip and pgAdmin again, they do not work


[DataGrip]: https://www.jetbrains.com/datagrip/
[HTTPie Desktop]: https://httpie.io/desktop
[Info Card]: https://sphinx-design-elements.readthedocs.io/en/latest/infocard.html
[pgAdmin]: https://www.pgadmin.org/
