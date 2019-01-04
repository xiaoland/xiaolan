# -*- coding: utf-8 -*-
'''天气'''
import sys
import os
import json
import requests
import random
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import speaker
from recorder import recorder

saytext_list = [
    "今天，s，温度是，d，摄氏度",
    "你猜啊！算了，告诉你吧：今天s，温度大概是d摄氏度",
    "我生气了，不想告诉你。但是看在你这么可爱的份上，告诉你咯：今天s，温度d摄氏度",
    "我是你的可爱小蓝，天气这就来：今天s，温度d摄氏度",
    "今天s，温度d摄氏度，天气天天都有，但如果我没有就恐怖了"
]


def start(tok):

    main(tok)


def main(tok):

    bt = baidu_tts()
    host = 'https://api.seniverse.com/v3/weather/now.json?key='
    key = 'sxyi6ehxblxkqeto'
    APIURL = key + '&location=ip&language=zh-Hans&unit=c'
    
    url = host + APIURL

    r = requests.get(url)
    
    json = r.json()
    print json
    weather = json['results'][0]['now']['text']
    temperature = json['results'][0]['now']['temperature']
    
    saytext = saytext_list[random.randint(0, 4)]
    saytext.replace("s", weather)
    saytext.replace("d", temperature)
    bt.tts(saytext, tok)
    speaker.speak()
