from machine import Pin
import time

red = Pin(15, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_DOWN)

signal = ""
prev_signal = ""
a_mode = False

while True:

    red.value(0 if a_mode else 1)

    if button.value():
        # Toggle mode
        a_mode = not a_mode
        signal = "a" if a_mode else "b"
                
        if signal != prev_signal:
            prev_signal = signal
            print(signal)
        
        time.sleep(0.5)
    
    
