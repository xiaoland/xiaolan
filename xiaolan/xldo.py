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
    
    os.system('python snowboy.py')

def snowboystop():

    snowboy.stop()
    convenstation()

def convenstation():

    time.sleep(1)
    speaker.ding()
    recorder.record()
    speaker.dong()
    baidu_stt.stt()

welcome()
snowboystart()




    


