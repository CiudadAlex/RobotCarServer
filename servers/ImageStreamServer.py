from servers.AbstractStreamServer import AbstractStreamServer, Item
from picamera2 import Picamera2
import time
import io


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

        buffered_image = io.BytesIO()
        image.save(buffered_image, format="PNG", optimize=True)
        image_bytes = buffered_image.read()

        width, height = image.size
        str_item_metadata = str(width) + "," + str(height)
        item_metadata = bytes(str_item_metadata, 'utf-8')

        return item_metadata, image_bytes

