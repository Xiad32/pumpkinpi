# pumpkinpi
Halloween Raspberry Pi Fun Work

# Description
This is a simple and fun project to get young STEM enthusiasts to work on a halloween theme STEM project. The equipment used are readily available (see list below). 

# Tools Used
1. Raspberry Pi 3b (any Raspberry Pi will do. The pins might be different)
2. AIY Voice Hat or any simmilar device to play sound from a pi (connections will differ)
3. Motion sensor
4. Breadboard
5. (optional) breakout cable from the pi to the breadboard
6. LEDs (lots of them)
7. Resistors for the LEDs
8. Power adaptor for the pi

# Set up
Carve a pumpkin. Be creative. Just make sure you can insert the circuit in at the end.
This was mine:

#ADD IMAGE

# Hardware
- Connecting the rig is simple. I used the references here to connect the Voice Hat to the pi. This frees ups the remaining pins for the leds and the motion sensor.
https://pinout.xyz/pinout/voice_hat#

- Choose one of the GPIO pins to turn on and off the lights. Pin 3 was used in the code. Change it as required. You can use the connection below as a guide
![picture alt](https://cdn.shopify.com/s/files/1/0176/3274/files/LEDs-BB400-1LED_bb_grande.png?6398700510979146820 "Connecting LEDs")
source: https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
I used a single pin for all the leds. You can modify the code to use multiple pins if needed.

- I used a PIR sensors for this project. They are simple to set up. One pin goes to Vcc the other to ground. The third pin connects to a GPIO for reading the sensor output. In the code, the motion sensor pin is hardcoded to 7. This can be changed if needed to. The senstivity and range can be modified as seen fit.

# Software
- For licensing reasons, I have not included any sounds in the repo. Download sounds that you like from several hosting sites on the internet and save them in the sounds directory. Then add the name of those files in the placeholder for them in the main.py file. You can use multiple files. The process will pick randomly from the provided list everytime the sensor is triggered.
- Running the code is simple. Simply run the command below from the terminal. Make sure you are in the root directory of the repository (pumpkinpi)

`python3 main.py`

# Result
See for yourself

# Feedback
Feedback is welcome. Upgrades to the code, connection or new ides are always nice. Thanks.
