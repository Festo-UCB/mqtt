# MQTT Client and Subscriber
## Description
Repository for the MQTT Data Simulation. Publishes sample JSON data using the MQTT protocol and uploads it to the Influx Database for the purpose of querying with smart contracts from the [Rust Backend Repository](https://github.com/Festo-UCB/RustBackend). Sample data may not necessarily reflect the true data being produced by the IOT device. Dependent on Eclipse Paho MQTT and InfluxDB. Install with `pip3 install paho-mqtt` and `pip install influxdb`.

## Installing Mosquitto Broker
This depends on Mosquitto as an MQTT broker. Install using [directions](https://mosquitto.org/download/). Available on Linux distributions with `snap install mosquitto`. Available on Mac using `brew install mosquitto`.

## Starting the Database
InfluxDB install [documentation](https://docs.influxdata.com/influxdb/v1.8/introduction/install/). Ubuntu instructions below. \
Install Database:
```
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/lsb-release
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt-get update && sudo apt-get install influxdb
```
Install Client:
```
sudo apt-get update && sudo apt-get install influx
```
Start InfluxDB with `sudo service InfluxDB start`.

```
sudo vim /etc/influxdb/influxdb.conf
```
Find the `auth-enabled = false` line. Remove the `#` to uncomment it. Use:
```
sudo systemctl restart influxdb
```
to restart the database with this new configuration.


## Starting the MQTT Services
In seperate terminals run:
```
mosquitto -p 8002
python3 mqtt_client.py
python3 mqtt_sub.py
```

## Navigating the Database 
Enter the database with `$ influx`. Exit the database with `> quit`. \
Show databases with `> SHOW DATABASES`. After running the python script `mqtt_sub.py` you should see the database `PuPPY`. \
Check the contents of the table using `SELECT * FROM 'device_data'`. Confirm that the data thrown from `mqtt_client.py` is populating the database.

## Repository File Descriptions
#### mosquitto.conf
Contains the startup configuration for Mosquitto \
Run using `mosquitto -p 8002`. This port can be changed in the `constants.py` file if `8002` is use.

#### mosquitto.log
Logfile for Mosquitto

#### mqtt_client.py
Publishes sample MQTT data every 10 seconds \
Run using `python3 mqtt_client.py`

#### mqtt_sub.py
Subscribes to the moquitto broker\
Publishes data to the Influx Database\
Run using `python3 mqtt_sub.py`
