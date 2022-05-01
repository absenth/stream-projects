import time
import socket
import sys
import datetime
import Adafruit_DHT
from influxdb import InfluxDBClient

# Setup socket for systemd
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9988))
s.listen(1)


# Configure InfluxDB connection variables
host = ""      # your InfluxDB Host
port = 8086    # default port
user = ""      # the InfluxDB user created for the pi, with write access
password = ""  # the InfluxDB password created for the pi, with write access
dbname = ""    # the database we created earlier
interval = 60  # Sample period in seconds


# Create the InfluxDB client object
client = InfluxDBClient(host, port, user, password, dbname)


# Enter the sensor details
sensor = Adafruit_DHT.DHT22
sensor_gpio = 4

# think of measurement as a SQL table, it's not...but...
measurement = "rpi-dht22"
# location will be used as a grouping tag later
location = ""  # The name of the room this sensor will be placed in. IE: office


def main():
    try:
        while True:

            humidity_list, temp_list = zip(* [Adafruit_DHT.read_retry(22, 4) for _ in range(10)])
            humidity = sum(humidity_list)/len(humidity_list)
            temperature = sum(temp_list)/len(temp_list)

            iso = time.ctime()

            data = [
                    {
                        "measurement": measurement,
                            "tags": {
                                "location": location,
                            },
                            "time": iso,
                            "fields": {
                                "temperature": temperature,
                                "humidity": humidity
                            }
                        }
                ]
            client.write_points(data)
            time.sleep(interval)

    except KeyboardInterrupt:
        pass


while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    conn.close()
    main()
