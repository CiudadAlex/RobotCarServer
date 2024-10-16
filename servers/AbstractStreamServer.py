from threading import Thread
import threading
import socket
import struct
from utils.TimeRegulator import TimeRegulator
import time


class AbstractStreamServer(Thread):

    def __init__(self, port, check_send_interval_millis):
        super().__init__()
        self.port = port
        self.check_send_interval_millis = check_send_interval_millis
        self.last_item = None
        self.lock = threading.Lock()
        self.start()

    def get_last_item(self):

        with self.lock:
            return self.last_item

    def run(self):
        thread_camera = threading.Thread(target=self.get_images_from_camera)
        thread_camera.start()

        server_socket = socket.socket()
        server_socket.bind(('0.0.0.0', self.port))
        server_socket.listen(0)

        while True:
            connection = server_socket.accept()[0].makefile('rb')
            thread_connection = StreamSender(self, connection, self.check_send_interval_millis)
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


class StreamSender(Thread):

    def __init__(self, stream_server, connection, check_send_interval_millis):
        super().__init__()
        self.last_item_id = None
        self.stream_server = stream_server
        self.connection = connection
        self.check_send_interval_millis = check_send_interval_millis
        self.start()

    def run(self):

        time_regulator = TimeRegulator(self.check_send_interval_millis)

        while True:

            time_regulator.wait_until_next_milestone()

            last_item = self.stream_server.get_last_item()

            if last_item is None:
                continue

            if last_item.item_id == self.last_item_id:
                continue

            self.last_item_id = last_item.item_id
            self.send_item_bytes_to_connection(last_item.item_bytes, self.connection)

    @staticmethod
    def send_item_bytes_to_connection(item_bytes, connection):

        item_size = len(item_bytes)
        connection.sendall(struct.pack('>I', item_size))
        connection.sendall(item_bytes)

        # FIXME finish metadata


class Item:

    def __init__(self, item_id, item_bytes):
        self.item_id = item_id
        self.item_bytes = item_bytes

# FIXME finish




