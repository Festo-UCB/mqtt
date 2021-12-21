from paho.mqtt import client as mqtt_client
from mqtt_client import connect_mqtt
from constants import topic

def subscribe(client: mqtt_client):
    def on_message(client, user_data, message):
        print(f"Received '{message.payload.decode()}' from '{message.topic}' topic")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
