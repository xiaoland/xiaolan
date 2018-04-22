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
import snowboy
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
import smarthome
import camera

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

def snowboystarts():
    
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
    intent = nlp.get_intent(text)
    s.getskills(intent, text)

def sconvenstation():
    
    token = ''
    b = baidu_stt(1, token, 2, '{')
    r = recorder()
    s = skills()
    speaker.speacilrecorder()
    speaker.ding()
    r.record()
    speaker.dong()
        
    tok = b.get_token()
    text = b.stt('./voice.wav', tok)
    if text == '':
        snowboystart()
    else:
        intent = nlp.get_intent(text)
        s.getskills(intent, text)
class skills(object):
    
    def __init__(self):
        pass
        
    def getskills(self, witch, text):
        s = skills()
        if witch == 'clock':
            s.clock()
        elif witch == 'xlonly':
            s.xlonly()
        elif witch == 'camera':
            s.camera()
        elif witch == 'smarthome':
            s.smarthome()
        elif witch == 'weather':
            s.weather()
        elif witch == 'music':
            s.music()
        elif witch == 'ts':
            s.ts()
        elif witch == 'email':
            s.email()
        elif witch == 'story':
            s.story()
        elif witch == 'joke':
            s.joke()
        elif witch == 'news':
            s.news()
        elif witch == 'smarthome':
            s.smarthome()
        elif witch == 'caream':
            s.caream()
        elif witch == 'video':
            s.video()
        elif witch == 'hotelSearch':
            s.hotel()
        elif witch == 'no':
            sconvenstation()
        else:
            s.tuling(text)
    
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
        
    def tuling(self, text):
        
        tuling.start(text)
    
    def story(self):
        
        story.start()
        
    def joke(self):
        
        joke.start()
        
    def news(self):
        
        news.start()
        
    def smarthome(self):
        
        s = smartHome()
        s.start()
    
    def video(self):
        
        video.start()
    
    def hotel(self):
        
        hotel.start()
        
welcome()
snowboystarts()




