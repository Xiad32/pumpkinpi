import RPi.GPIO as GPIO
import time
import subprocess
import random

led = 3
inPin = 7
# add file names to the list below
soundFiles = []
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.HIGH)
GPIO.setup(inPin, GPIO.IN)

def interact():
    selectedSound = random.choice(soundFiles)
    p = subprocess.Popen(['aplay', './sounds/' + selectedSound + '.wav'])
    nextState = 1
    states = [GPIO.HIGH, GPIO.LOW]
    speeds =  [  0.025, 0.04, 0.05, 0.1, 0.2, 0.25 ]
    speeds = speeds + speeds[:-1][::-1]
    def invert(x): return int(0.25/x);
    durations = list(map(invert, speeds))
    speedIndex = 0;
    counter = durations[speedIndex];

    while p.poll() == None:
        GPIO.output(led, states[nextState])
        # print("state: "+ str(states[nextState]))  
        if nextState: 
            nextState = 0 
        else: 
            nextState = 1
        if counter <= 0:
            speedIndex = (speedIndex + 1) % len(speeds)
            #print("New speedIndex: " + str(speedIndex))
            counter = durations[speedIndex]
        counter -= 1;
        #print("speed: "+str(speeds[speedIndex])+" counter: "+str(counter))
        time.sleep(speeds[speedIndex])

    GPIO.output(led, GPIO.LOW)

while True:
    #print("Reading Pin")
    engaged = GPIO.input(inPin)
    #print("Pin Reading: " + str(engaged))
    if engaged: interact()
    #print("Sleeping")
    time.sleep (1)

GPIO.output(led, GPIO.LOW)
GPIO.cleanup()
