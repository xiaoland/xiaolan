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
        
    def send(self, mail_host, mail_user, mail_pass, mail_port, sender, tok):
        
        bt = baidu_tts()
        bs = baidu_stt(1, 2, 3, 4)
        r = recorder()
        e = email()
        receivers = []
        
        bt.tts('请问您要给谁发送邮件呢？格式为，邮箱数字加邮箱服务商，如，一五二六七八九，QQ邮箱', tok)
        speaker.speak()
        speaker.ding()
        r.tsrecord()
        speaker.dong()
        receivers[0] = bs.stt('./voice.wav', tok)
        bt.tts('请问您要发送什么内容?', tok)
        speaker.speak()
        speaker.ding()
        r.tsrecord()
        speaker.dong()
        messages = bs.stt('./voice.wav', tok)
        
        message = MIMEText(messages, 'plain', 'utf-8')
        message['From'] = Header("小蓝邮件代发", 'utf-8')
        message['To'] =  Header("You", 'utf-8') 
        subject = '小蓝邮件代发'
        message['Subject'] = Header(subject, 'utf-8')
        
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, mail_port)
            smtpObj.login(mail_user,mail_pass)  
            smtpObj.sendmail(sender, receivers, message.as_string())
            bt.tts('邮件发送成功', tok)
            speaker.speak()
        except smtplib.SMTPException:
            bt.tts('无法发送邮件', tok)
            speaker.speak()
    
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
        
        bt.tts('欢迎使用小蓝邮件助手，请问您有什么需要吗', tok)
        speaker.speak()
        speaker.ding()
        r.record()
        speaker.dong()
        commands = bs.stt('./voice.wav', tok)
        command = e.command_choose(commands, tok)
        if command == 'send':
            e.send(mail_host, mail_user, mail_pass, mail_port, sender, tok)
        else:
            bt.tts('对不起，我们还暂时不支持该功能', tok)
            speaker.speak()
