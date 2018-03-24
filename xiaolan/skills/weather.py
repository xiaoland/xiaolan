import sys
import os
import logging
import json
import pygame
sys.path.append('/home/pi/xiaolan/xiaolan/')
import stt
import tts
import snowboy
import speaker
import recorder

def start():

    main()

def main():
    
    API: '9f4785b7a627c847408230423d34787b'
    URL = 'https://api.darksky.net/forecast/'
    long = '113.197281'
    lati = '22.658797'
    lang = 'zh'
    r = requests.get(URL + '/' + API + '/' + long + ',' + lati)
    summary = r.json()['summary']
    temperature = r.json()['temperature']
    temperatureHigh = r.json()['temperatureHigh']
    icon = r.json()['icon']
    humidity = r.json()['humidity']
    temperatureLow = r.json()['temperatureLow']
    if icon = 'rain':
        icon = '下雨'
    stext = ("今天最高温为", temperatureHigh, "最低温为：", temperatureLow, "天气状态是是：", icon)
    baidu_tts.tts(stext)
    speaker.say()
