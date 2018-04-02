#! /usr/bin/python
# -*- coding: UTF-8 -*-
''' 摄像头 '''
import json
import sys
import os
import requests
import pygame
import time
sys.path.append('/home/pi/xiaolan/xiaolan/')
import stt
import tts
import snowboy
import recorder
import speaker
__author__ = 'Caibiy'

import Adafruit_DHT,os,time,datetime,sqlite3
conn,cursor=(None,None)

def start():
	u = usbCamera()
	u.tskePhoto()
	
#USB摄像头
class usbCamera(object):
	def __init__(self):
		pass
	def takePhoto(self):
		speaker.kacha()
		nowTime = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
		os.system('fswebcam  -r 1280x720 --no-banner ../img/%s.jpg' % nowTime)
		executeDb('insert into pic (time) VALUES (\'%s\') ' %  nowTime)
def init():
	os.system('bash ./check.sh')
	s = smartHome(23,11,21)
	initDb()
	#uc = usbCamera()
	#uc.takePhoto()	
	cursor.execute('select * from pic')
	print(cursor.fetchall())

if __name__ =='__main__':
	init()
