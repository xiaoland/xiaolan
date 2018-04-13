# -*- coding: utf-8 -*-
'''天气'''
import sys
import os
import logging
import json
import pygame
import requests
import urllib2
import re
import socket
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import snowboy
import speaker
from recorder import recorder

def start():

    main()

def main():

    token = ''
    bt = baidu_tts()
    bs = baidu_stt(1, 'a', 2, '{')
    r = recorder()
    url = ' http://api.avatardata.cn/Weather/Query?key='
    APIKEY = '5fb31534ef0e4a43812ba3f881194afe'
    
    
    location = '中山'
    
    r = requests.post(url + APIKEY + '&cityname=' + location)
    
    json = r.json()
    print json
    weather = json['result']['isForeign']['weather']['day'][2]
    temperature = json['result']['isForeign']['weather']['day'][3]
    yundong = json['result']['isForeign']['life']['info']['yundong'][-1]
    chuanyi = json['result']['isForeign']['life']['info']['chuanyi'][-1]
    
    weatherstates = location + ',的天气是,' + weather + '，最高温度是,' + temperature + ',运动建议,' + yundong + '穿衣建议,' + chuanyi 
    saytext = weatherstates.encode('utf-8','strict')
    bt.tts(saytext, tok)
    speaker.speak()

