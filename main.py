from commanders.KeyboardCommander import KeyboardCommander
from servers.ImageStreamServer import ImageStreamServer
from servers.AudioStreamServer import AudioStreamServer
from servers import CommandServer


if __name__ == '__main__2':

    print("######## Start CommandServer")
    CommandServer.run_server()

    print("######## Start ImageStreamServer")
    image_stream_server = ImageStreamServer()
    image_stream_server.start()

    print("######## Start AudioStreamServer")
    audio_stream_server = AudioStreamServer()
    audio_stream_server.start()

    print("######## Start KeyboardCommander")
    keyboard_commander = KeyboardCommander()
    keyboard_commander.start()


# FIXME test servo
# FIXME obstacle detector

print("######## Start KeyboardCommander")
keyboard_commander = KeyboardCommander()
keyboard_commander.start()

