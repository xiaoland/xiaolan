# -*- coding: utf-8 -*-
# 百度STT
import sys
import signal
import requests
import os
import json
import xlpath
import wave
import pyaudio
import hyper
import logging
import time
import os.path
import demjson
import urllib
import urllib2
import base64
sys.path.append('/home/pi/xiaolan/xiaolan/baiduaip/aip')

domian = 'a'

class baidu_stt(object):
    def __init__(self, text, token, domain, transcribed):
        self.text = text
        self.domian = json
        self.token = token
        self.transcribed = transcribed

    def get_token(self): #获取token
        AK = '87oa8ZdtoVLSuVwV4YPqaeD3'
        SK = 'wi8G8UEa1tkgAKZbKsUHaZk8V6p4NxvL'
        url = 'http://openapi.baidu.com/oauth/2.0/token'
        params = urllib.urlencode({'grant_type': 'client_credentials',
                                   'client_id': AK,
                                   'client_secret': SK})
        r = requests.get(url, params=params)
        try:
            r.raise_for_status()
            token = r.json()['access_token']
            return token
        except requests.exceptions.HTTPError:
            self._logger.critical('Token request failed with response: %r',
                                  r.text,
                                  exc_info=True)
            return token
        
    def stt(self, fp, token): #开始
        try:
            wav_file = wave.open(fp, 'rb')
        except IOError:
            self._logger.critical('wav file not found: %s',
                                  fp,
                                  exc_info=True)
            return []
        n_frames = wav_file.getnframes()
        frame_rate = wav_file.getframerate()
        audio = wav_file.readframes(n_frames)
        base_data = base64.b64encode(audio)
        if self.token == '':
            self.token = self.get_token()
        dataf = {"format": "wav",
                "token": token,
                "len": len(audio),
                "rate": frame_rate,
                "speech": base_data,
                "cuid": 'b0-10-41-92-84-4d',
                "channel": 1}
        
        data = demjson.encode(dataf)
        
        r = requests.post('http://vop.baidu.com/server_api',
                          data=data,
                          headers={'content-type': 'application/json'})
        
        json = r.json()
        
        try:
            r.raise_for_status()
            text = ''
            if 'result' in r.json():
                text = r.json()['result'][0].encode('utf-8')
                print ("STT GET:")
                print (text)
                return text
        except requests.exceptions.HTTPError:
            self._logger.critical('Request failed with response: %r',
                                  r.text,
                                  exc_info=True)
            return []
        except requests.exceptions.RequestException:
            print ('Request failed.')
            return []
        except ValueError as e:
            print ('Cannot parse response: %s',
                                  e.args[0])
            return []
        except KeyError:
            print ('Cannot parse response')
            return []
        else:
            transcribed = []
            if text:
                transcribed.append(text.upper())
            print (json)
        
        #意图理解（大家一起补充啊，内容较多，或者看看有没有什么BUG，参考http://ai.baidu.com/docs#/ASR-Query-Protocol/6a6adfe0）
    def nlpquery(self):
        intent = 1 
        if intent == 1: 
            if domain == 'train': 
                arrival_city = r.json()['arrival_city'] 
                start_city = r.json()['start_city'] 
                start_station = r.json()['start_station'] 
                train_type = r.json()['train_type'] 
                return train_type, start_station, start_city, arrival_city 
            elif domain == 'weather': 
                date = r.json()['date'] 
                region = r.json()['region'] 
                return date return region 
            elif self.domain == 'flight': 
                start_date = r.json['start_date'] 
                start_city = r.json()['start_city'] 
                arrival_city = r.json()['arrival_city'] 
                airline = r.json()['airline'] 
                return airline, arrival_city, start_city, start_date 
            elif domain == 'map': 
                start = r.json()['start'] 
                arrival = r.json()['arrival'] 
                drive_sort = r.json()['drive_sort'] 
                route_type = r.json()[' route_type '] 
                return route_type 
                return drive_sort 
                return arrival 
                return start 
            elif domain == 'telephone':
                name = r.json()['name']
                operator = r.json()['operator'] 
                location = r.json()['location'] 
                return name 
                return operator 
                return location 
            elif domain == 'app': 
                appname = r.json()['appname'] 
                return appname 
            elif self.domain == 'website': 
                sitename = r.json()['sitename'] 
                browser = r.json()['browser'] 
                return browser 
                return sitename 
            elif domain == 'music': 
                name = r.json()['name'] 
                return name 
            elif domain == 'joke': 
                sence = r.json()['sence'] 
                audience = r.json()['audience'] 
                return sence 
                return audience 
            elif domian == 'instruction': 
                inent = r.json()['intent'] 
                return inent
            else:
                tuling = 'tuling'
                return tuling
            return domian
    def nlplexer(text):
        pass
        
        
        
