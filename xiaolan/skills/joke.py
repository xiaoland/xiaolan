# -*- coding: utf-8 -*-
''' 故事/笑话 '''
import json
import sys
import os
import requests
import pygame
import time
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import bsidu_stt
from tts import baidu_tts
import snowboy
import recorder
import speaker

def start():
    
    main()
    
def main():
    
    url = 'http://api.avatardata.cn/Joke/QueryJokeByTime?key='
    key = 'a63ac25e95f741aea51167a05891498c'
    r = requests.post(url + key + '&page=2&rows=10&sort=asc&time=1418745237')
    joke = r.json()['content']
    baidu_tts(joke)
    speaker.speak()
