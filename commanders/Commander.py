from managers.LedStripManager import LedStripManager
from actuators.Motor import Motor
import os


class Commander:

    instance = None

    @staticmethod
    def get_instance():
        if Commander.instance is None:
            Commander.instance = Commander()
        return Commander.instance

    def __init__(self):
        self.ledStripManager = LedStripManager()
        self.motor = Motor()

        self.command_map = {
            "led stop": self.ledStripManager.stop,
            "led police": self.ledStripManager.police,
            "led alarm": self.ledStripManager.alarm,
            "led rainbow": self.ledStripManager.rainbow,
            "led breathe": self.ledStripManager.breathe,
            "led rainbow_flag": self.ledStripManager.rainbow_flag,
            "move forward": self.motor.forward,

            "move backward": self.motor.backward,
            "move turn_forward_left": self.motor.turn_forward_left,
            "move turn_forward_right": self.motor.turn_forward_right,
            "move turn_backward_left": self.motor.turn_backward_left,
            "move turn_backward_right": self.motor.turn_backward_right,
            "move turn_left": self.motor.turn_left,
            "move turn_right": self.motor.turn_right,
            "move stop": self.motor.stop,

            "exit": self.exit
        }

    @staticmethod
    def exit():
        os._exit(0)

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
    def help_commands():
        print("Command list:")

        for command in Commander.get_instance().command_map.keys():
            print(command)

