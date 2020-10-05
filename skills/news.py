# -*- coding: utf-8 -*-
''' 新闻 '''
import sys
import requests
import random
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder
from xiaolan import speaker


def start(tok):
    
    main(tok)
    
def main(tok):
    APPKEY = 'b8fff66168feb233d5cdb2f7931750f3'
    url = 'http://v.juhe.cn/toutiao/index?type='
    r = recorder()
    bt = baidu_tts()
    bs = baidu_stt(1, 'a', 2, '{')
    newsserviceasktext = '请问您要听什么新闻?'
    
    bt.tts(newsserviceasktext, tok)
    speaker.speak()
    speaker.ding()
    r.record()
    speaker.dong()
    text = bs.stt('./voice.wav', tok)
    chose = random.randint(0,9)
    
    if '国内新闻' in text:
        newsservice = 'chinanews'
    elif '国际新闻' in text:
        newsservice = 'nationnews'
    elif '科技新闻' in text:
        newsservice = 'kejinews'
    elif '体育新闻' in text:
        newsservice = 'tiyunews'
    else:
        newsservice = 't'
    
    if newsservice == 'chinanews':
        newstype = 'guonei'
        r = requests.post(url + newstype + '&key=' + APPKEY)
        json = r.json()
        if chose == 0:
            saytext = json['result']['data'][0]['title']
        elif chose == 1:
            saytext = json['result']['data'][1]['title']
        elif chose == 2:
            saytext = json['result']['data'][2]['title']
        elif chose == 3:
            saytext = json['result']['data'][3]['title']
        elif chose == 4:
            saytext = json['result']['data'][4]['title']
        elif chose == 5:
            saytext = json['result']['data'][5]['title']
        elif chose == 6:
            saytext = json['result']['data'][6]['title']
        elif chose == 7:
            saytext = json['result']['data'][7]['title']
        elif chose == 8:
            saytext = json['result']['data'][8]['title']
        elif chose == 9:
            saytext = json['result']['data'][9]['title']
        else:
            saytext = json['result']['data'][0]['title']
        bt.tts(saytext, tok)
        speaker.speak()
        
    elif newsservice == 'nationnews':
        newstype = 'guoji'
        r = requests.post(url + newstype + '&key=' + APPKEY)
        json = r.json()
        if chose == 0:
            saytext = json['result']['data'][0]['title']
        elif chose == 1:
            saytext = json['result']['data'][1]['title']
        elif chose == 2:
            saytext = json['result']['data'][2]['title']
        elif chose == 3:
            saytext = json['result']['data'][3]['title']
        elif chose == 4:
            saytext = json['result']['data'][4]['title']
        elif chose == 5:
            saytext = json['result']['data'][5]['title']
        elif chose == 6:
            saytext = json['result']['data'][6]['title']
        elif chose == 7:
            saytext = json['result']['data'][7]['title']
        elif chose == 8:
            saytext = json['result']['data'][8]['title']
        elif chose == 9:
            saytext = json['result']['data'][9]['title']
        else:
            saytext = json['result']['data'][0]['title']
        bt.tts(saytext, tok)
        speaker.speak()
    
    elif newsservice == 'kejinews':
        newstype = 'keji'
        r = requests.post(url + newstype + '&key=' + APPKEY)
        json = r.json()
        if chose == 0:
            saytext = json['result']['data'][0]['title']
        elif chose == 1:
            saytext = json['result']['data'][1]['title']
        elif chose == 2:
            saytext = json['result']['data'][2]['title']
        elif chose == 3:
            saytext = json['result']['data'][3]['title']
        elif chose == 4:
            saytext = json['result']['data'][4]['title']
        elif chose == 5:
            saytext = json['result']['data'][5]['title']
        elif chose == 6:
            saytext = json['result']['data'][6]['title']
        elif chose == 7:
            saytext = json['result']['data'][7]['title']
        elif chose == 8:
            saytext = json['result']['data'][8]['title']
        elif chose == 9:
            saytext = json['result']['data'][9]['title']
        else:
            saytext = json['result']['data'][0]['title']
    elif newsservice == 'tiyunews':
        newstype = 'tiyu'
        r = requests.post(url + newstype + '&key=' + APPKEY)
        json = r.json()
        if chose == 0:
            saytext = json['result']['data'][0]['title']
        elif chose == 1:
            saytext = json['result']['data'][1]['title']
        elif chose == 2:
            saytext = json['result']['data'][2]['title']
        elif chose == 3:
            saytext = json['result']['data'][3]['title']
        elif chose == 4:
            saytext = json['result']['data'][4]['title']
        elif chose == 5:
            saytext = json['result']['data'][5]['title']
        elif chose == 6:
            saytext = json['result']['data'][6]['title']
        elif chose == 7:
            saytext = json['result']['data'][7]['title']
        elif chose == 8:
            saytext = json['result']['data'][8]['title']
        elif chose == 9:
            saytext = json['result']['data'][9]['title']
        else:
            saytext = json['result']['data'][0]['title']
    else:
        newstype = 'top'
        r = requests.post(url + newstype + '&key=' + APPKEY)
        json = r.json()
        if chose == 0:
            saytext = json['result'][0]['title']
        elif chose == 1:
            saytext = json['result'][1]['title']
        elif chose == 2:
            saytext = json['result'][2]['title']
        elif chose == 3:
            saytext = json['result'][3]['title']
        elif chose == 4:
            saytext = json['result'][4]['title']
        elif chose == 5:
            saytext = json['result'][5]['title']
        elif chose == 6:
            saytext = json['result'][6]['title']
        elif chose == 7:
            saytext = json['result'][7]['title']
        elif chose == 8:
            saytext = json['result'][8]['title']
        elif chose == 9:
            saytext = json['result'][9]['title']
        else:
            saytext = json['result'][0]['title']
        bt.tts(saytext, tok)
        speaker.speak()
    
