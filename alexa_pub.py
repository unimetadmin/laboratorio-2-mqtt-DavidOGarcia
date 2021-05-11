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
	meanEntrada = 10 #media
	stdEntrada = 2  #desviacion estandar
	tempMax = 12  #temperatura maxima
	horaBase= datetime.datetime.now().replace(minute=0, second=0)
	personasPorHora = np.random.normal(meanEntrada, stdEntrada)
	horaBase = horaBase + datetime.timedelta(hours=1)
	while(personasPorHora>0):
		hora = horaBase + datetime.timedelta(minutes=np.random.uniform(0,60))				
		temp = int(np.random.uniform(8, tempMax))
		payload = {
			"fecha": str(hora),
			"temperatura": str(temp)
		}
		client.publish('unimet/admin/bd',json.dumps(payload),qos=0)		
		personasPorHora-=1
		print(payload)
		time.sleep(300)
if __name__ == '__main__':
	main()
	sys.exit(0)