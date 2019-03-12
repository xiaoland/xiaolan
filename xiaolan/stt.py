# -*- coding: utf-8 -*-
# 百度STT
import sys
import requests
import os
import json
import wave
import pyaudio
import time
import os.path
import base64
import urllib
import urllib2
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
        
        try:
            r.raise_for_status()
            text = ''
            if 'result' in r.json():
                text = r.json()['result'][0].encode('utf-8')
                return text
        except requests.exceptions.HTTPError:
            print ('Request failed with response: %r',
                   r.text)
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
        
