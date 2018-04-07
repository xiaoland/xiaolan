# -*- coding: utf-8 -*-
'''音乐'''
import sys
import os
import requests
import json
import base64
import binascii
import hashlib
import json
import re
import urllib2
from Crypto.Cipher import AES
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import bsidu_stt
from tts import baidu_tts
import snowboy
import speaker
import recorder

def start(name):
  
    main(name)

def main(name):
  
    zh = '13415354654@163.com'
    passwd = 'Y20050801056'
    minimumsize = 1
    url2 = "http://music.163.com/playlist?id="
    r = requests.get(url2 + name)
    contents = r.text
    res = r'<ul class="f-hide">(.*?)</ul>'
    mm = re.findall(res, contents, re.S | re.M)
    res = r'<li><a .*?>(.*?)</a></li>'
    mm = re.findall(res, contents, re.S | re.M)

    for value in mm:

    	url = 'http://sug.music.baidu.com/info/suggestion'
    	payload = {'word': value, 'version': '2', 'from': '0'}
    	print "Song Name: " + value

    	r = requests.get(url, params=payload)
    	contents = r.text
    	d = json.loads(contents, encoding="utf-8")
    	if('data' not in d):
    		print "do not have flac\n"
        	continue
    	if('song' not in d["data"]):
    		print "do not have flac\n"
    		continue
    	songid = d["data"]["song"][0]["songid"]
    	print "Song ID: " + songid 

    	url = "http://music.baidu.com/data/music/fmlink"
    	payload = {'songIds': songid, 'type': 'mp3'}
    	r = requests.get(url, params=payload)
    	contents = r.text
    	d = json.loads(contents, encoding="utf-8")
    	if d is not None and 'data' not in d or d['data'] == '':
        	continue
    	songlink = d["data"]["songList"][0]["songLink"]
    	if(len(songlink) < 10):
        	print "do not have flac\n"
        	continue
		print "Song Source: " + songlink + "\n";

    	songdir = "songs"
   	if not os.path.exists(songdir):
        	os.makedirs(songdir)

    	songname = d["data"]["songList"][0]["songName"]
    	artistName = d["data"]["songList"][0]["artistName"]
    	filename = "music.flac"

   	f = urllib2.urlopen(songlink)
    	headers = requests.head(songlink).headers
    	size = int(headers['Content-Length']) / (1024 ** 2)

    	if not os.path.isfile(filename) or os.path.getsize(filename) < minimumsize:
        	print "%s is downloading now ......\n" % songname
        	with open(filename, "wb") as code:
                	code.write(f.read())
    	else:
        	print "%s is already downloaded. Finding next song...\n\n" % songname
    		print "\n================================================================\n"
    		print "Download finish!"
    		filename = '/home/pi/xiaolan/xiaolan/musiclib/music.flac'
    		flac_to_mp3.chageFile(filename)
    		speaker.player()
        
    
    
 
