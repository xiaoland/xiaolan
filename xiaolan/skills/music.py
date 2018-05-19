# -*- coding: utf-8 -*-

import time
import sys
import os
import requests
import json
import demjson
import random
sys.path.append('/home/pi/xiaolan/xiaolan/')
import speaker
from recorder import recorder
from stt import baidu_stt
from tts import baidu_tts


bt = baidu_tts()

def start(tok):
    m = music()
    m.main(tok)

class xlMusic(object):
    
    def __init__(self):
        
        pass
    
    def command_choose(self, commands, tok):
        
        if '随机播放' in commands or '随机' in commands:
            command = 'sui_ji'
            return command
        elif '搜索播放' in commands or '搜索' in commands:
            command = 'sou_suo'
            return command
        else:
            command = 'sui_ji'
            return command
        
    def sui_ji(self, services, tok):
        
        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        m = xlMusic()
        
        url = 'http://tingapi.ting.baidu.com/v1/restserver/ting?'
        song_name_c = random.uniform(0, 11)
        if song_name_c == 0:
            song_name = '粉红色的回忆'
        elif song_name_c == 1:
            song_name = 'I hope you think of me'
        elif song_name_c == 2:
            song_name = '小幸运'
        elif song_name_c == 3:
            song_name = '全部都是你'
        elif song_name_c == 4:
            song_name = '佛系少女'
        elif song_name_c == 5:
            song_name = 'Something just like this'
        elif song_name_c == 6:
            song_name = 'Feel this Moment'
        elif song_name_c == 7:
            song_name = 'Welcome to NewYork'
        elif song_name_c == 8:
            song_name = '洛天依投食歌'
        elif song_name_c == 9:
            song_name = '带你去旅行'
        elif song_name_c == 10:
            song_name = '死机之歌'
        elif song_name_c == 11:
            song_name = 'Shape of You'
        
        
        get_song_id_rawj = requests.get(url + services['search'] + song_name)
        get_song_id_j = get_song_id_rawj.json()
        try:
            id = get_song_id_j['song'][song_name_c]['songid']
        except KeyError:
            try:
                id = get_song_id_j['song'][0]['songid']
            except KeyError:
                bt.tts('对不起，播放错误')
                speaker.speak()
            else:
                pass
        else:
            get_song_url_rawj = requests.get(url + services['musicurl_get'] + id)
            get_song_url_j = get_song_url_rawj.json()
            song_url_f = get_song_url_j['data'][song_name_c]['url']
            download = requests.get(song_url)
            speaker.play()
        
    def main(self, tok):
        
        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        m = xlMusic()
        
        welcome = '欢迎使用小蓝音乐播放器，云服务使用百度音乐'
        ask = '请问您要随机播放还是搜索播放？'
        url = 'http://tingapi.ting.baidu.com/v1/restserver/ting?'
        services = {'musicurl_get': 'method=baidu.ting.song.play&songid=', 'search': 'method=baidu.ting.search.catalogSug&query='}
        
        bt.tts(welcome, tok)
        speaker.speak()
        bt.tts(ask, tok)
        speaker.speak()
        speaker.ding()
        r.record()
        speaker.dong()
        try:
            commands = bs.stt('./voice.wav', tok)
        except TypeError:
            speaker.speak()
            speaker.ding()
            r.record()
            speaker.dong()
            command = m.command_choose(commands, tok)
        else:
            if command == 'sui_ji':
                m.sui_ji(services, tok)
            elif command == 'sou_suo':
                m.sou_suo(services, tok)
            else:
                m.sui_ji(services, tok)
                
