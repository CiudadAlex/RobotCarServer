import RPi.GPIO as GPIO
import time


class ObstacleDetector:

    """
    Returns the distance in meters
    """
    @staticmethod
    def check_distance():

        Tr = 11
        Ec = 8

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Tr, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(Ec, GPIO.IN)
        GPIO.output(Tr, GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(Tr, GPIO.LOW)

        while not GPIO.input(Ec):
            pass

        t1 = time.time()
        while GPIO.input(Ec):
            pass

        t2 = time.time()

        return (t2-t1) * 340 / 2

