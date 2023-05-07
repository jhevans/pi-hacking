# Event based switch on PIN 10 flashes LED at pin 12 twice

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)

def button_callback(channel):
    print("Blink blink!")
    
    for _ in range(2):
        GPIO.output(12,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(12,GPIO.LOW)
        time.sleep(0.5)

GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback)

while(True):
    pass

