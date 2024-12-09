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
# FIXME obstacle detector

import time
from actuators.CameraTilt import CameraTilt
camera_tilt = CameraTilt()
camera_tilt.home()

time.sleep(3)
print("######## up")
camera_tilt.up()

time.sleep(3)
print("######## down")
camera_tilt.down()

time.sleep(3)
print("######## down")
camera_tilt.down()
