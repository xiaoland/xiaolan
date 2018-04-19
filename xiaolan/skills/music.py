# -*- coding: utf-8 -*-

import re
import time
import sys
import os
import requests
import json
import demjson
import threading
import MusicCrawler
import random
sys.path.append('/home/pi/xiaolan/xiaolan/')
import speaker
from recorder import recorder
from stt import baidu_stt
from tts import baidu_tts
import nlp
import flac_to_mp3
sys.path.append('/home/pi/xiaolan/xiaolan/skills/')
import Crawler


global mCount
global song_name

mCount=0

def write_file(data):
    music = 'music'
    global mCount
    if not os.path.exists("/home/pi/xiaolan/xiaolan/musiclib/" % song_name.decode('utf-8')):
        os.mkdir('/home/pi/xiaolan/xiaolan/musiclib/' % song_name.decode('utf-8'))
    if not data:
        return
    with open('/home/pi/xiaolan/xiaolan/musiclib.m4a' + music as code:
        code.write(data)    

def MusicJsonCallback(e):
    headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Cache-Control':'no-cache','Connection':'keep-alive','Host':'dl.stream.qqmusic.qq.com','Pragma':'no-cache','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2717.400 QQBrowser/9.6.11133.400'}
    url='http://dl.stream.qqmusic.qq.com/%s?vkey=%s&guid=3218858725&uin=0&fromtag=66' % (e['data']['items'][0]['filename'],e['data']['items'][0]['vkey'])
    data=mCrawler.download(url,headers=headers)
    write_file(data)

def searchCallbacksong(e):
    headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Cache-Control':'no-cache','Connection':'keep-alive','Host':'dl.stream.qqmusic.qq.com','Pragma':'no-cache','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2717.400 QQBrowser/9.6.11133.400'}
    for index,item in enumerate(e['data']['song']['list']):
        global mCount
        mCount=mCount+1
        if item['type']==0:
            url='https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback&uin=0&songmid=%s&filename=C400%s.m4a&guid=3218858725' % (item['ksong']['mid'] if item['language']==2 else item['mid'],item['file']['media_mid'])
            html=mCrawler.download(url,headers=headers)
            exec(html)
        elif item['type']==111:
            url=item['url']+'?fromtag=38'
            data=mCrawler.download(url,headers=headers)
            write_file(data)
        elif item['type']==112:
            url='http://dl.stream.qqmusic.qq.com/C1L0%s.m4a?fromtag=38' % item['file']['media_mid']
            data=mCrawler.download(url,headers=headers)
            write_file(data)

mCrawler=Crawler.Crawler()

bt = baidu_tts()
bs = baidu_stt(1, 'a', 2, '{')
r = recorder()
tok = bs.get_token()
asktext = '欢迎使用小蓝音乐播放器，请输入指令，是随机播放还是搜索'
speaker.ding()
r.record()
speaker.dong()
text = bs.stt('./voice.wav', tok)
    if '搜索' in text:
        serasktext = '请说出要搜索的歌曲'
        bt.tts(serasktext, tok)
        speaker.speak()
        speaker.ding()
        r.record()
        speaker.dong()
        song_name = sertext
        song_name=unicode(song_name,'gbk').encode('utf-8')

        headers={'authority':'c.y.qq.com','method':'GET','path':'/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60916586359500801&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%s&g_tk=5381&jsonpCallback=searchCallbacksong&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0' % song_name,'scheme':'https','accept':'*/*','accept-language':'zh-CN,zh;q=0.8','cache-control':'no-cache','pragma':'no-cache','referer':'https://y.qq.com/portal/search.html','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2717.400 QQBrowser/9.6.11133.400'}
        html=mCrawler.download('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=66640132791913660&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%s&g_tk=5381&jsonpCallback=searchCallbacksong&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0' % song_name,headers=headers)
        exec(html)
        speaker.music()
    else:
        chose = random.randint(0,9)
        if chose == 0:
            deaf = '全部都是你'
        elif chose == 1:
            deaf = '带你去旅行'
        elif chose == 2:
            deaf = '皮皮虾我们走'
        elif chose == 3:
            deaf = 'i just want something like this'
        elif chose == 4:
            deaf = 'welcome to new york'
        elif chose == 5:
            deaf = 'sorry'
        elif chose == 6:
            deaf = '佛系少女'
        elif chose == 7:
            deaf = 'Something Just Like This'
        elif chose == 8:
            deaf = '粉红色的回忆'
        elif chose == 9:
            deaf = 'Happy'
        
        headers={'authority':'c.y.qq.com','method':'GET','path':'/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60916586359500801&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%s&g_tk=5381&jsonpCallback=searchCallbacksong&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0' % song_name,'scheme':'https','accept':'*/*','accept-language':'zh-CN,zh;q=0.8','cache-control':'no-cache','pragma':'no-cache','referer':'https://y.qq.com/portal/search.html','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2717.400 QQBrowser/9.6.11133.400'}
        html=mCrawler.download('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=66640132791913660&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%s&g_tk=5381&jsonpCallback=searchCallbacksong&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0' % deaf,headers=headers)
        exec(html)
        speaker.music()
