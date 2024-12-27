from managers.LedStripManager import LedStripManager
from actuators.Motor import Motor
from actuators.CameraTilt import CameraTilt
from servers.AudioStreamServer import AudioStreamServer
import os
import time


class Commander:

    COMMAND_LED_STOP = "led stop"
    COMMAND_LED_POLICE = "led police"
    COMMAND_LED_ALARM = "led alarm"
    COMMAND_LED_RAINBOW = "led rainbow"
    COMMAND_LED_BREATHE = "led breathe"
    COMMAND_LED_RAINBOW_FLAG = "led rainbow_flag"
    COMMAND_LED_RED = "led red"
    COMMAND_LED_FADING_RED = "led fading_red"

    COMMAND_MOVE_FORWARD = "move forward"
    COMMAND_MOVE_BACKWARD = "move backward"
    COMMAND_MOVE_TURN_FORWARD_LEFT = "move turn_forward_left"
    COMMAND_MOVE_TURN_FORWARD_RIGHT = "move turn_forward_right"
    COMMAND_MOVE_TURN_BACKWARD_LEFT = "move turn_backward_left"
    COMMAND_MOVE_TURN_BACKWARD_RIGHT = "move turn_backward_right"
    COMMAND_MOVE_TURN_LEFT = "move turn_left"
    COMMAND_MOVE_TURN_RIGHT = "move turn_right"
    COMMAND_MOVE_STOP = "move stop"

    COMMAND_LOOK_UP = "look up"
    COMMAND_LOOK_DOWN = "look down"
    COMMAND_LOOK_HOME = "look home"

    COMMAND_LISTEN_ON = "listen on"
    COMMAND_LISTEN_OFF = "listen off"

    COMMAND_EXIT = "exit"

    instance = None

    @staticmethod
    def get_instance():
        if Commander.instance is None:
            Commander.instance = Commander()
        return Commander.instance

    def __init__(self):
        self.ledStripManager = LedStripManager()
        self.motor = Motor()
        self.camera_tilt = CameraTilt()

        self.command_map = {
            Commander.COMMAND_LED_STOP: self.ledStripManager.stop,
            Commander.COMMAND_LED_POLICE: self.ledStripManager.police,
            Commander.COMMAND_LED_ALARM: self.ledStripManager.alarm,
            Commander.COMMAND_LED_RAINBOW: self.ledStripManager.rainbow,
            Commander.COMMAND_LED_BREATHE: self.ledStripManager.breathe,
            Commander.COMMAND_LED_RAINBOW_FLAG: self.ledStripManager.rainbow_flag,
            Commander.COMMAND_LED_RED: self.ledStripManager.red,
            Commander.COMMAND_LED_FADING_RED: self.ledStripManager.fading_red,

            Commander.COMMAND_MOVE_FORWARD: self.motor.forward,
            Commander.COMMAND_MOVE_BACKWARD: self.motor.backward,
            Commander.COMMAND_MOVE_TURN_FORWARD_LEFT: self.motor.turn_forward_left,
            Commander.COMMAND_MOVE_TURN_FORWARD_RIGHT: self.motor.turn_forward_right,
            Commander.COMMAND_MOVE_TURN_BACKWARD_LEFT: self.motor.turn_backward_left,
            Commander.COMMAND_MOVE_TURN_BACKWARD_RIGHT: self.motor.turn_backward_right,
            Commander.COMMAND_MOVE_TURN_LEFT: self.motor.turn_left,
            Commander.COMMAND_MOVE_TURN_RIGHT: self.motor.turn_right,
            Commander.COMMAND_MOVE_STOP: self.motor.stop,

            Commander.COMMAND_LOOK_UP: self.camera_tilt.up,
            Commander.COMMAND_LOOK_DOWN: self.camera_tilt.down,
            Commander.COMMAND_LOOK_HOME: self.camera_tilt.home,

            Commander.COMMAND_LISTEN_ON: self.listen_on,
            Commander.COMMAND_LISTEN_OFF: self.listen_off,

            Commander.COMMAND_EXIT: self.exit
        }

    @staticmethod
    def exit():
        os._exit(0)

    @staticmethod
    def listen_on():
        AudioStreamServer.listening = True

    @staticmethod
    def listen_off():
        AudioStreamServer.listening = False

    @staticmethod
    def execute(command):

        if command not in Commander.get_instance().command_map.keys():
            Commander.help_commands()
            return False
        else:
            func = Commander.get_instance().command_map[command]
            func()
            print("Executed")
            return True

    @staticmethod
    def execute_move_stop():
        return Commander.execute(Commander.COMMAND_MOVE_STOP)

    @staticmethod
    def execute_led_stop():
        return Commander.execute(Commander.COMMAND_LED_STOP)

    @staticmethod
    def execute_look_home():
        return Commander.execute(Commander.COMMAND_LOOK_HOME)

    @staticmethod
    def execute_move_a_bit_forward(secs):
        return Commander.execute_move_for_given_seconds(Commander.COMMAND_MOVE_FORWARD, secs)

    @staticmethod
    def execute_move_a_bit_backward(secs):
        return Commander.execute_move_for_given_seconds(Commander.COMMAND_MOVE_BACKWARD, secs)

    @staticmethod
    def execute_move_a_bit_left(secs):
        return Commander.execute_move_for_given_seconds(Commander.COMMAND_MOVE_TURN_LEFT, secs)

    @staticmethod
    def execute_move_a_bit_right(secs):
        return Commander.execute_move_for_given_seconds(Commander.COMMAND_MOVE_TURN_RIGHT, secs)

    @staticmethod
    def execute_move_for_given_seconds(command, secs):
        Commander.execute(command)
        time.sleep(secs)
        Commander.execute(Commander.COMMAND_MOVE_STOP)
        return True

    @staticmethod
    def help_commands():
        print("Command list:")

        for command in Commander.get_instance().command_map.keys():
            print(command)

