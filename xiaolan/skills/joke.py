# -*- coding: utf-8 -*-
''' 故事/笑话 '''
import json
import sys
import os
import requests
import pygame
import time
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import snowboy
import recorder
import speaker

def start():
    
    main()
    
def main():
    
    url = 'http://api.avatardata.cn/Joke/QueryJokeByTime?key='
    key = 'a63ac25e95f741aea51167a05891498c'
    bt = baidu_tts()
    bs = baidu_stt(1, 'a', 2, '{')
    
    r = requests.post(url + key + '&sort=asc&time=1418745237')
    
    json = r.json()
    
    jokef = json['result'][1]['content']
    jokes = json['result'][2]['content']
    jokefj = jokef.encode('utf-8','strict')
    jokesj = jokes.encode('utf-8','strict')
    saytext = jokefj + '第二个笑话' + jokesj
    tok = bt.get_token()
    bt.tts(saytext, tok)
    speaker.speak()
