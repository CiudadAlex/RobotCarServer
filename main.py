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

import sys
import time
from actuators.Motor import Motor

print(sys.argv)

'''
    Motor_A_EN = 4
    Motor_A_Pin1 = 26
    Motor_A_Pin2 = 21
    
    Motor_B_EN = 17
    Motor_B_Pin1 = 27
    Motor_B_Pin2 = 18
    
    -------------------------------
    
    Motor_A_EN = 4
    Motor_A_Pin1 = 14
    Motor_A_Pin2 = 15
    
    Motor_B_EN = 17
    Motor_B_Pin1 = 27
    Motor_B_Pin2 = 18

'''
'''
Motor.Motor_A_EN = 4
Motor.Motor_A_Pin1 = 14
Motor.Motor_A_Pin2 = 15

Motor.Motor_B_EN = 17
Motor.Motor_B_Pin1 = 27
Motor.Motor_B_Pin2 = 18


def print_motor_values():
    print(f"{Motor.Motor_A_EN} {Motor.Motor_A_Pin1} {Motor.Motor_A_Pin2} || {Motor.Motor_B_EN} {Motor.Motor_B_Pin1} {Motor.Motor_B_Pin2}")


for i in range(30):
    Motor.Motor_B_EN = i
    print_motor_values()
    motor = Motor()
    motor.forward(100)
    time.sleep(1)
    motor.stop()

print("END______________________")
'''

motor = Motor()
motor.forward(100)
time.sleep(5)
motor.stop()

print("END______________________")
