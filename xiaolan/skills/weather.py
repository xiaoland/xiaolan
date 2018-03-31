# -*- coding: utf-8 -*-
'''天气'''
import sys
import os
import logging
import json
import pygame
import requests
sys.path.append('/home/pi/xiaolan/xiaolan/')
import stt
import tts
import snowboy
import speaker
import recorder

def start():

    main()

def main():
    
    API = 'sxyi6ehxblxkqeto'
    location = 'ip'
    LANGUAGE = 'zh-Hans'
    
    result = requests.get(API, params={
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=1)
    weather = r.json()['text']
    return result
