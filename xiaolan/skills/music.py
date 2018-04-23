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

def start():
    m = music()
    tok = bt.get_token()
    m.musicwelcome(tok)

class music(object):
    def __init__(self):
        pass
    def musicwelcome(self, tok):
        
        bt = baidu_tts()
        bs = baidu_stt(1, 'a', 2, '{')
        r = recorder()
        host = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?'
        dataup = 'ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=39931161434873138&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w='
        datadown = '&g_tk=679269129&jsonpCallback=MusicJsonCallback4697791032816454&loginUin=1481605673&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
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
            serurl = host + dataup + ser_song_name + datadown
            
            ser = requests.get(serurl)
            
            serjson = ser.json()
        
    
    
