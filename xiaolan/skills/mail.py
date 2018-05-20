# -*- coding: utf-8 -*-

import time
import sys
import os
import requests
import json
import demjson
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sys.path.append('/home/pi/xiaolan/xiaolan/')
import speaker
from recorder import recorder
from stt import baidu_stt
from tts import baidu_tts

def start(tok):
    
    e = email()
    e.main(tok)
    
class email(object):
    
    def __init__(self):
        
        pass
        
    def main(self, tok):
        
        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        e = email()
        
        mail_host = 'smtp.qq.com' #这里默认qq邮箱，可以更改
        mail_user = '' #邮箱账户
        mail_pass = '' #邮箱密码
        mail_port = '465' #与邮箱服务商相通
        sender = 'xiaolan@hadream.com'
        receivers = []
        message['From'] = Header("xiaolan@hadream", 'utf-8')   # 发送者
        message['To'] =  Header("get", 'utf-8')        # 接收者
        
        bt.tts('请问您要向谁发送邮件，请说数字和邮箱服务商', tok)
        speaker.speak()
