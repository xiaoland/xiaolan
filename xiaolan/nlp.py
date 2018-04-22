# -*- coding: utf-8 -*-
import sys
if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')
import time
import os
import json
import requests
import pygame
import demjson
import base64
import hashlib
from recorder import recorder
import snowboy
from tts import baidu_tts
from stt import baidu_stt


def get_intent(text):

        urlf = 'http://api.xfyun.cn/v1/aiui/v1/text_semantic?text='
        appid = '5ace1bbb'
        apikey = '9e1b8f6028b14b969cdec166eca127ea'
        lastmdl = 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9'
        curtimeo = int(time.time())
        curtimef = str(curtimeo)

        textl = base64.b64encode(text)
        textv = 'text=' + textl
        
        csumc = apikey + curtimef + 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9' + textv

        c = hashlib.md5()
        c.update(csumc)
        checksuml = c.hexdigest()
        
        headers = {'X-Appid': appid, 'Content-type': 'application/x-www-form-urlencoded; charset=utf-8', 'X-CurTime': curtimef, 'X-Param': 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9', 'X-CheckSum': checksuml}
        url = urlf + textl
        
        r = requests.post(url,
                          headers=headers)
        json = r.json()
        intent = json['data']['service']
        if intent != None:
                return intent
        else:
                do_intent(text)
        
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
        elif '唤醒词训练' in text:
                intent= 'snowboytrain'
                return intent
        else:
                intent = 'tuling'
                return intent
    except TypeError:
        intent = 'no'
        return intent
