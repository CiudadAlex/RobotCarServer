from servers.AbstractStreamServer import AbstractStreamServer, Item
from picamera2 import Picamera2
import time


class ImageStreamServer(AbstractStreamServer):

    def __init__(self):
        super().__init__(port=8000, check_collect_interval_millis=50, check_send_interval_millis=50)

        self.picam2 = Picamera2()
        camera_config = self.picam2.create_preview_configuration()
        self.picam2.configure(camera_config)

        self.picam2.start()
        time.sleep(2)

    def get_new_item_metadata_and_bytes(self):

        image = self.picam2.capture_image("main")

        image_bytes = image.tobytes()

        width, height = image.size
        str_item_metadata = str(width) + "," + str(height)
        item_metadata = bytes(str_item_metadata, 'utf-8')

        return item_metadata, image_bytes


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
