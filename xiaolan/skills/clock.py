# -*- coding: utf-8 -*-
''' 闹钟 '''
import json
import sys
import os
import requests
import pygame
sys.path.append('/home/pi/xiaolan/xiaolan/')
import stt
import tts
import snowboy
import recorder
import speaker

def start():
    main()
  
def main(d, re, redata, h, m, s):
    if re == 'True':
        
