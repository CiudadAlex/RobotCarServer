from commanders.KeyboardCommander import KeyboardCommander
from servers.ImageStreamServer import ImageStreamServer
from servers.TextStreamServer import TextStreamServer
from tools.Speech2TextProcessor import Speech2TextProcessor


if __name__ == '__main__2':

    print("######## Start ImageStreamServer")
    image_stream_server = ImageStreamServer()
    image_stream_server.start()

    print("######## Start KeyboardCommander")
    keyboard_commander = KeyboardCommander()
    keyboard_commander.start()


def action_on_text(text):
    print("You said: ", text)


record_secs = 10     # record time
speech_2_text_processor = Speech2TextProcessor()
speech_2_text_processor.store_and_recognize_audio(record_secs, action_on_text)


# text_stream_server = TextStreamServer()
# text_stream_server.start()

# import CommandServer

# FIXME Microphone server
# FIXME test server LED commands


