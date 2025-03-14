from commanders.Commander import Commander
from tools.DataStorage import DataStorage
from sensors.ObstacleDetector import ObstacleDetector
import time


class WallFollower:

    instance = None

    @staticmethod
    def get_instance():
        if WallFollower.instance is None:
            WallFollower.instance = WallFollower()
        return WallFollower.instance

    def __init__(self):
        self.running = False

    def stop(self):
        self.running = False

    def execute(self):
        self.running = True

        DataStorage.get_instance().enabled_emergency_brake = False

        while self.running:

            distance = ObstacleDetector.check_distance()

            Commander.execute_move_stop()

            # Let it recover and stop the ultrasound echoes
            time.sleep(0.15)

        DataStorage.get_instance().enabled_emergency_brake = True


