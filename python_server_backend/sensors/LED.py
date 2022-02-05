import RPi.GPIO as GPIO
from time import sleep

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)

def initLED():
    GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)

def startLED():
    GPIO.output(16, GPIO.HIGH) # Turn on
    sleep(0.1)                 # Sleep for 1 second
    GPIO.output(16, GPIO.LOW)  # Turn off
    sleep(0.1)                 # Sleep for 1 second
    
    GPIO.output(20, GPIO.HIGH) # Turn on
    sleep(0.1)                 # Sleep for 1 second
    GPIO.output(20, GPIO.LOW)  # Turn off
    sleep(0.1)                 # Sleep for 1 second
    
    GPIO.output(21, GPIO.HIGH) # Turn on
    sleep(0.1)                 # Sleep for 1 second
    GPIO.output(21, GPIO.LOW)  # Turn off
    sleep(0.1)                 # Sleep for 1 second
    
        
    
