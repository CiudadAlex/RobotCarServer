from commanders.KeyboardCommander import KeyboardCommander
from servers.ImageStreamServer import ImageStreamServer
from servers.AudioStreamServer import AudioStreamServer


if __name__ == '__main__2':

    print("######## Start ImageStreamServer")
    image_stream_server = ImageStreamServer()
    image_stream_server.start()

    print("######## Start KeyboardCommander")
    keyboard_commander = KeyboardCommander()
    keyboard_commander.start()


def action_on_text(text):
    print("######## You said: ", text)


audio_stream_server = AudioStreamServer()
audio_stream_server.start()

# import CommandServer

# FIXME test AudioStreamServer
# FIXME test server LED commands


