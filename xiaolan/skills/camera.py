#! /usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
import requests
import json
sys.path.append('/home/pi/xiaolan/xiaolan/')
import speaker
from stt import baidu_stt
from tts import baidu_tts
import snowboy
import recorder
# 此处的dht11已经被移到了raspberrypi_gpio.py技能中

#USB摄像头
class usbCamera(object):
	def __init__(self):
		pass
	def takePhoto(self):
	
		os.system('fswebcam  -r 1280x720 --no-banner /home/pi/xiaolan/xiaolan/img/img.jpg')
		speaker.kacha()
def init():
	global conn,cursor
	os.system('bash ./check.sh')
	s = smartHome()
	initDb()
	#humidity,temperature=s.readDth()
	#if humidity is not None and temperature is not None:
	#	if
	#释放资源
	conn.close()
	cursor.close();
	#uc = usbCamera()
	#uc.takePhoto()	
	

if __name__ =='__main__':
	init()
