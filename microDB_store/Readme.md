# Purpose
Collect and store various data in time searies format to be visualized

## Database
InfluxDB line protocol format example
`weather,location=us-midwest,season=summer temperature=82 1465839830100400200`

## Setup
Build Docker Container:  
`docker build -t collector:latest .`