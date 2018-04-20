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



def wx_get_token():
        AS = '35217ef7c047d495ec7f5962a7fcf553'
        AID = 'wx05f5d960e3519a25'
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + AID + '&secret=' + AS
        r = requests.get(url)
        json = r.json()
        token = json['access_token']
        return token

def get_intent(text):
        
        city = '中山'
        tok = wx_get_token()
        url = 'https://api.weixin.qq.com/semantic/semproxy/search?access_token=' + tok
        appid = 'wx05f5d960e3519a25'
        service = "search,datetime,weather,location,number,restaurant,map,nearby,coupan,hotel,train,flight,travel,movie,music,video,novel,stock,remind,cookbook,baike,news,tv,instruction,tv_instruction"
        dataf = {
                "query": text,
                "city": city,
                "category": service,
                "appid": appid}
        
        data = json.dumps(dataf)
        r = requests.post(url,
                          data)
        wxintentjson = r.json()
        states = wxintentjson['errcode']
        if states == 0:
                intent = wxintentjson['intent']
                return intent
        else:
                do_intent()
        
def do_intent(text):#自制的语义理解系统,欢迎大家补充
    try:
        if '闹钟' in text:
                intent = 'clock'
                return intent
        elif '天气' in text:
                intent = 'weather'
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
        elif '笑话' in text:
                intent = 'joke'
                return intent
        else:
                intent = 'tuling'
                return intent
    except TypeError:
        intent = 'no'
        return intent
