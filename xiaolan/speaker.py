# -*- coding: utf-8 -*-
# 音响控制器
import sys
import os
import logging
import pygame
import hyper

def ding(): #开始录制指令提示音
    os.system('omxplayer /home/pi/xiaolan/xiaolan/musiclib/ding.wav')

def dong(): #结束录制指令提示音
    os.system('omxplayer /home/pi/xiaolan/xiaolan/musiclib/dong.wav')

def poweroff(): #关机提示音（太懒，mp3文件还没弄）
    os.system('omxplayer /home/pi/xiaolan/musiclib/xiaolan/poweroff.mp3')

def kacha(): #拍照声
    os.system('omxplayer /home/pi/xiaolan/xiaolan/musiclib/kacha.mp3')
    
def speak(): #说出的回话
    os.system('omxplayer /home/pi/xiaolan/xiaolan/musiclib/say.mp3')
    
def player(): #音乐播放器
    os.system('omxplayer /home/pi/xiaolan/xiaolan/music.mp3')
