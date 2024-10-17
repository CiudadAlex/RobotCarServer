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

        start = time.time()

        image = self.picam2.capture_image("main")
        rgb_image = image.convert('RGB')

        buffered_rgb_image = io.BytesIO()
        rgb_image.save(buffered_rgb_image, format="PNG", optimize=True)

        # FIXME check not working
        print(buffered_rgb_image)
        print(buffered_rgb_image.getbuffer().nbytes)

        image_bytes = buffered_rgb_image.getvalue()

        # FIXME check not working
        print(image_bytes)
        print(len(image_bytes))

        width, height = rgb_image.size
        str_item_metadata = str(width) + "," + str(height)
        item_metadata = bytes(str_item_metadata, 'utf-8')

        end = time.time()
        print(f"millis = {1000 * (end - start)}")

        return item_metadata, image_bytes

