# -*- coding: utf-8 -*-
# 小蓝中央控制

import sys
import os
import pyaudio
import pygame
import requests
import json
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder
import speaker
import nlp
sys.path.append('/home/pi/xiaolan/xiaolan/skills/')
import clock
import xlonly
import weather
import music
import tuling
import joke
import news
from smarthome import hass
import camera
import snowboytrain
import ts
sys.path.append('/home/pi/xiaolan/xiaolan/snowboy/')
import snowboydecoder

def welcome():

    print('''

    #################*******###################
    #         小蓝-中文智能家居对话机器人         #
    #      (c)蓝之酱-1481605673@qq.com         #
    #   www.github.com/xiaoland/xiaolan-dev   #                                   
    #               欢迎使用!!!  :)            #              
    ###########################################

    ''')
    
    print('Check xiaolan')
    os.system('omxplayer /home/pi/xiaolan/xiaolan/musiclib/welcome.mp3')
    os.system('pulseaudio --start')

def awaken():

    os.system('python /home/pi/xiaolan/xiaolan/snowboy.py')
    
def convenstation():
    
    b = baidu_stt(1, 3, 2, '{')
    r = recorder()
    s = skills()
    speaker.ding()
    r.record()
    speaker.dong()  
    tok = b.get_token()
    text = b.stt('./voice.wav', tok)
    intent = nlp.get_intent(text)
    s.getskills(intent, text, tok)

def sconvenstation():

    speaker.speacilrecorder()
        
class skills(object):
    
    def __init__(self):
        pass
        
    def getskills(self, witch, text, tok):
        s = skills()
        if witch == 'clock':
            s.clock(tok)
        elif witch == 'xlonly':
            s.xlonly(tok)
        elif witch == 'camera':
            s.camera(tok)
        elif witch == 'smarthome':
            s.smarthome(tok)
        elif witch == 'weather':
            s.weather(tok)
        elif witch == 'music':
            s.music(tok)
        elif witch == 'ts':
            s.ts(tok)
        elif witch == 'email':
            s.email(tok)
        elif witch == 'story':
            s.story(tok)
        elif witch == 'joke':
            s.joke(tok)
        elif witch == 'news':
            s.news(tok)
        elif witch == 'smarthome':
            s.smarthome(tok)
        elif witch == 'caream':
            s.caream(tok)
        elif witch == 'video':
            s.video(tok)
        elif witch == 'hotelSearch':
            s.hotel(tok)
        elif witch == 'no':
            sconvenstation()
        elif witch == 'reintent':
            intent = nlp.do_intent(text, tok)
            s.getskills(intent, text, tok)
        elif witch == 'snowboytrain':
            s.snowboytrain(tok)
        elif witch == 'translate':
            s.ts(tok)
        elif witch == 'respeaker':
            os.system('omxplayer /home/pi/xiaolan/xiaolan/musiclib/say.mp3')
        else:
            s.onesay(text, tok)
    
    def clock(self, tok):
        clock.start(tok)
        
    def xlonly(self, tok):
        
        xlonly.start(tok)
    
    def weather(self, tok):
        
        weather.start(tok)
        
    def camera(self, tok):
        
        camera.start(tok)
        
    def music(self, tok):
        
        music.start(tok)
        
    def tuling(self, text, tok):
        
        tuling.start(text, tok)
    
    def story(self, tok):
        
        story.start(tok)
        
    def joke(self, tok):
        
        joke.start(tok)
        
    def news(self, tok):
        
        news.start(tok)
        
    def smarthome(self, tok):
        
        sm = hass()
        sm.start(tok)
    
    def video(self, tok):
        
        video.start(tok)
    
    def hotel(self, tok):
        
        hotel.start(tok)
        
    def snowboytrain(self, tok):
        
        snowboytrain.start(tok)
    
    def ts(self, tok):
        
        ts.start(tok)
        
    def onesay(self, text, tok):
        
        onesay.start(text, tok)

choses = sys.argv[1]
if choses == 'b':
    welcome()
    awaken()
elif choses == 'a':
    convenstation()
else:
    welcome()
    awaken()




