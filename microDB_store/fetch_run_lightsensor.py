import requests
import json
from influxdb import InfluxDBClient


ADDRESS='localhost:5001'
DB_ADDRESS='localhost'
DB_NAME='sensor_db'

def to_point(payload):
    data = []
    measurement_name='lightsensor'
    data.append("{measurement},location={location} lights={temperature}"
            .format(measurement=measurement_name,
                    location="closet1",
                    lights=payload['light']))
    return data

def response_convert(response):
    json_res = response.json()
    point = to_point(json_res)
    print(f'POINT (lightsensor): {point}')
    return point


try:
    client = InfluxDBClient(host=DB_ADDRESS, port=8086)
    client.switch_database(DB_NAME)
except:
    print("DB Connection broken!")


try:
    response = requests.get('http://' + ADDRESS + '/api/light')
    print(f'RESPONSE (lightsensor): {response.json()}')
    point = response_convert(response)

    client.write(point, {'db':DB_NAME}, 204, 'line')
except:
    raise("Unable to fetch data")