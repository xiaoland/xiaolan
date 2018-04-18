# -*- coding: utf-8 -*-
#MusicCrawler.py

import os
import re
import time
sys.path.append('/home/pi/xiaolan/xiaolan/skills/')
import Crawler

global mCount
global song_name

mCount=0

def write_file(data):
    global mCount
    if not os.path.exists("D:/%s/" % song_name.decode('utf-8')):
        os.mkdir('D:/%s/' % song_name.decode('utf-8'))
    if not data:
        return
    with open('D:/%s/%s.m4a' % (song_name.decode('utf-8'),str(mCount)),'wb') as code:
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

song_name=raw_input(unicode('输入歌曲名:','utf-8').encode('gbk'))
song_name=unicode(song_name,'gbk').encode('utf-8')

headers={'authority':'c.y.qq.com','method':'GET','path':'/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60916586359500801&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%s&g_tk=5381&jsonpCallback=searchCallbacksong&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0' % song_name,'scheme':'https','accept':'*/*','accept-language':'zh-CN,zh;q=0.8','cache-control':'no-cache','pragma':'no-cache','referer':'https://y.qq.com/portal/search.html','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2717.400 QQBrowser/9.6.11133.400'}
html=mCrawler.download('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=66640132791913660&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%s&g_tk=5381&jsonpCallback=searchCallbacksong&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0' % song_name,headers=headers)
exec(html)
