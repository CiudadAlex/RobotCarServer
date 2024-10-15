from threading import Thread
from actuators.LedStripChoreographer import LedStripChoreographer
import time


class LedStripManager(Thread):

    def __init__(self):
        super().__init__()
        self.ledStripChoreographer = LedStripChoreographer()
        self.func = None
        self.start()

    def run(self):

        while True:

            if self.func is None:
                self.ledStripChoreographer.black()
                time.sleep(0.5)
            else:
                self.func()

    def stop(self):
        self.func = None
        self.ledStripChoreographer.stop()

    def police(self):
        self.func = self.ledStripChoreographer.police
        self.ledStripChoreographer.stop()

    def alarm(self):
        self.func = self.ledStripChoreographer.alarm
        self.ledStripChoreographer.stop()

    def rainbow(self):
        self.func = self.ledStripChoreographer.rainbow
        self.ledStripChoreographer.stop()

    def breathe(self):
        self.func = self.ledStripChoreographer.breathe
        self.ledStripChoreographer.stop()

    def rainbow_flag(self):
        self.func = self.ledStripChoreographer.rainbow_flag
        self.ledStripChoreographer.stop()

