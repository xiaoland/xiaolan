# coding=utf-8
# author: Lan_zhijiang
# description: xiaolan's tts classes
# date: 2020/10/1

import requests
import shutil
import urllib.parse


class BaiduTTS():
    def __init__(self, log, setting):
        
        self.log = log
        self.token = ""

        self.app_key = setting["apiSettings"]["tts"]["appKey"]
        self.secret_key = setting["apiSettings"]["tts"]["secretKey"]

        self.get_token()
        
    def get_token(self):

        """
        获取token
        :return:
        """
        AK = 'M9jz0511Yfbb15d1BshqtC5g'
        SK = 'Z73I2jvytEa8QydGnNlP3oOKfudIlvgE'
        URL = 'http://openapi.baidu.com/oauth/2.0/token'

        param = {'grant_type': 'client_credentials',
                 'client_id': self.app_key,
                 'client_secret': self.secret_key}
        params = urllib.parse.urlencode(param)
        r = requests.get(URL, params=params)
        try:
            r.raise_for_status()
            token = r.json()['access_token']
            self.token = token
            return token
        except requests.exceptions.HTTPError:
            self.log.add("BaiduTTS: Getting token http error! Status code: " + str(r.status_code), 3)


          
        
    def start(self, text, token):

        """
        开始生成语音
        :param saytext:
        :param token:
        :return:
        """
        data = {'tex': text,
                 'lan': 'zh',
                 'tok': token,
                 'ctp': 1,
                 'cuid': 'b0-10-41-92-84-4d',
                 'per': 4
        }
        r = requests.post('http://tsn.baidu.com/text2audio',
                          data=data,
                          headers={'content-type': 'application/json'},stream=True)

        if r.status_code == 200:  
            with open(r"./data/say.mp3", 'wb') as f:  # 改为流式输出如何
                r.raw.decode_content = True  
                shutil.copyfileobj(r.raw, f)
        else:
            self.log.add("BaiduTTS: Tts error! Status code: " + str(r.status_code), 3)
