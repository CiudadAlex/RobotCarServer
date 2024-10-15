python3 -m venv .venv
source .venv/bin/activate

sudo apt-get install -y libqtgui4 libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqt4-test
sudo apt-get install -y util-linux procps hostapd iproute2 iw haveged dnsmasq
sudo apt-get install -y python3-smbus
sudo apt-get install -y i2c-tools
# sudo apt-get install -y python3-opencv
sudo apt-get install -y libfreetype6-dev libjpeg-dev build-essential

sudo ./.venv/bin/pip3 install RPi.GPIO==0.7.1
sudo ./.venv/bin/pip3 install adafruit-pca9685==1.0.1
sudo -H ./.venv/bin/pip3 install --upgrade luma.oled==3.13.0
sudo ./.venv/bin/pip3 install rpi_ws281x==5.0.0
sudo ./.venv/bin/pip3 install mpu6050-raspberrypi==1.2
sudo ./.venv/bin/pip3 install flask==3.0.3
sudo ./.venv/bin/pip3 install flask_cors==5.0.0
sudo ./.venv/bin/pip3 install websockets==13.1
sudo ./.venv/bin/pip3 install imutils==0.5.4
sudo ./.venv/bin/pip3 install zmq==0.0.0
sudo ./.venv/bin/pip3 install pybase64==1.4.0
sudo ./.venv/bin/pip3 install psutil==6.0.0


# sudo ./.venv/bin/pip3 install opencv-python==4.10.0.84
# sudo ./.venv/bin/pip3 install picamera==1.13

# sudo rpi-update

# sudo apt install -y python3-kms++
# sudo apt install -y python3-libcamera=v0.3.1+50-69a894c4
# sudo apt install -y libcamera-dev=v0.3.1+50-69a894c4
# sudo ./.venv/bin/pip3 install rpi-libcamera



# sudo apt install -y libcap-dev
# sudo apt install -y libavformat-dev libavfilter-dev libavdevice-dev libavcodec-dev ffmpeg
# sudo apt install -y libavutil-dev libswscale-dev libavresample-dev libopenmpi-dev
# sudo apt install -y python3-prctl libatlas-base-dev libopenjp2-7 python3-pip
# sudo apt install -y python3-picamera2

# sudo ./.venv/bin/pip3 install numpy --upgrade
# sudo ./.venv/bin/pip3 install libpcap==1.11.0b12
# sudo ./.venv/bin/pip3 install ffmpeg-python==0.2.0
# sudo ./.venv/bin/pip3 install av
# sudo ./.venv/bin/pip3 install picamera2

# sudo apt update
# sudo apt install --reinstall -y libraspberrypi0 libraspberrypi-dev libraspberrypi-doc libraspberrypi-bin
