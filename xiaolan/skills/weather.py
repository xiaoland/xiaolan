# -*- coding: utf-8 -*-
'''天气'''
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
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
from recorder import recorder

def start():

    main()

def main():

    bt = baidu_tts()
    bs = baidu_stt(1, token, 2, '{')
    r = recorder()
    url = ' http://api.avatardata.cn/Weather/Query?key='
    APIKEY = '5fb31534ef0e4a43812ba3f881194afe'

    locsertext = '请问您要查询哪个城市的天气?'
    locsertchtext = locsertchtext.encode('utf-8','strict')
    tok = bt.get_token()
    bt.tts(locsertchtext, tok)
    speaker.speak()
    speaker.ding()
    r.record()
    speaker.dong()
    location = bs.stt('./voice.wav', tok)
    
    
    r = requests.post(url + APIKEY + '&cityname=' + location)
    
    json = r.json()
    windy = json['result']['data']['realtime']['wind']['direct']
    weather = json['result']['data']['realtime']['weather']['info']
    humidity = json['result']['data']['realtime']['weather']['humidity']
    temperature = json['result']['data']['realtime']['weather']['temperature']
    wuran = json['result']['data']['life']['info']['wuran'][0]
    chuanyi = json['result']['data']['life']['info']['chuanyi'][-1]
    
    weatherstates = city_name + ',的天气是' + weather + '，温度是' + temperature + '，湿度是' + humidity + ',空气污染级别为' + wuran + '穿衣建议' + chuanyi 
    saytext = weatherstates.encode('utf-8','strict')
    baidu_tts(saytext, tok)
    speaker.speak()
