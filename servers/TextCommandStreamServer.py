from servers.AbstractStreamServer import AbstractStreamServer
from tools.Speech2TextProcessor import Speech2TextProcessor


class TextCommandStreamServer(AbstractStreamServer):

    def __init__(self):
        super().__init__(port=7999, check_collect_interval_millis=500, check_send_interval_millis=500)

        self.speech_2_text_processor = Speech2TextProcessor(interval_record_secs=5, function_with_recognized_text=self.action_on_text)
        self.speech_2_text_processor.start()

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

