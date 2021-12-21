# MQTT Client and Subscriber
## Description
Repository for the MQTT Data Simulation. Publishes sample JSON data using the MQTT protocol and uploads it to the Influx Database for the purpose of querying with smart contracts from the [Rust Backend Repository](https://github.com/Festo-UCB/RustBackend). Sample data may not necessarily reflect the true data being produced by the IOT device. Dependent on Eclipse Paho MQTT and InfluxDB. Install with `pip3 install paho-mqtt` and `pip install influxdb`.

## Starting the Database
InfluxDB install documentation: https://docs.influxdata.com/influxdb/v1.8/introduction/install/ \
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

## Starting the MQTT Services
In seperate terminals run:
```
mosquitto -p 8003
python3 mqtt_client.py
python3 mqtt_sub.py
```

## Repository File Descriptions
#### mosquitto.conf
Contains the startup configuration for Mosquitto \
Run using `mosquitto -p 8003`

#### mosquitto.log
Logfile for Mosquitto

#### mqtt_client.py
Publishes sample MQTT data every 10 seconds \
Run using `python3 mqtt_client.py`

#### mqtt_sub.py
Subscribes to the moquitto broker\
Publishes data to the Influx Database\
Run using `python3 mqtt_sub.py`
