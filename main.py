from commanders.KeyboardCommander import KeyboardCommander
from servers.ImageStreamServer import ImageStreamServer
# from servers.TextStreamServer import TextStreamServer
from tools.Speech2TextProcessor import Speech2TextProcessor


if __name__ == '__main__2':

    print("######## Start ImageStreamServer")
    image_stream_server = ImageStreamServer()
    image_stream_server.start()

    print("######## Start KeyboardCommander")
    keyboard_commander = KeyboardCommander()
    keyboard_commander.start()


def action_on_text(text):
    print("######## You said: ", text)


speech_2_text_processor = Speech2TextProcessor(interval_record_secs=5, function_with_recognized_text=action_on_text)
speech_2_text_processor.start()


# text_stream_server = TextStreamServer()
# text_stream_server.start()

# import CommandServer

# FIXME test Microphone server
# FIXME test server LED commands


