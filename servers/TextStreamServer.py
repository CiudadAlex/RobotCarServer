from servers.AbstractStreamServer import AbstractStreamServer
from tools.Speech2TextListener import Speech2TextListener


class TextStreamServer(AbstractStreamServer):

    def __init__(self):
        super().__init__(port=8000, check_collect_interval_millis=500, check_send_interval_millis=500)

        self.speech_2_text_listener = Speech2TextListener(self.action_on_text)
        self.speech_2_text_listener.start()

        self.last_text = None

    def action_on_text(self, text):
        print("You said: ", text)
        self.last_text = text

    def get_new_item_metadata_and_bytes(self):

        if self.last_text is None:
            return None, None

        text_bytes = bytes(self.last_text, 'utf-8')
        item_metadata = bytes("Text", 'utf-8')

        self.last_text = None

        return item_metadata, text_bytes

