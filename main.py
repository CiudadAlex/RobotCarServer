from commanders.KeyboardCommander import KeyboardCommander
from servers.ImageStreamServer import ImageStreamServer
from servers.TextStreamServer import TextStreamServer
from tools.Speech2TextListener import Speech2TextListener


if __name__ == '__main__2':

    print("######## Start ImageStreamServer")
    image_stream_server = ImageStreamServer()
    image_stream_server.start()

    print("######## Start KeyboardCommander")
    keyboard_commander = KeyboardCommander()
    keyboard_commander.start()


def action_on_text(text):
    print("You said: ", text)


speech_2_text_listener = Speech2TextListener(action_on_text)
speech_2_text_listener.start()


# text_stream_server = TextStreamServer()
# text_stream_server.start()

# import CommandServer

# FIXME Microphone server

# FIXME REST server on port 8080 with LED commands
# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

# FIXME try (arecord -l)
# /usr/share/alsa/alsa.conf
# defaults.ctl.card 2
# defaults.pcm.card 2

