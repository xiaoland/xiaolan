# -*- coding: utf-8 -*-
'''天气'''
import sys
import os
import logging
import json
import pygame
import requests
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import snowboy
import speaker
import recorder

def start(loc):

    main(loc)

def main(loc):
    
    APIKEY = '5fb31534ef0e4a43812ba3f881194afe'
    location = loc
    url = ' http://api.avatardata.cn/Weather/Query?key='
    
    r = requests.post(url + APIKEY + '&cityname=' + location)
    weather = r.json()['info']
    temperature = r.json()['temperature']
    humidity = r.json()['humidity']
    city_name = r.json()['city_name']
    saytext = (city_name + '的天气是' + weather + '，温度是' + temperature + '，湿度是' + humidity)
    baidu_tts(saytext)
    speaker.speak()
