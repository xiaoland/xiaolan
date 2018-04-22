#! /usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
import requests
import json
import demjson
sys.path.append('/home/pi/xiaolan/xiaolan/')
import speaker
from stt import baidu_stt
from tts import baidu_tts
import snowboy
import recorder

def start():
    
    main()

def get_wave(fname):
    with open(fname) as infile:
        return base64.b64encode(infile.read())

def main():
    
    r = recorder()
    bt = baidu_tts()
    tok = bt.get_token()
    url = 'https://snowboy.kitt.ai/api/v1/train/'
    apikey = '78ee816d9bfc8fb0e01341d4408e3f23fbbc9b03'
    askf = '第一次训练录音开始，请在滴一声之后说出，blueberry'
    bt.tts(askf, tok)
    speaker.speak()
    speaker.ding()
    r.trainrecord()
    speaker.dong()
    
    data = {
            "name": 'blueberry',
            "language": 'en',
            "token": apikey,
            "voice_samples": [
                {"wave": get_wave(wav1)},
                {"wave": get_wave(wav2)},
                {"wave": get_wave(wav3)}
            ],
           }
            
