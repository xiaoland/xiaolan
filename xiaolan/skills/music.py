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

def start(tok):
    m = music()
    m.musicwelcome(tok)

class music(object):
    def __init__(self):
        pass
    def musicwelcome(self, tok):
        
        bt = baidu_tts()
        bs = baidu_stt(1, 'a', 2, '{')
        r = recorder()
        url = 'http://mp3.baidu.com/dev/api/?'
        songurl = 'http://ting.baidu.com/data/music/links?songIds='
        ask_chose = '欢迎使用小蓝音乐播放器，请输入指令，是随机播放还是搜索'
        bt.tts(ask_chose, tok)
        speaker.speak()
        speaker.ding()
        r.record()
        speaker.dong()
        text = bs.stt('./voice.wav', tok)
        if '搜索' in text:
            ask_song_name = '请问您喜欢听哪首歌呢?'
            bt.tts(ask_song_name, tok)
            speaker.speak()
            speaker.ding()
            r.record()
            speaker.dong()
            ser_song_name = bs.stt('./voice.wav', tok)
            serurl = url + 'tn=getinfo&ct=0&ie=utf-8&word=' + ser_song_name + '&format=json'
            
            ser = requests.get(serurl)
            
            serjson = ser.json()
            songid = serjson['song_id']
            
            
        
    
    
