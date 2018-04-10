# -*- coding: utf-8 -*-
import sys
import os
import json
import requests
import pygame
import demjson
import time
import ssl
import urllib2
import urllib
from recorder import recorder
import snowboy
from tts import baidu_tts
from stt import baidu_stt


def get_intent(text):
        ak = 'cd3c2238c7348d28363a1aad0b93d474'
        url = 'https://ai.aixxz.com/api?'

        host = 'https://ai.aixxz.com'
        path = '/api'
        method = 'POST'
        appcode = 'cd3c2238c7348d28363a1aad0b93d474'
        textf = text.encode('utf-8','strict')
        textl = 'text=' + textf + '&uesr=123456'
        querys = 'city=%E6%B7%B1%E5%9C%B3&comfrom=comfrom&event=text&lang=zh_CN&nickname=%E8%8A%B1%E5%A5%BD%E6%9C%88%E5%9C%86&' + textl

        bodys = {}
        url = host + path + '?' + querys

        request = urllib2.Request(url)
        request.add_header('Authorization', 'APPCODE ' + appcode)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        response = urllib2.urlopen(request, context=ctx)
        content = response.read()
        if (content):
                print content
        return domain
        
        
def do_intent(text): #自制的语义理解系统,欢迎大家补充
        if '闹钟' in text:
                intent = 'clock'
                return intent
        elif '打开' in text:
                intent = 'smarthome'
                return intent
        elif '翻译' in text:
                intent = 'ts'
                return intent
        elif '搜索' in text:
                intent = 'ser'
                return intent
        elif '闲聊' in text:
                intent = 'tuling'
                return intent
        elif '关机' in text:
                print ('SHUTDOWING...')
                os.system('sudo poweroff')
        elif '重启' in text:
                print ('REBOOTING...')
                os.system('sudo reboot')
        elif '怎么走' in text:
                intent = 'map'
                return intent
        elif '酒店' in text:
                intent = 'hotel'
                return intent
        elif '旅游' in text:
                intent = 'travel'
                return intent
        elif '做游戏' in text:
                intent = 'minigame'
                return intent
        elif '新闻' in text:
                intent = 'news'
                return intent
        elif '傻逼' in text:
                speaker.falu()
        elif '拍照' in text:
                intent = 'camera'
                return intent
        elif '邮件' in text:
                intent = 'email'
                return intent
        elif '快递' in text:
                intent = 'experss'
                return intent
        else:
                intent = 'tuling'
                return intent
