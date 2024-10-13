from commanders.KeyboardCommander import KeyboardCommander
from time import sleep
from picamera2 import Picamera2


if __name__ == '__main__':

    # keyboardCommander = KeyboardCommander()
    # keyboardCommander.start()

    picam2 = Picamera2()
    picam2.start_and_capture_file("test.jpg")


# FIXME Camera
# FIXME Microphone


