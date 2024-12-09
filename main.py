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

'''
from actuators.CameraTilt import CameraTilt
camera_tilt = CameraTilt()
camera_tilt.home()
'''

from actuators.Motor import Motor

motor = Motor()
motor.stop()

while True:
    print("Waiting command")
    input = input()

    if input == "w":
        motor.forward(100)
    elif input == "s":
        motor.backward(100)
    elif input == "a":
        motor.turn_forward_left(100, 0.5)
    elif input == "d":
        motor.turn_forward_right(100, 0.5)
    elif input == "e":
        motor.stop()
    elif input == "q":
        break

    print(f"Command '{input}' executed")


print("END______________________")
