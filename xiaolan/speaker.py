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
    
    pygame.init()
    pygame.mixer.music.load('/home/pi/xiaolan/xiaolan/musiclib/say.mp3')
    pygame.mixer.music.play()
    
def music(): #音乐播放器
    
    pygame.init()
    pygame.mixer.music.load('/home/pi/xiaolan/xiaolan/musiclib/music.mp3')
    pygame.mixer.music.play()
    
def speacilrecorder():
    
    pygame.init()
    pygame.mixer.music.load('omxplayer /home/pi/xiaolan/xiaolan/musiclib/speacilrecorder.mp3')
    pygame.mixer.music.play()
