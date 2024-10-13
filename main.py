from commanders.KeyboardCommander import KeyboardCommander
from time import sleep
from picamera import PiCamera


if __name__ == '__main__':

    # keyboardCommander = KeyboardCommander()
    # keyboardCommander.start()

    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('foo.jpg')


# FIXME Camera
# FIXME Microphone


