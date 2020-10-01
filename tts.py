# coding=utf-8
# author: Lan_zhijiang
# description: xiaolan's tts classes
# date: 2020/10/1

import requests
import shutil
import urllib.parse
import threading

from player import XiaolanPlayer


class BaiduTts():
    def __init__(self, log, setting):
        
        self.log = log
        self.setting = setting
        self.read_chunk = setting["player"]["readChunk"]
        self.player = XiaolanPlayer(log, setting)
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

        param = {'grant_type': 'client_credentials',
                 'client_id': self.app_key,
                 'client_secret': self.secret_key}
        params = urllib.parse.urlencode(param)
        r = requests.get('http://openapi.baidu.com/oauth/2.0/token', params=params)
        try:
            r.raise_for_status()
            token = r.json()['access_token']
            self.token = token
            return token
        except requests.exceptions.HTTPError:
            self.log.add_log("BaiduTTS: Getting token http error! Status code: " + str(r.status_code), 3)

    def put_data(self, data):

        """
        将数据放入player的输出队列中（2号线程）
        :param data: 要被放入的总数据
        :return:
        """
        self.log.add_log("BaiduTts: Putting data start, put chunk data into player's queue", 1)

        start = 0
        end = self.read_chunk-1

        c_data = data[start:end]
        while c_data != "":
            self.log.add_log("BaiduTts: Send chunk to player's queue", 0, is_print=False)
            self.player.put(c_data)
            start = end + 1
            end+=self.read_chunk
            c_data = data[start:end]

        for i in range(0, 2):
            self.player.put('')

    def start(self, text, is_play=True):

        """
        开始生成语音
        :param text: 要转换的文本
        :param is_play: 是否立即播放
        :return:
        """
        data = {
            'tex': text,
            'lan': 'zh',
            'tok': self.token,
            'ctp': 1,
            'cuid': 'b0-10-41-92-84-4d',
            'per': 4,
            'cue': 6
        }
        r = requests.post('http://tsn.baidu.com/text2audio',
                          data=data,
                          headers={'content-type': 'application/json'}, stream=True)

        if r.status_code == 200:
            r.raw.decode_content = True
            if is_play:
                put_data_t = threading.Thread(target=self.put_data, args=(data,))
                stream_out_t = threading.Thread(target=self.player.stream_output, args=())
                put_data_t.start()
                stream_out_t.start()
            else:
                with open("./data/audio/say.wav", "wb") as f:
                    shutil.copyfileobj(r.raw, f)
        else:
            self.log.add_log("BaiduTTS: Tts network error! Status code: " + str(r.status_code), 3)
