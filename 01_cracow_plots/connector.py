import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def create_server_connection():
    try:
        print(os.getenv('DB_HOST'))
        if connection is None:
            connection = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                passwd=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_DATABASE')
            )
        print("Połączenie udane")
        return connection
    except Error as err:
        print(f"Nie udało się połączyć: {err}")
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("Połączenie zamknięte")
