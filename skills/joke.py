# -*- coding: utf-8 -*-
''' 故事/笑话 '''
import sys
import requests
import time
import random
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
from xiaolan import speaker


def start(tok):
    
    main(tok)


def main(tok):
    
    url = 'http://v.juhe.cn/joke/content/list.php'
    key = '21e780488098fa8b77394405421d8ae1'
    bt = baidu_tts()
    bs = baidu_stt(1, 'a', 2, '{')
    chose = random.randint(0, 9)
    
    r = requests.get(url + "key=" + key + "&page=10&pagesize=10&sort=asc&time=" + str(int(time.time())))
    
    json = r.json()
    
    if chose == 0:
        saytext = json['result']["data"][0]['content']
    elif chose == 1:
        saytext = json['result']["data"][1]['content']
    elif chose == 2:
        saytext = json['result']["data"][2]['content']
    elif chose == 3:
        saytext = json['result']["data"][3]['content']
    elif chose == 4:
        saytext = json['result']["data"][4]['content']
    elif chose == 5:
        saytext = json['result']["data"][5]['content']
    elif chose == 6:
        saytext = json['result']["data"][6]['content']
    elif chose == 7:
        saytext = json['result']["data"][7]['content']
    elif chose == 8:
        saytext = json['result']["data"][8]['content']
    elif chose == 9:
        saytext = json['result']["data"][9]['content']
    else:
        saytext = json['result']["data"][0]['content']

    bt.tts(saytext, tok)
    speaker.speak()
