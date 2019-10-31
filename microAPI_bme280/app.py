from flask import Flask
import bme280
import smbus2
import json
import datetime
from time import sleep

# Date to string converter
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def get_data():

    port = 1
    address = 0x77 # Adafruit BME280 address. Other BME280s may be different
    bus = smbus2.SMBus(port)

    bme280.load_calibration_params(bus,address)
    bme280_data = bme280.sample(bus,address)
    now = datetime.datetime.now()
    data = {
            "time_stamp":now,
            "humidity":bme280_data.humidity,
            "pressure":bme280_data.pressure,
            "ambient_temperature":bme280_data.temperature
        }

    sleep(1)
    return data

app = Flask(__name__)

@app.route("/api/bme280")
def hello():
    print("!!!!!")
    print(get_data())
    json_data = json.dumps(get_data(), default = myconverter)
    return json_data


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) 
