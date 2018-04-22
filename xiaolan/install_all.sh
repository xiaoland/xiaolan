#!/bin/bash
sudo apt-get install omxplayer pulseaudio fswebcam
sudo apt-get install cmake g++ gcc python2.7 python3
sudo apt-get install python-dev python3-dev python-pyaudio python3-pyaudio sox
su root
pip install pyaudio
pip install demjson requests hyper crypto
pip install MusicBoxApi==1.0.4
sudo apt-get install libatlas-base-dev
mv /home/pi/xiaolan-dev /home/pi/xiaolan
wget http://www.portaudio.com/archives/pa_stable_v190600_20161030.tgz
tar -zxvf pa_stable_v190600_20161030.tgz -C /home/pi/
sudo apt install libasound-dev
cd /home/pi/portaudio
./configure
make
sudo make install
su root
cp /home/pi/xiaolan/xiaolan/autostartxl /etc/init.d/
chmod +777 /etc/init.d/autostartxl
sudo update-rc.d autostartxl defaults
cd /home/pi/xiaolan/xiaolan
python xldo.py
