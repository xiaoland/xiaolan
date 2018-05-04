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

def start(cortolthings, platfrom):
	h = smartHome()
	platfrom = 'hass'
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
		if platfrom == 'hass':
			h = smartHome()
			bt = baidu_tts()
			bs = baidu_stt(1, 2, 3, 4)
			tok = bt.get_token()
			ask = "请在滴一声之后，说出指令"
			bt.tts(ask, tok)
			speaker.speak()
			speaker.ding()
			recorder.record()
			speaker.dong()
			text = bs.stt('./voice.wav', tok)
			if "灯" in parsed_text:
				h.hasslights(tok)
			elif "开关" in parsed_text:
				h.hassswitchs(tok)
			elif "获取" in parsed_text:
				asks = "您要获取传感器的数据还是灯或插头的状态"
				bt.tts(asks, tok)
				speaker.speak()
				speaker.ding()
				recorder.record()
				speaker.dong()
				text = bs.stt('./voice.wav', tok)
				if "灯" in text:
					ty = 1
					h.hasssensor(ty, tok)
				elif "插座" in text:
					ty = 2
					h.hasssensor(ty, tok)
				elif "传感器" in text:
					ty = 3
					h.hasssensor(ty, tok)
			
	#灯类控制Homeassistant
	def hasslight(tok):
		url = '192.168.2.110'
		apikey = 'y20050801'
		entity_id = {}
		askf = "您想要控制什么灯?，请在滴一声之后说出，开，或，关，加上，名称"
		baidu_tts.tts(askf)
		speaker.speak()
		speaker.ding()
		recorder.record()
		speaker.dong()
		baidu_stt.stt()
			
		headers = {'x-ha-access': password, 'content-type': 'application/json'}
    		r = requests.get('http://' + url + ':8123/api/history/period/2016-12-29T00:00:00+02:00',
				 headers=headers)
		
		json = r.json()
		services = keyvalue_all(1, json)
		
		if '打开' in text:
			pass
		elif '关闭' in text:
			pass
	
	#开关控制（homeassistant)
	def hassswitchs(tok):
		domain = "switch"
		url = '192.168.2.110'
		apikey = 'y20050801'
		entity_id = {}
		askt = "您想要控制什么开关?，请在滴一声之后说出，开，或，关，加上，名称"
		bt.tts(askt, tok)
		speaker.speak()
		speaker.ding()
		recorder.record()
		speaker.dong()
		text = bs.stt('./voice.wav', tok))
			
		headers = {'x-ha-access': password, 'content-type': 'application/json'}
    		r = requests.get('http://' + url + ':8123/api/history/period/2016-12-29T00:00:00+02:00',
				 headers=headers)
		
		json = r.json()
		all_data_base = json[0:-1]
		friendly_name = all_data_base[0:-1]['attributes']['friendly_name']
		for friendly_name in 
		
		
		
		if '打开' in :
			pass
		elif cortolinent == 'turn_off':
			pass

	
	#设备数据/状态获取(homeassistant)
	def hasssensor(ty):
		url = 'http://192.168.2.110'
		apikey = 'y20050801'
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
