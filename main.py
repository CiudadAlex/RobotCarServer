# from commanders.KeyboardCommander import KeyboardCommander

from picamera2 import Picamera2
import time

if __name__ == '__main__':

    # keyboardCommander = KeyboardCommander()
    # keyboardCommander.start()

    picam2 = Picamera2()

    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)

    picam2.start()

    time.sleep(2)

    picam2.capture_file("test_photo.jpg")


# FIXME Camera server
# FIXME Microphone


