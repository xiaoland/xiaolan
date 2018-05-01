# -*- coding: utf-8 -*-
''' 智能家居技能（尚未完善，大家一起加油，用函数哦)  '''
import json
import sys
import os
import requests
import pygame
import time
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import recorder
import speaker

password = 'y20050801056'

def start(cortolthings, platfrom):
	h = smartHome()
	h.start(platfrom)
	
def keyvalue_all(self,input_json):  
    key_value=''  
    if isinstance(input_json,dict):  
        for key in input_json.keys():  
            key_value = input_json.get(key)  
            if isinstance(key_value,dict):  
                self.print_keyvalue_all(key_value)  
            elif isinstance(key_value,list):  
                for json_array in key_value:  
                    self.print_keyvalue_all(json_array)  
            else:  
                print str(key)+" = "+str(key_value)  
    elif isinstance(input_json,list):  
        for input_json_array in input_json:  
            self.print_keyvalue_all(input_json_array)  
	
#主控包含传感器、蜂鸣器
class smartHome(object):
	def __init__(self,sensors,cortolswitch,cortollight,cortolinent,entyid):
		self.sensors = sensors
		self.cortollight = cortollight
		self.cortolswitch = cortolswitch
		self.cortolinent = cortolinent
		self.entyid = entyid

	
	def main(self, platfrom):
		if platfrom == '':
			h = smartHome()
			ask = "请在滴一声之后，说出指令"
			baidu_tts.tts(ask)
			speaker.speak()
			speaker.ding()
			recorder.record()
			speaker.dong()
			baidu_stt.stt()
			baidu_stt.nlp()
			inent = cortolinent
			if "灯" in parsed_text:
				h.hasslights(cortollight)
			elif "开关" in parsed_text:
				back = cortolswitch
				h.hassswitchs(cortolswitch)
			elif "获取" in parsed_text:
				asks = "您要获取传感器的数据还是灯或插头的状态"
				baidu_tts.tts(asks)
				speaker.speak()
				speaker.ding()
				recorder.record()
				speaker.dong()
				baidu_stt.stt()
				if "灯" in text:
					ty = 1
					h.hasssensor(ty)
				elif "插头" in text:
					ty = 2
					h.hasssensor(ty)
				elif "传感器" in text:
					ty = 3
					h.hasssensor(ty)
			
			
			
			
    	#蜂鸣器（raspberrypi)
	def buzzer(self):
		os.system('gpio -g write %s 1' % self.__pbuzzer)
		time.sleep(0.5)
		os.system('gpio -g write %s 0' % self.__pbuzzer)
	
	#温湿度读取（DHT11）
	def readDth(self):
		humidity,temperature = Adafruit_DHT.read_retry(self.sensor,self.__pdht11)
		if humidity is not None and temperature is not None:
			print('temp:%s,humidity%d' % (humidity,temperature))
			return (humidity,temperature)
	
	#灯类控制Homeassistant
	def hasslight(cortollight):
		url = '192.168.2.110'
		apikey = 'y20050801056'
		if cortollight == '':
			askf = "您想要控制什么灯?，请在滴一声之后说出，开，或，关，加上，名称"
			baidu_tts.tts(askf)
			speaker.speak()
			speaker.ding()
			recorder.record()
			speaker.dong()
			baidu_stt.stt()
			
		headers = {'x-ha-access': password, 'content-type': 'application/json'}
    		r = requests.get("192.168.2.110:8123/api/services", headers=headers)
		json = r.json()
		services = keyvalue_all(1, json)
		
		if cortolinent == 'open':
			pass
		elif cortolinent == 'close':
			pass
	
	#开关控制（homeassistant)
	def hassswitchs(cortolswitch):
		domain = "switch"
		url = '192.168.2.110'
		apikey = 'y20050801056'
		if cortolswitch == '':
			askt = "您想要控制什么开关?，请在滴一声之后说出，开，或，关，加上，名称"
			baidu_tts.tts(askt)
			speaker.speak()
			speaker.ding()
			recorder.record()
			speaker.dong()
			baidu_stt.stt()
			
		headers = {'x-ha-access': password, 'content-type': 'application/json'}
    		r = requests.get("192.168.2.110:8123/api/services", headers=headers)
		json = r.json()
		services = keyvalue_all(1, json)
		
		if cortolinent == 'open':
			pass
		elif cortolinent == 'close':
			pass

	
	#设备数据/状态获取(homeassistant)
	def hasssensor(ty):
		url = 'http://192.168.2.110'
		apikey = 'y20050801056'
		if ty == 1:
			askf = "您想要获取哪个开关的状态？"
			baidu_tts.tts(askf)
			speaker.speak()
			speaker.ding()
			recorder.record()
			speaker.dong()
			baidu_stt.stt()
			text = switch
			
			headers = {'x-ha-access': password, 'content-type': 'application/json'}
    			r = requests.get("192.168.2.110:8123/api/services", headers=headers)
			json = r.json()
			services = keyvalue_all(1, json)
			
			if switch_states == 'on':
				saytext = "该插座为打开状态"
				baidu_tts.tts(saytext)
				speaker.speak()
			elif switch_states == 'off':
				saytext = "该插座状态为关闭"
				baidu_tts.tts(saytext)
				speaker.speak()
		elif ty == 3:
			askf = "您想要获取哪个传感器的状态？"
			baidu_tts.tts(askf)
			speaker.speak()
			speaker.ding()
			recorder.record()
			speaker.dong()
			baidu_stt.stt()
			text = sensor
			
			headers = {'x-ha-access': password, 'content-type': 'application/json'}
    			r = requests.get("192.168.2.110:8123/api/services", headers=headers)
			json = r.json()
			service = keyvalue_all(1, json)
			
			saytext = "该传感器的数据为" + sensor_states
			baidu_tts.tts(saytext)
			speaker.speak()
		elif ty == 2:
			askf = "您想要获取哪个灯的状态？"
			baidu_tts.tts(askf)
			speaker.speak()
			speaker.ding()
			recorder.record()
			speaker.dong()
			baidu_stt.stt()
			text = light
			
			if light_states == 'on':
				saytext = "该灯为打开状态"
				baidu_tts.tts(saytext)
				speaker.speak()
			elif light_states == 'off':
				saytext = "该灯为关闭状态"
				baidu_tts.tts(saytext)
				speaker.speak()
