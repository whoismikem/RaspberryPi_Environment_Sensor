import json
import datetime
import RPi.GPIO as GPIO
from time import sleep
from flask import Flask

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

# Date to string converter
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def get_data():
    result = GPIO.input(4)
    if result == 1:
        result = False;
    elif result == 0:
        result = True;

    now = datetime.datetime.now()
    data = {
            "time_stamp":now,
            "light": result
        }

    sleep(1)
    return data

app = Flask(__name__)

@app.route("/api/light")
def hello():
    json_data = json.dumps(get_data(), default = myconverter)
    return json_data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True) 
