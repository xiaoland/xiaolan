# -*- coding: utf-8 -*-
''' 新闻 '''
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

def start(newsservice):
    
    main()
    
def main(newsservice):
    cAPIKEY = '549dfe30dba14d87bcbca16c86bc4d85'
    nAPIKEY = 'e32ca74cc1ec40dba642f07ffc529447'
    kAPIKEY = '37d6e1142ceb4cbe98b5cb2de55300d2'
    chinanewsurl = 'http://api.avatardata.cn/GuoNeiNews/Query?key='
    nationnewsurl = 'http://api.avatardata.cn/WorldNews/Query?key='
    kejinewsurl = 'http://api.avatardata.cn/TechNews/Query?key='
    if newsservice == 'chinanews':
        r = requests.post(chinanewsurl + cAPIKEY + '&page=1&rows=1')
        saytext = r.json()['title']
        baidu_tts.tts(saytext)
        speaker.speak()
        
    elif newsservice == 'nationnews':
        r = requests.post(nationnewsurl + nAPIKEY + '&page=1&rows=1')
        saytext = r.json()['title']
        baidu_tts.tts(saytext)
        speaker.speak()
    
    elif newsservice == 'kejinews':
        r = requests.post(kejinewsurl + kAPIKEY + '&page=1&rows=1')
        saytext = r.json()['title']
        baidu_tts.tts(saytext)
        speaker.speak()
    
