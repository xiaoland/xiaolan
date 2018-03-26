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

def welcome():

    print('''

    #################*******###################
    #         小蓝-中文智能家居对话机器人          #
    #      (c)蓝之酱-1481605673@qq.com         #         
    #         由 叮当 中文对话机器人衍而来         #
    #      (c)潘伟洲 m@hahack.com              #
    #  log文件在小蓝的目录下,名字：xiaolan.log    #
    #  如果文件不存在，可以自行创建，要给予777权限   #
    #             欢迎使用!!!  :)              #
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
    detector.start(detected_callback=back,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)

    detector.terminate()

def convenstation():

    time.sleep(1)
    speaker.ding()
    recorder.record()
    speaker.dong()
    baidu_stt.stt()

welcome()
snowboystart()




    


