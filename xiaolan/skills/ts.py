# -*- coding: UTF-8 -*-
import sys
import base64
import requests
import os
import json
import demjson
import base64
import hashlib
sys.path.append('/home/pi/xiaolan/xiaolan/')
import speaker
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder

def start(tok):
    main(tok)
  
def main(tok):
    
    bt = baidu_tts()
    bs = baidu_stt(1, 2, 3, 4)
    r = recorder()
    m = hashlib.md5()
    host = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    appid = '20180425000150592'
    apikey = 'gN56Mdv4mh2KJ0Ko2p6v'
    
    asktext = '请问您要翻译什么？请在滴一声后说出内容，文言文也可以翻译哦！'
    bt.tts(asktext, tok)
    speaker.speak()
    speaker.ding()
    r.tsrecord()
    speaker.dong()
    tstext = bs.stt('./voice.wav', tok)
    
    signf = appid + tstext + '1435660288' + apikey
    m.update(signf)
    sign = m.hexdigest()
    data = 'q=' + tstext + '&from=auto&to=zh&appid=' + appid + '&salt=1435660288&sign=' + sign
    url = host + data
    
    r = requests(url)
    
    json = r.json()
    print json
    tsback = ['trans_result'][0]['dst']
    saytext = tsback
    bt.tts(saytext, tok)
    speaker.speak()
  
