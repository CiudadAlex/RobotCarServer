from threading import Thread
import threading
import io
import socket
import struct
from PIL import Image
from picamera2 import Picamera2
from utils.TimeRegulator import TimeRegulator
import time


class ImageStreamServer(Thread):

    def __init__(self):
        super().__init__()
        self.last_image = None
        self.start()

    def run(self):
        thread_camera = threading.Thread(target=self.get_images_from_camera)
        thread_camera.start()

        server_socket = socket.socket()
        server_socket.bind(('0.0.0.0', 8000))
        server_socket.listen(0)

        while True:
            connection = server_socket.accept()[0].makefile('rb')
            thread_connection = threading.Thread(target=self.send_to_connection, args=(connection,))
            thread_connection.start()

    def get_images_from_camera(self):

        picam2 = Picamera2()

        camera_config = picam2.create_still_configuration()
        picam2.configure(camera_config)

        picam2.start()
        time.sleep(2)

        time_regulator = TimeRegulator(50)

        while True:

            self.last_image = picam2.capture_image("main")
            time_regulator.wait_until_next_milestone()

    def send_to_connection(self, connection):

        time_regulator = TimeRegulator(50)

        while True:
            # self.last_image
            time_regulator.wait_until_next_milestone()

            # FIXME finish


