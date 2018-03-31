# -*- coding: utf-8 -*-
''' 闹钟 '''
import json
import sys
import os
import requests
import pygame
import time
sys.path.append('/home/pi/xiaolan/xiaolan/')
import stt
import tts
import snowboy
import recorder
import speaker

def start(d, re, redata, h, m):
    
    main(d, re, redata, h, m)
  
def main(d, re, redata, h, m):
    if re == 'True':
        flag = 1
        while flag:
            t = time.localtime()  # 当前时间的纪元值
            fmt = "%H %M"
            now = time.strftime(fmt, t)  # 将纪元值转化为包含时、分的字符串
            now = now.split(' ') #以空格切割，将时、分放入名为now的列表中

            hour = now[0]
            minute = now[1]
            if hour == h and minute == m:
                os.sys(omxplayer /home/pi/xiaolan/xiaolan/music/clock.mp3)
                flag = 0
        
