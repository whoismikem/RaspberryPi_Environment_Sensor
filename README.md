# Physical World Sampler
Born form the need to sample the physical world for various purposes and applications.

## Components
* Raspberry Pi4 
* [ Waveshare BME280 Environmental Sensor ]: ( https://www.amazon.com/gp/product/B07P4CWGGK/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc= )

## Running

### BME280 Data Api
Basic flask app exposing the sensor data so it can be easly collected.
1. Change into the appropriate project directory.
`cd microAPI_bme280`

2. Build the container:
`docker build -t microapi_bme280:latest .`

3. Run the container in provliged mode giving the container access to more thing such as GPIO:
`docker run -d -p 5000:5000 --privileged microapi_bme280`

### Data Collector
Basic tool to collect the sensor data and deposit it in the influxDB time series table.
1. Change intp the appropriate project directory:
cd `microDB_store`

2. Build the container:
`docker build -t bme_collector:latest .`

3. Run:
`docker run -d bme_collector`

### InfluxDB
1. Create presistant storage area for influxDB data:
`mkdir ~/influxDB`

2. Run the influxDB container:
`docker run -p 8086:8086 -v ~/influxDB:/var/lib/influxdb -d influxdb`

### Grafana
1. Create presistant storage area for grafana data:
`mkdir ~/grafana-store`

2. Run the grafana container:
`docker run -d -p 3000:3000 -v ~/grafana-storage:/var/lib/grafana grafana/grafana-arm32v7-linux:dev-musl`
