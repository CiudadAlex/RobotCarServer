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

    def two_colors_alternate(self, color1, color2, time1, time2):

        self.active = True

        while self.active:

            try:
                self.strip.set_color(color1)
                time.sleep(time1)
                self.check_active()
                self.strip.set_color(color2)
                time.sleep(time2)
            except Exception:
                traceback.print_exc(file=sys.stdout)
                self.stop()

        self.strip.set_color(LedStrip.BLACK)

    def police(self):
        self.two_colors_alternate(LedStrip.RED, LedStrip.BLUE, 0.5, 0.5)

    def alarm(self):
        self.two_colors_alternate(LedStrip.WHITE, LedStrip.BLACK, 0.3, 0.3)

    def circular_transition_of_colors(self, list_tuples_color_components):

        self.active = True

        while self.active:

            try:
                last_tuple_color_components = None

                for tuple_color_components in list_tuples_color_components:

                    if last_tuple_color_components is None:
                        last_tuple_color_components = tuple_color_components
                        continue

                    t1 = last_tuple_color_components
                    t2 = tuple_color_components

                    self.strip.color_transition(t1[0], t1[1], t1[2], t2[0], t2[1], t2[2], 20, wait=0.05)
                    self.check_active()
                    last_tuple_color_components = tuple_color_components

            except Exception:
                traceback.print_exc(file=sys.stdout)
                self.stop()

        self.strip.set_color(LedStrip.BLACK)

    def rainbow(self):

        list_tuples_color_components = [
            (255, 0, 0),
            (255, 255, 0),
            (0, 255, 0),
            (0, 255, 255),
            (0, 0, 255),
            (255, 0, 255),
            (255, 0, 0)]
        self.circular_transition_of_colors(list_tuples_color_components)

    def breathe(self):

        list_tuples_color_components = [
            (255, 255, 255),
            (0, 0, 0),
            (255, 255, 255)]
        self.circular_transition_of_colors(list_tuples_color_components)

    def rainbow_flag(self):
        list_colors = [LedStrip.RED, LedStrip.ORANGE, LedStrip.YELLOW, LedStrip.GREEN, LedStrip.CYAN, LedStrip.BLUE]
        self.strip.set_colors_list(list_colors)

    def black(self):
        self.strip.set_color(LedStrip.BLACK)

    def red(self):
        self.strip.set_color(LedStrip.RED)

    def fading_color(self, r, g, b):
        self.strip.color_transition(r, g, b, 0, 0, 0, 20, wait=0.05)

    def fading_red(self):
        self.fading_color(255, 0, 0)

