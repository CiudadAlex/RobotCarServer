from actuators import LED
import time
from rpi_ws281x import *

if __name__ == '__main__':
    while True:
        led = LED()
        try:
            led.colorWipe(Color(255,0,0))
            time.sleep(1)
            led.colorWipe(Color(0,255,0))
            time.sleep(1)
            led.colorWipe(Color(0,0,255))
            time.sleep(1)
        except:
            led.colorWipe(Color(0,0,0))
