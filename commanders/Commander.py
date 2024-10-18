from managers.LedStripManager import LedStripManager
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

        self.command_map = {
            "led stop": self.ledStripManager.stop,
            "led police": self.ledStripManager.police,
            "led alarm": self.ledStripManager.alarm,
            "led rainbow": self.ledStripManager.rainbow,
            "led breathe": self.ledStripManager.breathe,
            "led rainbow_flag": self.ledStripManager.rainbow_flag,
            "exit": self.exit
        }

    @staticmethod
    def exit():
        os._exit(0)

    @staticmethod
    def execute(command):

        if command not in Commander.get_instance().command_map.keys():
            Commander.help_commands()
        else:
            func = Commander.get_instance().command_map[command]
            func()
            print("Executed")

    @staticmethod
    def help_commands():
        print("Command list:")

        for command in Commander.get_instance().command_map.keys():
            print(command)

