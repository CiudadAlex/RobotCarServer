from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero import Device, LED
from time import sleep

Device.pin_factory = LGPIOFactory()

print("hello blinky!")

led = LED(18)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
