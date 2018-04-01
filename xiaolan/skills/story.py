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

def start(storyname, storytype):
    
    main(storyname, storytype)
    
def main(storyname, storytype):
    
    
