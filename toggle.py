from machine import Pin
import time

red = Pin(15, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_DOWN)

signal = ""
prev_signal = ""
NSFW_mode = False

while True:
    # Light up LEDs based on button/door states
    if NSFW_mode:
        red.value(1)
    else:
        red.value(0)

    if button.value():
        # Toggle NSFW_Mode
        NSFW_mode = not NSFW_mode
        signal = "NSFW" if NSFW_mode else "SFW"
        time.sleep(0.5)
    
    if signal != prev_signal:
        prev_signal = signal
        print(signal)
