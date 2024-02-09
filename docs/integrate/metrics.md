(metrics)=
# Processing monitoring metrics with CrateDB

Storing metrics data for the long term is a common need in systems monitoring
scenarios. CrateDB offers corresponding integration adapters.


(telegraf)=
## Telegraf

```{div}
:style: "float: right"
[![](https://raw.githubusercontent.com/influxdata/branding/master/docs/img/logo-usage/logo-symbol-black.svg){w=180px}](https://www.influxdata.com/time-series-platform/telegraf/)
```

[Telegraf] is a leading open source server agent to help you collect metrics
from your stacks, sensors, and systems. More than 200 adapters to connect
to other systems leaves nothing to be desired.

Telegraf is a server-based agent for collecting and sending all metrics and
events from databases, systems, and IoT sensors. Telegraf is written in Go
and compiles into a single binary with no external dependencies, and requires
a very minimal memory footprint.

### Scope

- **IoT sensors**: Collect critical stateful data (pressure levels, temperature
  levels, etc.) with popular protocols like MQTT, ModBus, OPC-UA, and Kafka.

- **DevOps Tools and frameworks**: Gather metrics from cloud platforms,
  containers, and orchestrators like GitHub, Kubernetes, CloudWatch, Prometheus,
  and more.

- **System telemetry**: Metrics from system telemetry like iptables, Netstat,
  NGINX, and HAProxy help provide a full stack view of your apps.

### Resources

- [Use CrateDB With Telegraf, an Agent for Collecting & Reporting Metrics]

![](https://www.influxdata.com/wp-content/uploads/Main-Diagram_06.01.2022v1.png){h=200px}

```{seealso}
[CrateDB and Telegraf]
```

```{div}
:style: "clear: both"
```


[CrateDB and Telegraf]: https://crate.io/integrations/cratedb-and-telegraf
[Telegraf]: https://www.influxdata.com/time-series-platform/telegraf/
[Use CrateDB With Telegraf, an Agent for Collecting & Reporting Metrics]: https://crate.io/blog/use-cratedb-with-telegraf-an-agent-for-collecting-reporting-metrics
