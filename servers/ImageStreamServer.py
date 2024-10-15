from threading import Thread
import threading
import socket
import struct
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

            time_regulator.wait_until_next_milestone()

            if self.last_image is None:
                continue

            self.send_image_to_connection(self.last_image, connection)

    @staticmethod
    def send_image_to_connection(image, connection):

        image_bytes = image.tobytes()
        image_size = len(image_bytes)
        connection.sendall(struct.pack('>I', image_size))
        connection.sendall(image_bytes)


# FIXME check

'''
from PIL import Image
from io import BytesIO 
orig = Image.new(mode='RGBA', size=(240, 60))
image_bytes = orig.tobytes()
stream = BytesIO(image_bytes)
new = Image.frombytes('RGBA', (240,60), stream.getvalue())
'''

'''
import socket
import struct

def send_images(images):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)
    print("Server listening on port 12345")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    num_images = len(images)
    conn.send(str(num_images).encode())

    for image_path in images:
        with open(image_path, 'rb') as f:
            image_data = f.read()
            image_size = len(image_data)
            conn.sendall(struct.pack('>I', image_size))
            conn.sendall(image_data)
    
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]  # List your image paths here
    send_images(image_paths)
'''


'''
import socket
import struct

def receive_images():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('server_IP_address', 12345))

    num_images = int(client_socket.recv(1024).decode())
    for i in range(num_images):
        image_size = struct.unpack('>I', client_socket.recv(4))[0]
        image_data = b""
        while len(image_data) < image_size:
            packet = client_socket.recv(4096)
            if not packet:
                break
            image_data += packet
        
        image_name = f"received_image_{i}.jpg"
        with open(image_name, 'wb') as f:
            f.write(image_data)
        print(f"{image_name} received with size {image_size} bytes")
    
    client_socket.close()

if __name__ == "__main__":
    receive_images()
'''
