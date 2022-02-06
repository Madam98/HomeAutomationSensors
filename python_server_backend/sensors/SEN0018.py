import RPi.GPIO as GPIO
import datetime
import time
import os.path

import sqlite3
from sqlite3 import Error

PIR_PIN = 17
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

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


def initSEN0018():
    GPIO.setup(PIR_PIN, GPIO.IN)

#print('Starting up the PIR Module (click on STOP to exit)')
#time.sleep(1)
#print ('Ready')

def startSEN0018():
    conn = initSQLite()
    while(True):
        if GPIO.input(PIR_PIN):
            print('Motion Detected')
            current = datetime.datetime.now()
            #current = datetime.datetime.now()
            
            #print(current)
            
            conn.execute("INSERT INTO sen0018 (date_time) VALUES (?)", current)
            conn.commit()
            print(conn.execute("SELECT id ,TIME(date_time) FROM sen0018 ORDER BY ROWID DESC").fetchone())
    #else:
        #print('Nie ma cie')
    #time.sleep(1)
