## Setup steps:

1) To run kafka, zookeeper, influxdb, grafana, and the metrics service, run the following command: 
```
docker-compose up -d
```

2) Run the telegraf agent with the following command:
```
telegraf --config ~/workspace/metrics-service/telegraf.conf
```

3) To bring down the services, run the following command:
```
docker-compose down
```

## Important notes:
1) Kafka -> InfluxDB
```
https://www.influxdata.com/blog/getting-started-apache-kafka-influxdb/
```
2) InfluxDB -> Grafana
```
https://www.influxdata.com/blog/getting-started-influxdb-grafana/
```
3) InfluxDB query
```sql
from(bucket: "sensor_data")
  |> range(start: 2016-01-01T00:00:00Z, stop: 2026-01-31T00:00:00Z)
  |> aggregateWindow(every: 1m, fn: mean, createEmpty: false)
  |> yield(name: "mean")
```
