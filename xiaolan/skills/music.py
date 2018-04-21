# -*- coding: utf-8 -*-

import re
import time
import sys
import os
import requests
import json
import demjson
import eyed3
import subprocess
import hashlib
import re
import subprocess
import threading
from MusicBoxApi import api as NetEaseApi
sys.path.append('/home/pi/xiaolan/xiaolan/')
import speaker
from recorder import recorder
from stt import baidu_stt
from tts import baidu_tts

bt = baidu_tts()
bs = baidu_stt(1, 'a', 2, '{')
r = recorder()
tok = bs.get_token()
asktext = '欢迎使用小蓝音乐播放器，请输入指令，是随机播放还是搜索'
speaker.ding()
r.record()
speaker.dong()
text = bs.stt('./voice.wav', tok)

if '随机' in text:
    netease = NetEaseApi.NetEase()
    music_list = netease.top_songlist()
    datalist = netease.dig_info(music_list, 'songs')
    playlist = []
    for data in datalist:
        music_info = {}
        music_info.setdefautl("song_name", data.get("song_name"))
        music_info.setdefault("artist", data.get("artist"))
        music_info.setdefault("album_name", data.get("album_name"))
        music_info.setdefault("mp3_url", data.get("mp3_url"))
        music_info.setdefault("playTime", data.get("playTime"))
        music_info.setdefault("quality", data.get("quality"))
        playlist.append(music_info)
    print playlist
    return playlist
    
    
