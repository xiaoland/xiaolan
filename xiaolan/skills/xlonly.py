# -*- coding: utf-8 -*-
'''小蓝技能——父母私人助理，孝顺好帮手'''
import sys
import os
import pyaudio
import json
import pygame
sys.path.append('/home/pi/xiaolan/xiaolan/')
import stt
import tts
import snowboy
import recorder
import speaker

def xlonly():

    baidu_tts.tts("老爸，老妈，你们好啊，我是你们儿女派来的私人助理，小蓝")
    speaker.say()
    baidu_tts.tts("有什么吩咐吗？")
    speaker.say()
    speaker.ding()
    recorder.record()
    speaker.dong()
    baidu_stt.stt()
    
    
    
