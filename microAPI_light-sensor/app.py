import json
import datetime
import RPi.GPIO as GPIO
from time import sleep
from flask import Flask

BIND_ADDRESS = '0.0.0.0'
PORT = 5001

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

# Date to string converter
def date_to_str(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def get_data():
    result = GPIO.input(4)
    if result == 1:
        result = False;
    elif result == 0:
        result = True;
    else:
        result = None

    datetime_now = datetime.datetime.now()
    data = {
            "time_stamp": datetime_now,
            "light": result
        }

    sleep(1)
    return data

app = Flask(__name__)

@app.route("/api/light")
def execute_route():
    try:
        json_data = json.dumps(get_data(), default = date_to_str)
        return json_data
    except Exception as err:
        print(f'[ Error ]: err')
        return { 'error': err}

if __name__ == '__main__':
    app.run(host=BIND_ADDRESS, port=PORT, debug=True) 
