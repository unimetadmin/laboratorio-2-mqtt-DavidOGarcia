import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
import request

def on_connect(client, userdata, flags, rc):
	print('conectado publicador')



def main():
    
    client = paho.mqtt.client.Client("Unimet", False)
    client.qos = 0
    client.connect(host='localhost')

    while(True):
        url = "http://api.openweathermap.org/data/2.5/weather?q=Caracas&appid=6cf9ae43293928ec740fd51b2c9c524a"
        text = requests.get(url).json()
        temp = int(text['main']['temp']) - 273
        payload = {
            "temperatura de Caracas": str(temp)
        }
        
        client.publish('casa/sala/alexa', json.dumps(payload), qos=0)
        print(payload)
        time.sleep(1)
        
if __name__ == '__main__':
	main()
	sys.exit(0)