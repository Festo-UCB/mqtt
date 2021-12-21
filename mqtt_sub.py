from influxdb import InfluxDBClient
import json
from datetime import datetime
from paho.mqtt import client as mqtt_client
from mqtt_client import connect_mqtt
from constants import topic

def establish_database():
    db_client = InfluxDBClient('localhost', 8086, 'admin', 'password', 'PuPPY')
    db_client.create_database('PuPPY')
    db_client.get_list_database()
    db_client.switch_database('PuPPY')
    return db_client

def make_payload(message: str):
    payload = []
    message_dict = json.loads(message)
    data = {
        "measurement": "device-data",                       # similar to table name
        "tags": {
            "device-id": f"{message_dict['device_id']}"     # similar to primary key
            },
        "time": datetime.now(),                             # times series database needs timestamp
        "fields": {                                         # data from the iot device
            "usage": f"{message_dict['usage']}",
            "transaction_date": f"{message_dict['date']}",
            "transaction_time": f"{message_dict['time']}"
            }
    }
    payload.append(data)
    return payload

def send_payload(db_client, payload):
    db_client.write_points(payload)

def subscribe(client: mqtt_client):
    db_client = establish_database()

    def on_message(client, user_data, message):
        print(f"Received '{message.payload.decode()}' from '{message.topic}' topic")
        send_payload(db_client, make_payload(message.payload.decode('utf-8')))

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
