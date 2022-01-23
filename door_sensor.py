from machine import Pin
import time

red = Pin(15, Pin.OUT)
green = Pin(14, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_DOWN)
door = Pin(12, Pin.IN)

signal = ""
prev_signal = ""
NSFW_mode = False

while True:
    # Light up LEDs based on button/door states
    if not button.value():
        red.value(1)
    else:
        red.value(0)
        
    if not door.value():
        green.value(1)
    else:
        green.value(0)
    
    # If door opens, send a SFW signal
    if not door.value():
        signal = "SFW"
        NSFW_mode = False
        
    # If door closed and button gets pressed, send NSFW signal
    # Do not send a SFW signal until the door opens
    if (button.value() and door.value()) or NSFW_mode:
        signal = "NSFW"
        NSFW_mode = True
    else:
        signal = "SFW"
    
    if signal != prev_signal:
        prev_signal = signal
        print(signal)