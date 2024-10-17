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


def action_on_text(text):
    print("You said: ", text)


speech_2_text_listener = Speech2TextListener(action_on_text)
speech_2_text_listener.start()


# FIXME Microphone server

