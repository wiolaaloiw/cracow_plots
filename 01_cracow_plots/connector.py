import mysql.connector
from mysql.connector import Error
import json

def create_server_connection():
    with open('C:/Users/wmwsz/OneDrive/Desktop/python/TechLeads/L1-connector/01_cracow_plots/db_config.json', 'r') as file:
        config = json.load(file)
    
    connection = None
    try:
        connection = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            passwd=config['password'],
            database=config['database']
        )
        print("Połączenie udane")
    except Error as err:
        print(f"Nie udało się połączyć: {err}")
    
    return connection