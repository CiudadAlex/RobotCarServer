import threading
from actuators.LedStripChoreographer import LedStripChoreographer
import time


class LedStripManager:

    def __init__(self):

        self.ledStripChoreographer = LedStripChoreographer()
        self.func = None

        self.thread = threading.Thread(target=self.execute)
        self.thread.start()

    def execute(self):

        while True:

            if self.func is None:
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


