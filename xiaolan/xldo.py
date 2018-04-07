# -*- coding: utf-8 -*-
# 小蓝中央控制

import xlpath
import sys
import os
import pyaudio
import pygame
import requests
import json
import pygame
import hyper
import time
import signal
from stt import baidu_stt
from tts import baidu_tts
import logging
import tempfile
import wave
from recorder import recorder
import snowboy
import speaker
sys.path.append('/home/pi/xiaolan/xiaolan/snowboy/')
import snowboydecoder
sys.path.append('/home/pi/xiaolan/xiaolan/skills/')
import clock
import xlonly
import weather
import music
import tuling
import joke
import news
import smarthome
import camera

interrupted = False

def welcome():

    print('''

    #################*******####################
    #         小蓝-中文智能家居对话机器人         *
    #      (c)蓝之酱-1481605673@qq.com         *
    #         由叮当-中文对话机器人衍而来         *
    #      (c)潘伟洲-m@hahack.com              *                           
    #             欢迎使用!!!  :)              *              
    ###########################################

    ''')
    
    print('Check xiaolan')
    os.system('omxplayer /home/pi/xiaolan/xiaolan/musiclib/welcome.mp3')
    os.system('pulseaudio --start')

def snowboystart():
    
    os.system('python /home/pi/xiaolan/xiaolan/snowboy.py')

def convenstation():
    
    token = ''
    b = baidu_stt(1, token, 2, '{')
    r = recorder()
    s = skills()
    
    speaker.ding()
    r.record()
    speaker.dong()
    tok = b.get_token()
    text = b.stt('./voice.wav', tok)
    query = b.nlpquery(text)
    s.getskills(query)
    
class skills(object):
    
    def __init__(self, witch):
        self.witch = witch
        
    def getskills(self):
        if self.witch == 'clock':
            skills.clock(re, repeatday, d, h, m, music)
        elif self.witch == 'xlonly':
            skills.xlonly()
        elif self.witch == 'camera':
            skills.camera(service)
        elif self.witch == 'smarthome':
            skills.smarthome()
        elif self.witch == 'weather':
            skills.weather(loc)
        elif self.witch == 'music':
            skills.music(name)
        elif self.witch == 'ts':
            skills.ts()
        elif self.witch == 'email':
            skills.email()
        elif self.witch == 'story':
            skills.story()
        elif self.witch == 'joke':
            skills.joke()
        elif self.witch == 'news':
            skills.news(newsservice)
        elif self.witch == 'smarthome':
            skills.smarthome()
        elif self.witch == 'caream':
            skills.caream()
        else:
            skills.tuling(text)
    
    def clock(self, re, repeatday, d, h, m, music):
        clock.start(re, repeatday, d, h, m, music)
        
    def xlonly(self):
        
        xlonly.start()
    
    def weather(self, loc):
        
        weather.start(loc)
        
    def camera(self):
        
        camera.start(service)
        
    def music(self):
        
        music.start(name)
        
    def tuling(self, text):
        
        tuling.start(text)
    
    def story(self):
        
        story.start()
        
    def joke(self):
        
        joke.start()
        
    def news(self, newsservice):
        
        news.start(newsservice)
        
    def smarthome(self):
        
        s = smartHome()
        s.start()
        
welcome()
snowboystart()




