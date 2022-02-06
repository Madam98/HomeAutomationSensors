import RPi.GPIO as GPIO
import datetime
import time
import os.path

import sqlite3
from sqlite3 import Error

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
mq7_dpin = 26
mq7_apin = 0

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


#port init
def initMD7():
         GPIO.setwarnings(False)
         #GPIO.cleanup()			#clean up at the end of your script
         GPIO.setmode(GPIO.BCM)		#to specify whilch pin numbering system
         # set up the SPI interface pins
         GPIO.setup(SPIMOSI, GPIO.OUT)
         GPIO.setup(SPIMISO, GPIO.IN)
         GPIO.setup(SPICLK, GPIO.OUT)
         GPIO.setup(SPICS, GPIO.OUT)
         GPIO.setup(mq7_dpin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)	

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout
#main ioop

def startMD7():
        conn = initSQLite()
        #print("please wait...")
        #time.sleep(20)
    
        while(True):
            COlevel=readadc(mq7_apin, SPICLK, SPIMOSI, SPIMISO, SPICS)
            result = (((COlevel/1024.)*5) * 2000)/5.0
            current = datetime.datetime.now()
            
            #print("current" + str(conn))
            
            #print("Current CO AD vaule = " +str("%.2f"%((COlevel/1024.)*5))+" V")
            conn.execute("INSERT INTO mq7 (date_time, co_value, co_warning) VALUES (?, ?, ?)", (current, result, 1 - GPIO.input(mq7_dpin)))
            conn.commit()
            print("MQ7")
            print(conn.execute("SELECT id ,TIME(date_time), co_value, co_warning FROM mq7 ORDER BY ROWID DESC").fetchone())
            
            #if GPIO.input(mq7_dpin):
                
            time.sleep(10)
    


'''
def main():
         initMD7()
         #print("please wait...")
         #time.sleep(20)
         while True:
                  COlevel=readadc(mq7_apin, SPICLK, SPIMOSI, SPIMISO, SPICS)
                  
                  result = (((COlevel/1024.)*5) * 2000)/5.0
                  
                  if GPIO.input(mq7_dpin):
                           #print("CO not leak")
                           #print("Current CO AD vaule = " +str("%.2f"%((COlevel/1024.)*5))+" V")
                           #print("Current CO density is:" +str("%.2f"%((COlevel/1024.)))+" %")
                           #print("Uzyskana wartosc PPM: " +str("%.2f"%(result))+" ppm");
                           
                           time.sleep(0.5)
                  else:
                           print("CO is detected")
                           print("Current CO AD vaule = " +str("%.2f"%((COlevel/1024.)*5))+" V")
                           print("Current CO density is:" +str("%.2f"%((COlevel/1024.)))+" %")
                           print("Uzyskana wartosc PPM: " +str("%.2f"%(result))+" ppm");
                           
                           time.sleep(0.5)

if __name__ =='__main__':
         try:
                  main()
                  pass
         except KeyboardInterrupt:
                  pass
'''

GPIO.cleanup()
