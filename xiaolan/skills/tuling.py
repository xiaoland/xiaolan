# -*- coding: utf-8 -*-
'''图灵'''
import sys
import os
import requests
import json
import urllib2
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import speaker
import recorder


def start(text, tok):
  
    main(text, tok)


def main(text, tok):
    
    ak = '869429e05ea142ef9e3784f8e7965d1c'
    ui = '373523'
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    dataf = {
                "reqType": 0,
                "perception": {
                    "inputText": {
                        "text": text
                    },
                },
                "userInfo": {
                  "apiKey": ak,
                  "userId": ui
                }
           }
    data = json.dumps(dataf)
    talkback = requests.post(url, data=data)
    talkback_data = talkback.json()
    text = talkback_data["results"][-1]["values"]["text"]
    saytext = text.encode('utf-8', 'strict')
    bt = baidu_tts()
    bt.tts(saytext, tok)
    speaker.speak()
