import paho.mqtt.client as mqtt
import sqlite3
import time

def on_message(mqttc, obj, msg):
    payload=msg.payload.decode('ascii')
    print(payload)

user = "tbsiksgl"
pwd = "1gAdKntb6WfT"
topic = "test"
server = "soldier.cloudmqtt.com"
port = 14009
mqttc = mqtt.Client()
mqttc.username_pw_set(user,pwd)
mqttc.on_message = on_message
mqttc.connect(server, port)
mqttc.subscribe(topic, 0)
mqttc.loop_forever()
