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
    weather = json['result']['weather'][1]['info']['day'][2]
    temperature = json['result']['weather'][1]['info']['day'][3]
    yundong = json['result']['life']['info']['yundong'][-1]
    chuanyi = json['result']['life']['info']['chuanyi'][-1]
    mweather = json['result']['weather'][2]['info']['day'][2]
    mtemperature = json['result']['weather'][2]['info']['day'][3]
    
    tweatherstates = location + ',今天的天气是,' + weather + '，最高温度是,' + temperature + ',运动建议,' + yundong + '穿衣建议,' + chuanyi
    mweatherstates = location + ',明天的天气是,' + mweather + '，最高温度是,' + mtemperature
    saytextf = tweatherstates.encode('utf-8','strict')
    saytexts = mweatherstates.encode('utf-8','strict')
    saytext = saytextf + saytexts
    tok = bt.get_token()
    bt.tts(saytext, tok)
    speaker.speak()
