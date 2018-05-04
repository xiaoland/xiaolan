# -*- coding: utf-8 -*-
''' 智能家居技能（尚未完善，大家一起加油，用函数哦)  '''
import json
import sys
import os
import requests
import demjson
import time
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder
import speaker

def start(tok):
	
	h = hass()
	hass.start(tok)

class hass(object):
	def __init__(self):
		
		pass
	
	def start(self, tok):
		 
		bt = baidu_tts()
		bs = baidu_stt(1, 2, 3, 4)
		r = recorder()
		h = hass()
		welcome = '欢迎使用小蓝专用智能家居控制系统！请在，滴，一声之后说出指令'
		
		bt.tts(welcome, tok)
		speaker.speak()
		speaker.ding()
		r.record()
		speaker.dong()
		text = bs.stt('./voice.wav', tok)
		
		while text == None:
			sorry = '对不起，我没有听清楚，请重复一遍'
			bt.tts(sorry, tok)
			speaker.speak()
			speaker.ding()
			r.record()
			speaker.speak()
			text = bs.stt('./voice.wav', tok)
			if text != None:
				break
		if '打开' in text:
			cortolthings = text[2:-1]
			cortolmode = 'turn_on'
			h.cortol(cortolthings, cortolmode, tok)
		elif '关闭' in text:
			cortolthings = text[2:-1]
			cortolmode = 'turn_off'
			h.cortol(cortolthings, cortolmode, tok)
		elif '查看' in text:
			if '传感器' in text:
				getstatethings = text[2:-4]
				getmode = 'sensor'
				h.sensor(getstatethings, getmode, tok)
			elif '插座' in text:
				getstatethings = text[2:-4]
				getmode = 'switchs'
				h.sensor(getstatethings, getmode, tok)
			elif '灯' in text:
				getstatethings = text[2:-4]
				getmode = 'light'
				h.sensor(getstatethings, getmode, tok, e_id)
		else:
			h.usuallycortol(text, tok)
		
	def cortol(cortolthings, cortolmode, tok):
		 	
		url = 'http://hassio.local:'
		port = '8123'
		passwd = 'y20050801'
		bt = baidu_tts()
		bs = baidu_stt(1, 2, 3, 4)
		r = recorder()
		h = hass()
		
		
		
		
		
		
		
		
			
			
			
			
			
			
