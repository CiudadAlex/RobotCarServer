from servers.AbstractStreamServer import AbstractStreamServer
from tools.DataStorage import DataStorage


class TextCommandStreamServer(AbstractStreamServer):

    def __init__(self):
        super().__init__(port=7999, check_collect_interval_millis=500, check_send_interval_millis=500)

    def get_new_item_metadata_and_bytes(self):

        last_text_command = DataStorage.get_instance().last_text_command

        if last_text_command is None:
            return None, None

        text_bytes = bytes(last_text_command, 'utf-8')
        item_metadata = bytes("Text", 'utf-8')

        DataStorage.get_instance().last_text_command = None
        print(f"### Sending text command: {last_text_command}")

        return item_metadata, text_bytes

