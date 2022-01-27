from machine import Pin
import time

red = Pin(15, Pin.OUT)
green = Pin(14, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_DOWN)
door = Pin(10, Pin.IN, Pin.PULL_DOWN)

signal = ""
prev_signal = ""
NSFW_mode = False

while True:
    # Light up LEDs based on button/door states
    red.value(not button.value())
    green.value(not door.value())
    
    # If door opens, send a SFW signal
    if not door.value():
        
        # My door is not flush with the door frame, leading to
        # occasional "blips". Pause for 0.1 seconds to mitigate
        # false positives
        time.sleep(0.1)
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