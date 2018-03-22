# -*- coding: utf-8 -*-
# 音响控制器
import sys
import os
import logging
import pygame
import hyper
from xldo import xlmain

def ding():
    os.system('omxplayer /home/pi/xiaolan/musiclib/ding.wav')

def dong():
    os.system('omxplayer /home/pi/xiaolan/musiclib/dong.wav')

def welcome():
    os.system('omxplayer /home/pi/xiaolan/musiclib/welcome.mp3')

def poweroff():
    os.system('omxplayer /home/pi/xiaolan/musiclib/poweroff.mp3')

def say():
    os.system('omxplayer /home/pi/xiaolan/say.mp3')
