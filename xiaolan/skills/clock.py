# -*- coding: utf-8 -*-
''' 闹钟 '''
import json
import sys
import os
import requests
import pygame
import time
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import recorder
import speaker

def start(tok):
    
    main(tok)
  
def main(tok):
    bt = baidu_tts()
    bs = baidu_stt(1, 2, 3, 4)
    r.recorder()
    asktext = '请问您要设定什么时候的闹钟？要重复请在开头说重复闹钟，默认单次，重复闹钟请说出重复日期哦！'
    bt.tts(asktext, tok)
    speaker.speak()
    speaker.ding()
    r.record()
    speaker.dong()
    settext = bs.stt('./voice.wav', tok)
    if settext[0:3] = '重复闹钟':
        clockmode = 'reclock'
        reclocktime = settext[4:6]
        
    
