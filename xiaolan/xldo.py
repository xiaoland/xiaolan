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
from stt import baidu_stt
from tts import baidu_tts
import logging
import tempfile
import wave
import recorder
import snowboy
import speaker

class xlmain(object):
    def __init__(self):
        self.self = self
        
    def welcome(self):

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
        os.system('omxplayer /home/pi/xiaolan/musiclib/welcome.mp3')

    def snowboystart(self):
    
        os.system('python snowboy.py')

def convenstation():

    snowboy.stop()
    recorder.record()
    speaker.dong()
    baidu_stt.stt()
    baidu_stt.nlp()

x = xlmain()
x.welcome()
x.snowboystart()




    


