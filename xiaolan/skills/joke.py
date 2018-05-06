# -*- coding: utf-8 -*-
''' 故事/笑话 '''
import json
import sys
import os
import requests
import pygame
import time
import random
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import recorder
import speaker

def start(tok):
    
    main(tok)
    
def main(tok):
    
    url = 'http://api.avatardata.cn/Joke/QueryJokeByTime?key='
    key = 'a63ac25e95f741aea51167a05891498c'
    bt = baidu_tts()
    bs = baidu_stt(1, 'a', 2, '{')
    chose = random.randint(0,9)
    
    r = requests.post(url + key + '&sort=asc&time=1418745237')
    
    json = r.json()
    
    if chose == 0:
        saytext = json['result'][0]['content']
    elif chose == 1:
        saytext = json['result'][1]['content']
    elif chose == 2:
        saytext = json['result'][2]['content']
    elif chose == 3:
        saytext = json['result'][3]['content']
    elif chose == 4:
        saytext = json['result'][4]['content']
    elif chose == 5:
        saytext = json['result'][5]['content']
    elif chose == 6:
        saytext = json['result'][6]['content']
    elif chose == 7:
        saytext = json['result'][7]['content']
    elif chose == 8:
        saytext = json['result'][8]['content']
    elif chose == 9:
        saytext = json['result'][9]['content']
    else:
        saytext = json['result'][0]['content']
        
    saytext = jokefj + '第二个笑话' + jokesj
    bt.tts(saytext, tok)
    speaker.speak()
