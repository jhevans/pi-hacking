# Use a switch on GPIO pin 10 to switch an LED on pin 12

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while(True):
    if GPIO.input(10) == GPIO.HIGH:
        print("Button pushed")
        print("LED on")
        GPIO.output(12,GPIO.HIGH)
    else:
        print("No button")
        print("LED off")
        GPIO.output(12,GPIO.LOW)



