# -*- coding: utf-8 -*-

import time
import sys
import os
import requests
import json
import demjson
sys.path.append('/home/pi/xiaolan/xiaolan/')
import speaker
from recorder import recorder
from stt import baidu_stt
from tts import baidu_tts

bt = baidu_tts()
bs = baidu_stt(1, 'a', 2, '{')
r = recorder()

def start():
    m = music()
    tok = bs.get_token()
    m.musicwelcome(tok)

class music(object):
    def __init__(self):
        pass
    def musicwelcome(self, tok):

        asktext = '欢迎使用小蓝音乐播放器，请输入指令，是随机播放还是搜索'
        speaker.ding()
        r.record()
        speaker.dong()
        text = bs.stt('./voice.wav', tok)
    
    
