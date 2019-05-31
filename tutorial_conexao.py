import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def connectDB():
	connection_config_dict = {
	    'user': 'application',
	    'password': '1234',
	    'host': '127.0.0.1',
	    'database': 'gatry',
	    'raise_on_warnings': True,
	    'use_pure': False,
	    'autocommit': True,
	    'pool_size': 5
	}
	try:
	    connection = mysql.connector.connect(**connection_config_dict)
	    if connection.is_connected():
	        db_Info = connection.get_server_info()
	        print("Succesfully Connected to MySQL database. MySQL Server version on ", db_Info)
	        return connection
	except Error as e:
	    print("Error while connecting to MySQL", e)

def closeDB(connection):
	if connection.is_connected():
		connection.close()
