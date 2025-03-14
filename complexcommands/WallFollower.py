from commanders.Commander import Commander
from tools.DataStorage import DataStorage
from sensors.ObstacleDetector import ObstacleDetector
import time


class WallFollower:

    AWAY_METERS = 0.3
    FORWARD_SECS = 0.7
    TURN_SECS = 0.12

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
            self.take_action(distance)

            # Let it recover and stop the ultrasound echoes
            time.sleep(0.15)

        DataStorage.get_instance().enabled_emergency_brake = True

    def take_action(self, distance):

        if distance > WallFollower.AWAY_METERS:
            Commander.execute_move_a_bit_forward(WallFollower.FORWARD_SECS)
            return

        Commander.execute_move_a_bit_right(WallFollower.TURN_SECS)


