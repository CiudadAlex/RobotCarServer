from picamera2 import Picamera2
import time

if __name__ == '__main__':

    picam2 = Picamera2()

    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)

    picam2.start()

    for i in range(10):
        time.sleep(2)
        print("take photo")
        picam2.capture_file(f"test_photo_{i}.jpg")


# FIXME Camera server
# FIXME Microphone
# FIXME try: python3 -m venv --system-site-packages .venv

