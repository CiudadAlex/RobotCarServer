python3 -m venv --system-site-packages .venv
source .venv/bin/activate

sudo apt install -y libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev
sudo apt install -y util-linux procps hostapd iproute2 iw haveged dnsmasq
sudo apt install -y python3-smbus
sudo apt install -y i2c-tools
sudo apt install -y libfreetype6-dev libjpeg-dev build-essential
sudo apt install -y python3-pyaudio
sudo apt install -y flac

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
sudo ./.venv/bin/pip3 install SpeechRecognition==3.10.4
sudo ./.venv/bin/pip3 install Flask==3.0.3
sudo ./.venv/bin/pip3 install webrtcvad==2.0.10
sudo ./.venv/bin/pip3 install pyttsx3==2.91

# Camera
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-picamera2

# Microphone
sudo apt install -y pulseaudio
sudo apt install -y jackd2

# Speak
sudo apt install -y espeak
sudo ./.venv/bin/pip3 install python-espeak==0.6.3

# Firewall
sudo apt install -y ufw
sudo ufw --force enable
sudo ufw allow 22
sudo ufw allow 8000
sudo ufw allow 8088
sudo ufw allow 7999
sudo ufw allow 7998

# Startup
cp ./RobotCarServer/start.sh .
cp ./RobotCarServer/stop_motor.sh .
sudo chmod 777 ./start.sh
sudo chmod 777 ./stop_motor.sh

sudo chmod 777 /etc/rc.local
sudo cp ./RobotCarServer/rc.local /etc

