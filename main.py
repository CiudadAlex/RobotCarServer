from commanders.KeyboardCommander import KeyboardCommander
from camera_pi import Camera


if __name__ == '__main__':

    # keyboardCommander = KeyboardCommander()
    # keyboardCommander.start()

    camera = Camera()
    frame = camera.get_frame()

    with open("image.jpg", "wb") as binary_file:
        # Write bytes to file
        binary_file.write(frame)


# FIXME Camera
# FIXME Microphone


