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
        
    def welcome(self): # 欢迎

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

    def snowboystart(self): #语音唤醒
    
        os.system('python snowboy.py')

def convenstation(): # 对话过程操作

    snowboy.stop() # 暂停语音唤醒（问题就在这里，一旦停止唤醒，整个程序就直接停止了，如果不停止，就是占用麦克风，无法录制指令，待解决）
    recorder.record() # 开始录音
    speaker.dong() # 提示音
    baidu_stt.stt() # 语音转文字
    baidu_stt.nlp() # 语意理解（正在完善，详细参见http://ai.baidu.com/docs#/ASR-Query-Protocol/6a6adfe0)

# 启动
x = xlmain()
x.welcome()
x.snowboystart()




    


