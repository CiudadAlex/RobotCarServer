import Adafruit_PCA9685


class CameraTilt:
    """
    change this form 1 to 0 to reverse servos
    """
    look_direction = 1

    look_max = 500
    look_min = 100

    def __init__(self):

        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(50)

        self.org_pos = 300

    @staticmethod
    def ctrl_range(raw):
        if raw > CameraTilt.look_max:
            raw_output = CameraTilt.look_max
        elif raw < CameraTilt.look_min:
            raw_output = CameraTilt.look_min
        else:
            raw_output = raw
        return int(raw_output)

    def camera_ang(self, direction, ang):

        if ang == 'no':
            ang = 50
        if CameraTilt.look_direction:
            if direction == 'lookdown':
                self.org_pos += ang
                self.org_pos = self.ctrl_range(self.org_pos)
            elif direction == 'lookup':
                self.org_pos -= ang
                self.org_pos = self.ctrl_range(self.org_pos)
            elif direction == 'home':
                self.org_pos = 300
        else:
            if direction == 'lookdown':
                self.org_pos -= ang
                self.org_pos = self.ctrl_range(self.org_pos)
            elif direction == 'lookup':
                self.org_pos += ang
                self.org_pos = self.ctrl_range(self.org_pos)
            elif direction == 'home':
                self.org_pos = 300

        self.pwm.set_all_pwm(0, self.org_pos)

    def clean_all(self):
        self.pwm.set_all_pwm(0, 0)


