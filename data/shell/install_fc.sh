#!/bin/bash
su
dnf install git cmake g++ gcc python3-devel.x86_64 make ffmpeg pulseaudio.x86_64 fswebcam.x86_64 sox.x86_64
git clone https://github.com/popcornmix/omxplayer.git
./prepare-native-raspbian.sh
pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple pip -U
pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple
pip install PyAudio sox
pip install pyaudio sendmail
pip install requests hyper crypto
mv /home/pi/xiaolan-dev /home/pi/xiaolan
echo "请输入root账号的密码："
echo "如果输入完毕之后，停止了运行，在本脚本文件里找到本行，往下数第二行一直拖到最底复制带命令行中执行"
su root
cp /home/pi/xiaolan/xiaolan/autostartxl /etc/init.d/
chmod +777 /etc/init.d/autostartxl
sudo update-rc.d autostartxl defaults
cd /home/pi/xiaolan/xiaolan
python xldo.py b
