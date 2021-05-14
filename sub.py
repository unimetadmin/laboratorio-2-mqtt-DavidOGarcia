import sys
import paho.mqtt.client
import psycopg2
from psycopg2 import Error

def connect_bd(path,temp):
	try:
		#Connect to an existing database
		connection = psycopg2.connect(user="postgres",
		password="password1", host="127.0.0.1", 
		database="lab2")

		insert_query1 = """INSERT INTO nevera(dato) VALUES(%s) """
		item_tuple1 = (temp)

		insert_query2 = """INSERT INTO olla(temperatura) VALUES(%s) """
		item_tuple2 = (temp)

		insert_query3 = """INSERT INTO contador_personas(personas) VALUES(%s) """
		item_tuple3 = (temp)

		insert_query4 = """INSERT INTO nevera(temperatura, hielo) VALUES(%s, %s) """
		item_tuple4 = (temp, "ice")

		insert_query5 = """INSERT INTO nevera(temperatura, hielo) VALUES(%s, %s) """
		item_tuple5 = (temp, "ice")

		#Create a cursor to perform database operations
		cursor = connection.cursor()
		# Print PostgreSQL details
		print("PostgreSQL server information")
		print(connection.get_dsn_parameters(), "\n")
		# Executing a SQL query
		if("nevera" in path):
			cursor.execute(insert_query1, item_tuple1)
			connection.commit()
			
		elif(path == "casa/cocina/olla"):
			cursor.execute(insert_query2, item_tuple2)
			connection.commit()
		elif(path == "casa/sala/contador_personas"):
			cursor.execute(insert_query3, item_tuple3)
			connection.commit()
		elif(path == "casa/sala/alexa"):
			cursor.execute(insert_query4, item_tuple4)
			connection.commit()
		elif(path == "casa/baño/tanque"):
			cursor.execute(insert_query5, item_tuple5)
			connection.commit()

		print("1 item se ha insertado correctamente")
		cursor.execute("SELECT version();")
		# Fetch result
		record = cursor.fetchone()
		print("You are connected to - ",record,"\n")

	except (Exception, Error) as error:
		print("Error while connecting to PostgreSQL", error)
	finally:
		if (connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")



def on_connect(client, userdata, flags, rc):
	print('connected (%s)' % client._client_id)
	client.subscribe(topic='casa/#', qos=2)

def on_message(client, userdata, message):
	print('------------------------------')
	print('topic: %s' % message.topic)
	print('payload: %s' % message.payload)
	print('qos: %d' % message.qos)
	text = message.payload
	array = str(text).split("\"")
	text1 = array[1]+array[2]+array[3]
	connect_bd(message.topic, text1)

def main():
	client = paho.mqtt.client.Client(client_id='alejandro-subs', clean_session=False)
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(host='127.0.0.1', port=1883)
	client.loop_forever()

if __name__ == '__main__':
	main()

sys.exit(0)