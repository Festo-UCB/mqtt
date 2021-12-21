# MQTT Client and Subscriber
Repository for the MQTT Data Simulation. Publishes sample JSON data using the MQTT protocol and uploads it to the Influx Database for the purpose of querying with smart contracts from the [Rust Backend Repository](https://github.com/Festo-UCB/RustBackend). Sample data may not necessarily reflect the true data being produced by the IOT device. Dependent on Eclipse Paho MQTT. Install with `pip3 install paho-mqtt`.

### mosquitto.conf
Contains the startup configuration for Mosquitto \
Run using `mosquitto -c mosquitto.conf`

### mosquitto.log
Logfile for Mosquitto

### mqtt_client.py
Publishes sample MQTT data every 10 seconds \
Run using `python3 mqtt_client.py`

### mqtt_sub.py
Subscribes to the moquitto broker\
Publishes data to the Influx Database\
Run using `python3 mqtt_sub.py`
