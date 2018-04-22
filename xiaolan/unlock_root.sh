#! /bin/bash
echo "请设置root账户密码"
sudo passwd root
sudo passwd --unlock root
echo "输入设置好的root密码
su root
chmod 777 /home/pi/xiaolan-dev/xiaolan/install_all.sh
