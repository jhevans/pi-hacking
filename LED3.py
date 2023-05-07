# Event based switch on PIN 10 flashes LED at pin 12 twice

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pins definitions
btn_pin = 4
led_pin = 12

# Set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

def button_callback(channel):
    print("Blink blink!")
    
    for _ in range(2):
        GPIO.output(led_pin,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_pin,GPIO.LOW)
        time.sleep(0.5)

GPIO.add_event_detect(btn_pin,GPIO.RISING,callback=button_callback)

try:
    while(True):
        pass
finally:
    GPIO.cleanup()

