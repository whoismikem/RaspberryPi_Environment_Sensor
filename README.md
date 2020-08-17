# Physical World Sampler (Environment Sensor)
Born form the need to sample the physical world in many different ways for various purposes and applications.

* Room monitor - Monitor various rooms in your house or other structures.
* Green house / Grow Tent - Monitor the environment your plants are subjected to.
    
## Stack
![arch diagram](/extras/arch_diagram.png)

## Components
* [ Raspberry Pi4 ](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
* [ Raspberry Pi Case ](https://www.amazon.com/gp/product/B07W3ZMVP1/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
* [ Jumper Wires ](https://www.amazon.com/gp/product/B07XC5VWLN/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1) For making sensor connections.
* [ Waveshare BME280 Environmental Sensor ]( https://www.amazon.com/gp/product/B07P4CWGGK/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc= ) Providing temperature, humidity and barometric pressure of the surrounding environment.
* [ Raspberry Pi Camera Module V2: 8 Megapixel,1080p ]( https://www.amazon.com/gp/product/B01ER2SKFS/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1 ) Providing video and imagery of the surrounding environment.

## Running
### Docker Compose
1. Build container images:  `docker-compose build`
2. Start containers: `docker-compose up -d`

Build and run: `docker-compose up --build -V`

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
1. Create presistant storage area for grafana data:  :
`mkdir ~/grafana-store`

2. Run the grafana container:  
`docker run -d -p 3000:3000 -v ~/grafana-storage:/var/lib/grafana grafana/grafana-arm32v7-linux:dev-musl`

### Monitor PI Resources
Helpful Setup Link: https://medium.com/@dorian599/iot-raspberry-pi-container-and-system-monitoring-with-influxdb-telegraf-and-grafana-a1767c38c109

Download Grafana Dashboard from here: https://grafana.com/grafana/dashboards/10578

