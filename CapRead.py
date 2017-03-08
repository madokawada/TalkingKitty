1#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
from random import choice
from pygame import mixer

GPIO.setmode(GPIO.BCM)

mixer.init()
s00_sound = mixer.Sound('../sounds/s00.ogg')
s01_sound = mixer.Sound('../sounds/s01.ogg')
s02_sound = mixer.Sound('../sounds/s02.ogg')
s03_sound = mixer.Sound('../sounds/s03.ogg')
s04_sound = mixer.Sound('../sounds/s04.ogg')
s05_sound = mixer.Sound('../sounds/s05.ogg')
s06_sound = mixer.Sound('../sounds/s06.ogg')
s07_sound = mixer.Sound('../sounds/s07.ogg')
s08_sound = mixer.Sound('../sounds/s08.ogg')
s09_sound = mixer.Sound('../sounds/s09.ogg')
s10_sound = mixer.Sound('../sounds/s10.ogg')
s11_sound = mixer.Sound('../sounds/s11.ogg')
s11_sound = mixer.Sound('../sounds/s12.ogg')
s11_sound = mixer.Sound('../sounds/s13.ogg')
s11_sound = mixer.Sound('../sounds/s14.ogg')
s11_sound = mixer.Sound('../sounds/s15.ogg')

sounds = [mixer.Sound('../sounds/s00.ogg'),
          mixer.Sound('../sounds/s01.ogg'),
          mixer.Sound('../sounds/s02.ogg'),
          mixer.Sound('../sounds/s03.ogg'),
          mixer.Sound('../sounds/s04.ogg'),
          mixer.Sound('../sounds/s05.ogg'),
          mixer.Sound('../sounds/s06.ogg'),
          mixer.Sound('../sounds/s07.ogg'),
          mixer.Sound('../sounds/s08.ogg'),
          mixer.Sound('../sounds/s09.ogg'),
          mixer.Sound('../sounds/s10.ogg'),
          mixer.Sound('../sounds/s11.ogg'),
          mixer.Sound('../sounds/s12.ogg'),
          mixer.Sound('../sounds/s13.ogg'),
          mixer.Sound('../sounds/s14.ogg'),
          mixer.Sound('../sounds/s15.ogg')]

# CapRead copied from 
# https://bitbucket.org/boblemarin/raspberrypi-capacitive-sensor/src/1c18fad88ae70ce1d83dee9c43528e27664a150d/CapSense1/CapSenseAndLEDs.py?at=master&fileviewer=file-view-default

timeout = 10000

def Sounds():
    pass

def CapRead(inPin,outPin):
    total = 0
    
    # set Send Pin Register low
    GPIO.setup(outPin, GPIO.OUT)
    GPIO.output(outPin, GPIO.LOW)
    
    # set receivePin Register low to make sure pullups are off 
    GPIO.setup(inPin, GPIO.OUT)
    GPIO.output(inPin, GPIO.LOW)
    GPIO.setup(inPin, GPIO.IN)
    
    # set send Pin High
    GPIO.output(outPin, GPIO.HIGH)
    
    # while receive pin is LOW AND total is positive value
    while( GPIO.input(inPin) == GPIO.LOW and total < timeout ):
        total+=1
    
    if ( total > timeout ):
        return -2 # total variable over timeout
        
     # set receive pin HIGH briefly to charge up fully - because the while loop above will exit when pin is ~ 2.5V 
    GPIO.setup( inPin, GPIO.OUT )
    GPIO.output( inPin, GPIO.HIGH )
    GPIO.setup( inPin, GPIO.IN )
    
    # set send Pin LOW
    GPIO.output( outPin, GPIO.LOW ) 

    # while receive pin is HIGH  AND total is less than timeout
    while (GPIO.input(inPin)==GPIO.HIGH and total < timeout) :
        total+=1
    
    if ( total >= timeout ):
        return -2
    else:
        return total

try:
    while True:
        reading = CapRead(17,18)
        #reading2 = CapRead(22,23)
        print(reading)
        if(reading > 10):
            choice(sounds).play()
            time.sleep(.3)
        time.sleep(.1)
finally:
    GPIO.cleanup()