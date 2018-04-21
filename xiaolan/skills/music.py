# -*- coding: utf-8 -*-

import time
import sys
import os
import requests
import json
import demjson
import subprocess
import hashlib
import re
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
    
    
