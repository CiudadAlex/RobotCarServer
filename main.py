from commanders.KeyboardCommander import KeyboardCommander
from servers.ImageStreamServer import ImageStreamServer


if __name__ == '__main__':

    print("######## Start ImageStreamServer")
    imageStreamServer = ImageStreamServer()
    imageStreamServer.start()

    print("######## Start KeyboardCommander")
    keyboardCommander = KeyboardCommander()
    keyboardCommander.start()


# FIXME Camera server
# FIXME Microphone server


