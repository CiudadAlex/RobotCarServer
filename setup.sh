python3 -m venv .venv
source .venv/bin/activate

sudo ./.venv/bin/pip3 install RPi.GPIO
sudo ./.venv/bin/pip3 install adafruit-pca9685
sudo -H ./.venv/bin/pip3 install --upgrade luma.oled
sudo ./.venv/bin/pip3 install rpi_ws281x
sudo ./.venv/bin/pip3 install mpu6050-raspberrypi
sudo ./.venv/bin/pip3 install flask
sudo ./.venv/bin/pip3 install flask_cors
sudo ./.venv/bin/pip3 install websockets
sudo ./.venv/bin/pip3 install imutils zmq pybase64 psutil
sudo ./.venv/bin/pip3 install opencv-python

