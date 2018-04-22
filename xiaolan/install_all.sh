#!/bin/bash
sudo apt-get install omxplayer mplayer pulseaudio fswebcam
sudo apt-get install cmake g++ gcc python2.7 python3
sudo apt-get install python-dev python3-dev python-pyaudio python3-pyaudio sox
su root
pip install pyaudio
pip install demjson requests
pip install MusicBoxApi==1.0.4
sudo apt-get install libatlas-base-dev
mv /home/pi/xiaolan-dev /home/pi/xiaolan
su root
cp /home/pi/xiaolan/xiaolan/autostartxl /etc/init.d/
chmod +777 /etc/init.d/autostartxl
sudo update-rc.d autostartxl defaults
