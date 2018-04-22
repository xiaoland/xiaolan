#!/bin/bash
sudo apt-get install omxplayer pulseaudio fswebcam
sudo apt-get install cmake g++ gcc python2.7 python3
sudo apt-get install python-dev python3-dev python-pyaudio python3-pyaudio sox
pip install pyaudio
pip install requests hyper crypto
sudo apt-get install libatlas-base-dev
mv /home/pi/xiaolan-dev /home/pi/xiaolan
echo "请输入root账号的密码："
echo "如果输入完毕之后，停止了运行，在本脚本文件里找到本行，往下数第二行一直拖到最底复制带命令行中执行"
su root
cp /home/pi/xiaolan/xiaolan/autostartxl /etc/init.d/
chmod +777 /etc/init.d/autostartxl
sudo update-rc.d autostartxl defaults
cd /home/pi/xiaolan/xiaolan
python xldo.py
