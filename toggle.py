from machine import Pin
import time

red = Pin(15, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_DOWN)

signal = ""
prev_signal = ""
NSFW_mode = False

while True:

    red.value(0 if NSFW_mode else 1)

    if button.value():
        # Toggle NSFW_Mode
        NSFW_mode = not NSFW_mode
        signal = "NSFW" if NSFW_mode else "SFW"
                
        if signal != prev_signal:
            prev_signal = signal
            print(signal)
        
        time.sleep(0.5)
    
    
