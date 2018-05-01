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
import smarthome
import ts
import news
import tuling
sys.path.append('/home/pi/xiaolan/xiaolan/')
import speaker
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder

def start(text):
    if '打开' in text:
        switch = text[2:-1]
        hassmode = 'turn_on'
        smarthome.onesay(switch, hassmode)
    elif '关闭' in text:
        switch = text[2:-1]
        hassmode = 'turn_off'
        smarthome.onesay(switch, hassmode)
    elif '播放' in text:
        if '音乐' in text:
            music.start()
        else:
            songname = text[2:-1]
            music.onesay(songname)
    elif '我想听' in text:
        if '音乐' in text:
            music.start()
        else:
            songname = text[3:-1]
            music.onesay(songname)
    elif '儿子' in text:
        xlonly.ei()
        xlonly.start()
    else:
        tuling.start(text)
        
          
            
        
