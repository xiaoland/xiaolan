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
import nlp
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

#STT语音识别API选择：讯飞，百度，分别是：'aiui'   'baidu'
stt_use = 'baidu'

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

    if '智能家居' in text:
        s.smarthome()
    elif '儿子' in text:
        s.xlonly()
    elif '女儿' in text:
        s.xlonly()
    else:
        intent = nlp.get_intent(text)
        if intent == 'text':
            intent = nlp.do_intent(text)
        s.getskills(intent, text)
    
class skills(object):
    
    def __init__(self):
        pass
        
    def getskills(self, witch, text):
        if witch == 'clock':
            skills.clock()
        elif witch == 'xlonly':
            skills.xlonly()
        elif witch == 'camera':
            skills.camera()
        elif witch == 'smarthome':
            skills.smarthome()
        elif witch == 'weather':
            skills.weather()
        elif witch == 'music':
            skills.music()
        elif witch == 'ts':
            skills.ts()
        elif witch == 'email':
            skills.email()
        elif witch == 'story':
            skills.story()
        elif witch == 'joke':
            skills.joke()
        elif witch == 'news':
            skills.news()
        elif witch == 'smarthome':
            skills.smarthome()
        elif witch == 'caream':
            skills.caream()
        else:
            skills.tuling(text)
    
    def clock(self):
        clock.start()
        
    def xlonly(self):
        
        xlonly.start()
    
    def weather(self):
        
        weather.start()
        
    def camera(self):
        
        camera.start()
        
    def music(self):
        
        music.start()
        
    def tuling(self):
        
        tuling.start()
    
    def story(self):
        
        story.start()
        
    def joke(self):
        
        joke.start()
        
    def news(self):
        
        news.start()
        
    def smarthome(self):
        
        s = smartHome()
        s.start()
        
welcome()
snowboystart()




