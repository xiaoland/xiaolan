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
    weather = json['result']['weather'][0]['info']['day'][-6]
    temperature = json['result']['weather'][0]['info']['day'][2]
    yundong = json['result']['life']['info']['yundong'][-1]
    chuanyi = json['result']['life']['info']['chuanyi'][-1]
    
    tweatherstates = location + ',今天的天气是,' + weather + '，最高温度是,'  + temperature + '，摄氏度，' + yundong + chuanyi
    saytext = tweatherstates.encode('utf-8','strict')
    tok = bt.get_token()
    bt.tts(saytext, tok)
    speaker.speak()
