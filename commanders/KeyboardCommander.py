from managers.LedStripManager import LedStripManager


class KeyboardCommander:

    def __init__(self):
        self.ledStripManager = LedStripManager()

        self.command_map = {
            "led stop": self.ledStripManager.stop,
            "led police": self.ledStripManager.police,
            "led alarm": self.ledStripManager.alarm,
            "led rainbow": self.ledStripManager.rainbow,
            "led breathe": self.ledStripManager.breathe,
            "led rainbow_flag": self.ledStripManager.rainbow_flag
        }

    def start(self):

        while True:
            command = input("Insert command: ")

            if command not in self.command_map.keys():
                help()
            else:
                func = self.command_map[command]
                func()
                print("Executed")

    def help(self):
        print("Command list:")

        for command in self.command_map.keys():
            print(command)

