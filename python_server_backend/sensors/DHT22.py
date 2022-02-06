import Adafruit_DHT
#import board
import datetime
import time
import os.path

import sqlite3
from sqlite3 import Error


def create_connection(db_path):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        print("Connected to the database file")
        return conn

    except Error as e:
        print(e)


def initSQLite():
        db_path = "../sqlite_db/database.db"
        if os.path.isfile(db_path):
            print("Plik z baza danych istnieje")
            conn = create_connection(db_path)
            return conn
        else:
            print("Problem ze znalezieniem bazy danych")
            return -1

#def initDHT22():

#DHT_SENSOR = Adafruit_dht.DHT22(board.D18)
DHT_SENSOR = Adafruit_DHT.DHT22

DHT_PIN = 18
#umidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

def startDHT22(): 
    #humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
    conn = initSQLite()
    
    while(True):
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        current = datetime.datetime.now()
        if humidity is not None and temperature is not None:        
            #print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
            conn.execute("INSERT INTO humidity_temperature (date_time, humidity, temperature) VALUES (?, ?, ?)", (current, humidity, temperature))
            conn.commit()
            print("DHT:")
            print(conn.execute("SELECT id ,TIME(date_time), temperature, humidity FROM humidity_temperature ORDER BY ROWID DESC").fetchone())
   
        else:
            print("Failed to retrieve data from humidity sensor")
        
        time.sleep(10)
