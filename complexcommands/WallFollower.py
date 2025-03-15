from commanders.Commander import Commander
from tools.DataStorage import DataStorage
from sensors.ObstacleDetector import ObstacleDetector
import time
import threading


class WallFollower:

    CLOSE_METERS = 0.3
    FAR_AWAY_METERS = 1.0

    FORWARD_LONG_SECS = 0.7
    FORWARD_SHORT_SECS = 0.4

    TURN_LONG_SECS = 0.25
    TURN_SHORT_SECS = 0.12

    instance = None

    @staticmethod
    def get_instance():
        if WallFollower.instance is None:
            WallFollower.instance = WallFollower()
        return WallFollower.instance

    def __init__(self):
        self.running = False
        self.in_contact = False

    def stop(self):
        self.running = False

    def execute(self):
        thread = threading.Thread(target=self.execute_inner)
        thread.start()

    def execute_inner(self):

        self.running = True

        DataStorage.get_instance().enabled_emergency_brake = False

        while self.running:

            distance = ObstacleDetector.check_distance()
            self.take_action(distance)

            # Let it recover and stop the ultrasound echoes
            time.sleep(0.15)

        DataStorage.get_instance().enabled_emergency_brake = True

    def take_action(self, distance):

        if distance < WallFollower.CLOSE_METERS:
            self.in_contact = True

        if not self.in_contact:
            Commander.execute_move_a_bit_forward(WallFollower.FORWARD_LONG_SECS)
            return

        # in_contact is True
        if distance > WallFollower.FAR_AWAY_METERS:
            Commander.execute_move_a_bit_right(WallFollower.TURN_LONG_SECS)
            Commander.execute_move_a_bit_forward(WallFollower.FORWARD_SHORT_SECS)

        elif distance > WallFollower.CLOSE_METERS:
            Commander.execute_move_a_bit_right(WallFollower.TURN_SHORT_SECS)
            Commander.execute_move_a_bit_forward(WallFollower.FORWARD_SHORT_SECS)

        else:
            Commander.execute_move_a_bit_left(WallFollower.TURN_SHORT_SECS)
            Commander.execute_move_a_bit_forward(WallFollower.FORWARD_SHORT_SECS)

