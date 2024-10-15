# from commanders.KeyboardCommander import KeyboardCommander

from picamera2 import Picamera2
# from time import sleep
# from picamera import PiCamera


if __name__ == '__main__':

    # keyboardCommander = KeyboardCommander()
    # keyboardCommander.start()

    picam2 = Picamera2()
    picam2.start_and_capture_file("test.jpg")

'''
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    sleep(2)
    camera.capture('foo.jpg')
'''

# FIXME Camera
# FIXME Microphone


