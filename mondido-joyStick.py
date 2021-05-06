"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.
Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("mousemove") # this is going to be the wildcard
        display.show(Image.YES)

def on_message(client, userdata, msg):
    
    if msg.payload.decode() == "N": #this will check if the direction of the joystick is from north then it will how and arrow that is pointing to the north
        display.show(Image.ARROW_N)
    if msg.payload.decode() == "S":#this will check if the direction of the joystick is from south then it will how and arrow that is pointing to the south
        display.show(Image.ARROW_S)
    if msg.payload.decode() == "E": #this will check if the direction of the joystick is from noreasth then it will how and arrow that is pointing to the east
        display.show(Image.ARROW_E)
    if msg.payload.decode() == "W":#this will check if the direction of the joystick is from west then it will how and arrow that is pointing to the west
        display.show(Image.ARROW_W)
    if msg.payload.decode() == "NE":#this will check if the direction of the joystick is from northeast then it will how and arrow that is pointing to the northeast
        display.show(Image.ARROW_NE)
    if msg.payload.decode() == "NW":#this will check if the direction of the joystick is from northwest then it will how and arrow that is pointing to the nortwest
        display.show(Image.ARROW_NW)
    if msg.payload.decode() == "SW":#this will check if the tdirection of the joystick is from southwest then it will how and arrow that is pointing to the soutwest
        display.show(Image.ARROW_SW)
    if msg.payload.decode() == "SE":#this will check if the tdirection of the joystick is from southeast then it will how and arrow that is pointing to the southeast
        display.show(Image.ARROW_SE)
  

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60) #connection or the broker

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqt
