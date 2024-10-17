from commanders.KeyboardCommander import KeyboardCommander
from servers.ImageStreamServer import ImageStreamServer
from tools.Speech2TextListener import Speech2TextListener


if __name__ == '__main__2':

    print("######## Start ImageStreamServer")
    imageStreamServer = ImageStreamServer()
    imageStreamServer.start()

    print("######## Start KeyboardCommander")
    keyboardCommander = KeyboardCommander()
    keyboardCommander.start()


def speak_text(my_text):
    print("You said: ", my_text)


speech_2_text_listener = Speech2TextListener(speak_text)
speech_2_text_listener.start()


# FIXME Microphone server

