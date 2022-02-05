import LED
import DHT22
import MD7
import SEN0018
import CAMERA

import logging
import threading
import time
import RPi.GPIO as GPIO
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
        
        
def initGPIOMain():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

def runLED(name):
    LED.initLED();
    while(True):
        logging.info("Thread %s: starting", name)
        #time.sleep(10)
        LED.startLED()
        logging.info("Thread %s: finishing", name)

def runDHT22(name):
    #DHT22.initDHT22()
    while(True):
        logging.info("Thread %s: starting", name)
        DHT22.startDHT22()
        logging.info("Thread %s: finishing", name)   

def runMD7(name):
    MD7.initMD7()
    while(True):
        logging.info("Thread %s: starting", name)
        MD7.startMD7()
        logging.info("Thread %s: finishing", name)
        
def runSEN0018(name):
    SEN0018.initSEN0018()
    while(True):
        logging.info("Thread %s: starting", name)
        SEN0018.startSEN0018()
        logging.info("Thread %s: finishing", name)
        
def runCAMERA(name):
    #while(True):
    logging.info("Thread %s: starting", name)
    CAMERA.startCAMERA()
    #logging.info("Thread %s: finishing", name)   

#def main():
    
if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    initGPIOMain()
    #conn = initSQLite()
    
    threads = list()
    
    logging.info("LED : create thread %d", 1)
    led_thread = threading.Thread(target=runLED, args=(1,))
    time.sleep(0.5)
    
    logging.info("DHT22 : create thread %d", 2)
    DHT22_thread = threading.Thread(target=runDHT22, args=(2,))
    time.sleep(0.5)
    
    logging.info("MD7 : create thread %d", 3)
    MD7_thread = threading.Thread(target=runMD7, args=(3,))
    time.sleep(0.5)
    
    logging.info("SEN0018 : create thread %d", 4)
    SEN0018_thread = threading.Thread(target=runSEN0018, args=(4,))
    time.sleep(0.5)
    
    logging.info("CAMERA : create thread %d", 5)
    CAMERA_thread = threading.Thread(target=runCAMERA, args=(5,))    
    time.sleep(0.5)
    
    threads.append(led_thread)
    threads.append(DHT22_thread)
    threads.append(MD7_thread)
    #threads.append(SEN0018_thread)
    #threads.append(CAMERA_thread)
    
    #led_thread.start()
    DHT22_thread.start()
    MD7_thread.start()
    SEN0018_thread.start()
    CAMERA_thread.start()
    
    
    
    
    
    
