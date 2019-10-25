from influxdb import InfluxDBClient

DB_NAME='sensor_db'
IDB_ADDRESS = 'localhost'

try:
    client = InfluxDBClient(host=IDB_ADDRESS, port=8086)
    client.switch_database(DB_NAME)
except:
    print("! Unable to connet to influxDB")


results =  client.query('SELECT * FROM "bme280"')
print(results.raw)
print("!!!!!!!!!!!!!!!!!!!!!")
print(results.get_points())