import Adafruit_PCA9685
import time


class CameraTilt:
    """
    change this form 1 to -1 to reverse servos
    """
    look_direction = 1

    look_max = 500
    look_min = 100
    look_home = 300

    def __init__(self):

        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(50)

        self.current_pos = CameraTilt.look_home

    @staticmethod
    def ctrl_range(raw):
        if raw > CameraTilt.look_max:
            raw_output = CameraTilt.look_max
        elif raw < CameraTilt.look_min:
            raw_output = CameraTilt.look_min
        else:
            raw_output = raw
        return int(raw_output)

    def add_angle_to_tilt(self, ang):
        self.current_pos += ang
        self.current_pos = self.ctrl_range(self.current_pos)
        self.pwm.set_all_pwm(0, self.current_pos)

    def home(self):
        self.current_pos = CameraTilt.look_home
        self.pwm.set_all_pwm(0, self.current_pos)
        time.sleep(0.2)
        self.clean_all()

    def up(self):
        self.add_angle_to_tilt(50 * CameraTilt.look_direction)

    def down(self):
        self.add_angle_to_tilt(-50 * CameraTilt.look_direction)

    def clean_all(self):
        self.pwm.set_all_pwm(0, 0)


