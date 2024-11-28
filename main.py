from commanders.KeyboardCommander import KeyboardCommander
from servers.ImageStreamServer import ImageStreamServer
from servers.AudioStreamServer import AudioStreamServer
from servers import CommandServer


if __name__ == '__main__2':

    print("######## Start CommandServer")
    CommandServer.run_server()

    print("######## Start ImageStreamServer")
    image_stream_server = ImageStreamServer()
    image_stream_server.start()

    print("######## Start AudioStreamServer")
    audio_stream_server = AudioStreamServer()
    audio_stream_server.start()

    print("######## Start KeyboardCommander")
    keyboard_commander = KeyboardCommander()
    keyboard_commander.start()


# FIXME test servo and motor
'''
from actuators.CameraTilt import CameraTilt
camera_tilt = CameraTilt()
camera_tilt.home()
'''

import time

from actuators.Motor import Motor
motor = Motor()
# motor.forward(100)

motor.motor_side_left(run=True, direction=0, speed=100)
motor.motor_side_right(run=True, direction=0, speed=100)

time.sleep(10)
motor.stop()

print("END______________________")


