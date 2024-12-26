from sensors.ObstacleDetector import ObstacleDetector
from actuators.Motor import Motor
from threading import Thread


class EmergencyBrake(Thread):

    def __init__(self):
        super().__init__()
        self.active = True
        self.motor = Motor()

    def run(self):

        while self.active:

            distance = ObstacleDetector.check_distance()
            if distance < 0.15:
                self.motor.stop()
                print("BRAKE!!!!!")
