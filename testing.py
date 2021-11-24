import RPi.GPIO as GPIO
import time

inPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin, GPIO.IN)

while True:
    engaged = GPIO.input(inPin)
    if engaged: print("Engaged")
    else: print("Not engaged")
    time.sleep(1)


