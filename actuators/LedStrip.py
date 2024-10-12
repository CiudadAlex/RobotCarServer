import time
from rpi_ws281x import *


class LedStrip:

    WHITE = Color(255, 255, 255)
    BLACK = Color(0, 0, 0)
    RED = Color(255, 0, 0)
    GREEN = Color(0, 255, 0)
    BLUE = Color(0, 0, 255)
    YELLOW = Color(255, 255, 0)
    MAGENTA = Color(255, 0, 255)
    CYAN = Color(0, 255, 255)
    ORANGE = Color(255, 128, 0)

    def __init__(self):
        self.LED_COUNT = 16        # Number of LED pixels.
        self.LED_PIN = 12          # GPIO pin connected to the pixels (18 uses PWM!).
        self.LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA = 10          # DMA channel to use for generating signal (try 10)
        self.LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
        self.LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
        self.LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()

    def set_color_componets(self, r, g, b, wait=0):
        """Wipe color across display a pixel at a time."""
        color = Color(r, g, b)
        self.set_color(color, wait)

    def set_color(self, color, wait=0):
        """Wipe color across display a pixel at a time."""
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait)

    def set_colors_list(self, list_colors):
        """Wipe color across display a pixel at a time."""
        max_item = min(len(list_colors), self.strip.numPixels())
        for i in range(max_item):
            self.strip.setPixelColor(i, list_colors[i])
            self.strip.show()

    def color_transition(self, r_start, g_start, b_start, r_end, g_end, b_end, steps, wait=0.05):

        for k in range(0, steps + 1):
            r = r_start + k * (r_end - r_start)/steps
            g = g_start + k * (g_end - g_start)/steps
            b = b_start + k * (b_end - b_start)/steps
            self.set_color_componets(int(r), int(g), int(b))
            time.sleep(wait)

