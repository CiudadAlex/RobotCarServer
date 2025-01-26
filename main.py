from commanders.KeyboardCommander import KeyboardCommander
from servers.ImageStreamServer import ImageStreamServer
from servers.AudioStreamServer import AudioStreamServer
from servers.TextCommandStreamServer import TextCommandStreamServer
from servers import CommandServer
from commanders.Commander import Commander
from background.EmergencyBrake import EmergencyBrake
import time


def init():

    Commander.execute_move_stop()
    Commander.execute_led_stop()
    Commander.execute_look_home()

    time.sleep(0.2)
    Commander.execute_look_up()
    time.sleep(0.2)
    Commander.execute_look_up()


if __name__ == '__main__':

    init()

    print("######## Start CommandServer")
    CommandServer.run_server()

    print("######## Start ImageStreamServer")
    image_stream_server = ImageStreamServer()
    image_stream_server.start()

    print("######## Start AudioStreamServer")
    audio_stream_server = AudioStreamServer()
    audio_stream_server.start()

    print("######## Start TextCommandStreamServer")
    text_command_stream_server = TextCommandStreamServer()
    text_command_stream_server.start()

    print("######## Start EmergencyBrake")
    emergency_brake = EmergencyBrake()
    emergency_brake.start()

    print("######## Start KeyboardCommander")
    keyboard_commander = KeyboardCommander()
    keyboard_commander.start()

