import RPi.GPIO as GPIO
import time

PIR_PIN = 17
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

def initSEN0018():
    GPIO.setup(PIR_PIN, GPIO.IN)

#print('Starting up the PIR Module (click on STOP to exit)')
#time.sleep(1)
#print ('Ready')

def startSEN0018():
    while(True):
        if GPIO.input(PIR_PIN):
            print('Motion Detected')
    #else:
        #print('Nie ma cie')
    #time.sleep(1)
