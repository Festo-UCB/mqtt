from paho.mqtt import client as mqtt_client
from constants import broker, port, topic
from datetime import datetime, date
import time
import random

client_id = f"device-{random.randint(0, 100)}"
username = 'username'
password = 'password'

def connect_mqtt():
    def on_connect(client, user_data, flags, rc):
        if rc == 0:
            print("Connected to Mosquitto Broker")
        else:
            print("Failed to connect to Mosquitto Broker")
            print(f"Is Mosquitto Broker runnning and configured to use {broker}:{port}?")

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    
    return client

def publish(client, message):
    result = client.publish(topic, message)
    
    status = result[0]
    if status == 0:
        print(f"Sent '{message}' \nto topic '{topic}'")
    else:
        print(f"Failed to send message to topic {topic}")

def run_sim():
    usage_count = 0
    dev_id = 1000
    
    client = connect_mqtt()

    while True:
        usage_count += random.randint(1, 10) 
        msg = f"{{'device_id': '{dev_id}', 'usage': {usage_count}, 'date': '{date.today().strftime('%d-%m-%Y')}', 'time': '{datetime.now().strftime('%H:%M:%S')}'}}"

        publish(client, msg)
        time.sleep(10)

if __name__ == '__main__':
    run_sim()
