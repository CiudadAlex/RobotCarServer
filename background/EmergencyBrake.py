from sensors.ObstacleDetector import ObstacleDetector
from commanders.Commander import Commander
from threading import Thread


class EmergencyBrake(Thread):

    def __init__(self, debug=False):
        super().__init__()
        self.active = True
        self.debug = debug

    def run(self):

        while self.active:

            distance = ObstacleDetector.check_distance()

            if self.debug:
                print(f"distance = {distance}")

            if distance < 0.15:
                Commander.execute_move_stop()
                print("BRAKE!!!!!")
