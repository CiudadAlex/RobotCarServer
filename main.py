from commanders.KeyboardCommander import KeyboardCommander
from servers.ImageStreamServer import ImageStreamServer
from servers.AudioStreamServer import AudioStreamServer
from servers import CommandServer
from commanders.Commander import Commander
from background.EmergencyBrake import EmergencyBrake


if __name__ == '__main__':

    Commander.execute_move_stop()
    Commander.execute_led_stop()
    Commander.execute_look_home()

    print("######## Start CommandServer")
    CommandServer.run_server()

    print("######## Start ImageStreamServer")
    image_stream_server = ImageStreamServer()
    image_stream_server.start()

    print("######## Start AudioStreamServer")
    audio_stream_server = AudioStreamServer()
    audio_stream_server.start()

    print("######## Start EmergencyBrake")
    emergency_brake = EmergencyBrake(debug=True)
    emergency_brake.start()

    print("######## Start KeyboardCommander")
    keyboard_commander = KeyboardCommander()
    keyboard_commander.start()

