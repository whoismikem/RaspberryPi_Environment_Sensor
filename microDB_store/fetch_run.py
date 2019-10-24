import requests
import json
from influxdb import InfluxDBClient


ADDRESS='192.168.1.10:5000'
DB_NAME='sensor_db'

def to_point(payload):
    print("!!!!!!!!!!!!!!!")
    print(payload)
    data = []
    measurement_name='bme280'
    data.append("{measurement},location={location} temperature={temperature},humidity={humidity},pressure={pressure}"
            .format(measurement=measurement_name,
                    location="closet1",
                    temperature=payload['ambient_temperature'],
                    humidity=payload['humidity'],
                    pressure=payload['pressure']))
    return data

def store_json_response(response):
    json_res = response.json()
    print("JSON Response:", type(json_res))
    point = to_point(json_res)
    print("Point Type: ", type(point))
    return point
try:
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database(DB_NAME)
except:
    print("Broke here")


try:
    response = requests.get('http://' + ADDRESS + '/api/bme280')
    point = store_json_response(response)

    client.write(point, {'db':DB_NAME}, 204, 'line')
    print("DATA Written!")
    results =  client.query('SELECT * FROM "bme280"')
    print("RES!!!!!!!!!!!!!")
    print(results.raw)
except:
    raise("Unable to fetch data")
