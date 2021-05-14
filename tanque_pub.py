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
    cantAgua = 100

    while(True):
        temp = int(np.random.uniform(8,tempMax))
        payload = {
            "temperatura": str(temp)
        }

        if(temp == 100):
            print("El agua ya hirvió")
        
        client.publish('casa/baño/tanque', json.dumps(payload), qos=0)
        print(payload)
        time.sleep(1)
        contador+=1
        
if __name__ == '__main__':
	main()
	sys.exit(0)