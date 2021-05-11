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
    meanEntrada = 10
    stdEntrada = 2
    tempMax = 12
    iceMax = 10
    contador = 0

    while(True):
        temp = int(np.random.uniform(8,tempMax))
        hielo = int(np.random.uniform(0,iceMax))
        payload = {
            "temperatura": str(temp)
        }
        payload2 = {
            "cantidad de hielo": str(hielo)
        }

        if(contador == 2):
            client.publish('casa/cocina/nevera', json.dumps(payload), qos=0)
            client.publish('casa/cocina/nevera', json.dumps(payload2), qos=0)
            print(payload)
            print(payload2)
            time.sleep(3)
            contador = 1
        else:
            client.publish('casa/cocina/nevera', json.dumps(payload), qos=0)
            print(payload)
            time.sleep(3)
            contador+=1
        


if __name__ == '__main__':
	main()
	sys.exit(0)