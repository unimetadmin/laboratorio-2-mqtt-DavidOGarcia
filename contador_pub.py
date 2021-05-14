import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime

def on_connect(client, userdata, flags, rc):
	print('conectado publicador')



def main():
    client = paho.mqtt.client.Client("Unimet", False)
    client.qos = 0
    client.connect(host='localhost')
    cantPersonas = 10
    while(True):
        personas = int(np.random.uniform(0,cantPersonas))
        payload = {
            "personas en la sala": str(personas)
        }

        if(personas >= 5):
            print("Hay demasiadas personas en la sala")
        
        client.publish('casa/sala/contador_personas', json.dumps(payload), qos=0)
        print(payload)
        time.sleep(60)
        
if __name__ == '__main__':
	main()
	sys.exit(0)