from actuators.LedStrip import LedStrip
import time
import sys
import traceback


class LedStripChoreographer:

    def __init__(self):
        self.strip = LedStrip()
        self.active = False

    def stop(self):
        self.active = False

    def check_active(self):
        if not self.active:
            raise Exception("Interruption")

    def police(self):

        self.active = True

        while self.active:

            try:
                self.strip.set_color(LedStrip.RED)
                time.sleep(0.5)
                self.check_active()
                self.strip.set_color(LedStrip.BLUE)
                time.sleep(0.5)
            except Exception:
                traceback.print_exc(file=sys.stdout)
                self.stop()

        self.strip.set_color(LedStrip.BLACK)

    def rainbow(self):

        self.active = True

        while self.active:

            try:
                self.strip.color_transition(255,   0,   0, 255, 255,   0, 20, wait=0.05)
                self.check_active()
                self.strip.color_transition(255, 255,   0,   0, 255,   0, 20, wait=0.05)
                self.check_active()
                self.strip.color_transition(0,   255,   0,   0, 255, 255, 20, wait=0.05)
                self.check_active()
                self.strip.color_transition(0,   255, 255,   0,   0, 255, 20, wait=0.05)
                self.check_active()
                self.strip.color_transition(0,     0, 255, 255,   0, 255, 20, wait=0.05)
                self.check_active()
                self.strip.color_transition(255,   0, 255, 255,   0,   0, 20, wait=0.05)
                self.check_active()

            except Exception:
                traceback.print_exc(file=sys.stdout)
                self.stop()

        self.strip.set_color(LedStrip.BLACK)
