from pi5neo import Pi5Neo

print("hello blinky!")

# Initialize the Pi5Neo class with 6 LEDs and an SPI speed of 800kHz
neo = Pi5Neo('/dev/spidev10.0', 6, 800)

# Fill the strip with a red color
neo.fill_strip(255, 0, 0)
neo.update_strip()  # Commit changes to the LEDs

# Set the 5th LED to blue
neo.set_led_color(4, 0, 0, 255)
neo.update_strip()
