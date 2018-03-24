import sys
import os
import logging
import json
import pygame
sys.path.append('/home/pi/xiaolan/')
import stt
import tts
import snowboy
import speaker
import recorder

def start():

    main()

def main():
    
    URL = ''
    data = { }
    r = requests.post(URL, data)
