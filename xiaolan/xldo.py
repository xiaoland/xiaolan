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
import recorder
import snowboy
import speaker
sys.path.append('/home/pi/xiaolan/xiaolan/snowboy/')
import snowboydecoder
sys.path.append('/home/pi/xiaolan/xiaolan/skills/')
import clock
import xlonly
import weather
import music

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

def snowboystart():
    
    def signal_handler(signal, frame):
        global interrupted
        interrupted = True


    def interrupt_callback():
        global interrupted
        return interrupted

    model = '/home/pi/xiaolan/xiaolan/snowboy/xiaolanxiaolan.pmdl'
    
    # capture SIGINT signal, e.g., Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    print('Listening... Press Ctrl+C to exit')

    # main loop
    detector.start(detected_callback=convenstation,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)

    detector.terminate()

def convenstation():

    time.sleep(1)
    speaker.ding()
    recorder.record()
    speaker.dong()
    baidu_stt.stt()

class skills(object):
    
    def __init__(self, witch):
        self.witch = witch
        
    def getskills(self):
        if self.witch == 'clock':
            skills.clock()
        elif self.witch == 'xlonly':
            skills.xlonly()
        elif self.witch == 'cream':
            skills.cream()
        elif self.witch == 'smarthome':
            skills.smarthome()
        elif self.witch == 'weather':
            skills.weather()
        elif self.witch == 'music':
            skills.music()
        elif self.witch == 'ts':
            skills.ts()
        elif self.witch == 'email':
            skills.email()
        elif self.witch == 'call':
            skills.call()
    
    def clock(re, repeatday, d, h, m, music):
        clock.start(re, repeatday, d, h, m, music)
        
    def xlonly():
        xlonly.start()
    
    def weather(loc):
        weather.start(loc)
        

welcome()
snowboystart()




