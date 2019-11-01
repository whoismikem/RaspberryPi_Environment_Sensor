from influxdb import InfluxDBClient

DB_NAME='sensor_db'
IDB_ADDRESS = '192.168.1.10'

try:
    client = InfluxDBClient(host=IDB_ADDRESS, port=8086)
#    client.create_database(DB_NAME)
    client.switch_database(DB_NAME)
except:
    print("! Unable to connet to influxDB")


results =  client.query('SELECT * FROM "bme280"')
print(results.raw)
print("!!!!!!!!!!!!!!!!!!!!!")
print(results.get_points())
