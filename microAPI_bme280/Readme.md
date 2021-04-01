# BME280

## Notes
* Enable i2c on raspberry pi (if not yet enabled): `sudo raspi-config`
* Install i2c-tools: `sudo apt-get install i2c-tools`

## Verify sensor
* Verify kernel i2c enabled: `dmesg | grep i2c`
```
[    3.545507] i2c /dev entries driver
```
* Check kernel i2c drivers/modules loaded: `lsmod | grep i2c`
```
i2c_bcm2835            16384  0
i2c_dev                20480  0
```
* Check device is communicating: `i2cdetect -y 1`
```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- 77                         
```


## Build Container
* Build container image: `docker build -t microapi_bme280 .`
* Run container: `docker run -d -p 5000:5000 --rm --privileged --name microapi_bme280 microapi_bme280`


## Running without container
* Python virtual environment: `python3 -m venv venv`
* Activate virtual environment: `source venv/bin/activate`
* Install packages: `pip install -r requirements.txt`
* Run: `python app.py`

### API Endpoint  
`http://<sensor_address>:5000/api/bme280`