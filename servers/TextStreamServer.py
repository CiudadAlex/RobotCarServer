from servers.AbstractStreamServer import AbstractStreamServer
from tools.Speech2TextListener import Speech2TextListener


class TextStreamServer(AbstractStreamServer):

    def __init__(self):
        super().__init__(port=8000, check_collect_interval_millis=500, check_send_interval_millis=500)

        self.speech_2_text_listener = Speech2TextListener(self.action_on_text)
        self.speech_2_text_listener.start()

    @staticmethod
    def action_on_text(text):
        print("You said: ", text)

    def get_new_item_metadata_and_bytes(self):

        image = self.picam2.capture_image("main")
        image_bytes = image.tobytes()

        width, height = image.size
        str_item_metadata = str(width) + "," + str(height)
        item_metadata = bytes(str_item_metadata, 'utf-8')

        return item_metadata, image_bytes