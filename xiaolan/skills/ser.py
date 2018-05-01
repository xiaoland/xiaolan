# -*- coding: utf-8 -*-

import time
import sys
import os
import requests
import json
import demjson
import urllib
import urllib2
sys.path.append('/home/pi/xiaolan/xiaolan/')
import speaker
from recorder import recorder
from stt import baidu_stt
from tts import baidu_tts

def start(text):
  main(text)
def main(text):
  if '搜索' in text:
    sertext = text[2:-1]
  else:
    sertext = text
  url = 'http://www.baidu.com/s?'
  search = [('w',sertext)]
  sertext = url + urllib.urlencode(search)
  serback = requests.get(serurl)
  
  
