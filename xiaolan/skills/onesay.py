# -*- coding: UTF-8 -*-
import sys
import base64
import requests
import os
import json
import demjson
import base64
import hashlib
import music
from smarthome import hass
import ts
import news
import tuling
sys.path.append('/home/pi/xiaolan/xiaolan/')
import speaker
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder

def start(text, tok):
    sm = hass()
    if '打开' in text:
        cortolthings = text[2:-1]
        cortolmode = 'turn_on'
        sm.cortol(cortolthings, cortolmode, tok)
    elif '关闭' in text:
        cortolthings = text[2:-1]
        cortolmode = 'turn_off'
        sm.cortol(cortolthings, cortolmode, tok)
    elif '将' in text and '翻译' in text:
        tsthings = text[1:-6]
        tsmode = text[-1:-2]
    elif '查看' in text and '状态' in text:
        getstatethings = text[2:-1]
        getmode = 'sensor'
        sm.sensor(getstatethings, getmode, tok)
        
    elif '播放' in text:
        if '随机' in text or '音乐' in text:
            music.main()
        else:
            songname = text[2:-1]
            music.onesay(songname)
    elif '我想听' in text:
        if '随机' in text or '音乐' in text:
            music.start()
        else:
            songname = text[3:-1]
            music.onesay(songname)
            
    elif '儿子' in text:
        xlonly.ei()
        xlonly.start()
    else:
        tuling.start(text)
        
          
            
        
