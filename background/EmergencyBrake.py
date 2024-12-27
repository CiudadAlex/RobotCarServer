from sensors.ObstacleDetector import ObstacleDetector
from commanders.Commander import Commander
from threading import Thread


class EmergencyBrake(Thread):

    def __init__(self):
        super().__init__()
        self.active = True

    def run(self):

        while self.active:

            distance = ObstacleDetector.check_distance()
            if distance < 0.15:
                Commander.execute_move_stop()
                print("BRAKE!!!!!")
