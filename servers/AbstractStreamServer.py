from threading import Thread
import threading
import socket
import struct
from utils.TimeRegulator import TimeRegulator


class AbstractStreamServer(Thread):

    def __init__(self, port, check_collect_interval_millis, check_send_interval_millis):
        super().__init__()
        self.port = port
        self.check_collect_interval_millis = check_collect_interval_millis
        self.check_send_interval_millis = check_send_interval_millis
        self.last_item = None
        self.last_item_id = 0
        self.lock = threading.Lock()

    def get_last_item(self):

        with self.lock:
            return self.last_item

    def set_last_item(self, item):

        with self.lock:
            self.last_item = item

    def run(self):
        thread_collector = threading.Thread(target=self.collect_items)
        thread_collector.start()

        server_socket = socket.socket()
        server_socket.bind(('0.0.0.0', self.port))
        server_socket.listen(0)

        while True:
            connection = server_socket.accept()[0].makefile('rb')
            thread_sender = StreamSender(self, connection, self.check_send_interval_millis)
            thread_sender.start()

    def collect_items(self):

        time_regulator = TimeRegulator(self.check_collect_interval_millis)

        while True:
            item_id = self.last_item_id + 1
            item_metadata, item_bytes = self.get_new_item_metadata_and_bytes()

            item = Item(item_id, item_metadata, item_bytes)
            self.set_last_item(item)
            self.last_item_id = item_id

            time_regulator.wait_until_next_milestone()

    def get_new_item_metadata_and_bytes(self):
        raise NotImplementedError("The extending class should override the method 'get_new_item'")


class StreamSender(Thread):

    def __init__(self, stream_server, connection, check_send_interval_millis):
        super().__init__()
        self.last_item_id = None
        self.stream_server = stream_server
        self.connection = connection
        self.check_send_interval_millis = check_send_interval_millis

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
            self.send_item_bytes_to_connection(last_item.item_metadata, last_item.item_bytes, self.connection)

    @staticmethod
    def send_item_bytes_to_connection(item_metadata, item_bytes, connection):

        metadata_size = len(item_metadata)
        connection.sendall(struct.pack('>I', metadata_size))
        connection.sendall(item_metadata)

        item_size = len(item_bytes)
        connection.sendall(struct.pack('>I', item_size))
        connection.sendall(item_bytes)


class Item:

    def __init__(self, item_id, item_metadata, item_bytes):
        self.item_id = item_id
        self.item_metadata = item_metadata
        self.item_bytes = item_bytes


