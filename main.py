from actuators.LED import LED
import time
from rpi_ws281x import *

if __name__ == '__main__':
    for i in range(10):
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

led.colorWipe(Color(0,0,0))
