# coding=utf-8
# author: Lan_zhijiang
# description: xiaolan's nlu engine
# date: 2020/10/3

import time
import os
import requests
import base64
import hashlib
from skill_manager import XiaolanSkills


class XiaolanNlu():

    def __init__(self, log, setting):

        self.log = log
        self.setting = setting

        self.nlu_settings = self.setting["apiSettings"]["nlu"]
        self.xiaolan_skills = XiaolanSkills(log, setting)

    def get_intent(self, text):

        """
        请求讯飞NLU识别意图
        :param text: 文本
        :return:
        """
        self.log.add_log("XiaolanNlu: Getting intent with ifly nlu engine")

        url = 'http://api.xfyun.cn/v1/aiui/v1/text_semantic?text='
        app_id = self.nlu_settings["appId"]  # '5ace1bbb'
        api_key = self.nlu_settings["appKey"]  # '9e1b8f6028b14b969cdec166eca127ea'
        lastmdl = self.nlu_settings["lastMdl"]  # 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9'

        time_stamp = str(int(time.time()))

        try:
            base64_text = base64.b64encode(text)
        except TypeError:
            intent = None
            return intent
                
        text = 'text=' + text
        
        raw = api_key + time_stamp + lastmdl + text

        hash = hashlib.md5()
        hash.update(raw)
        check_sum = hash.hexdigest()
        
        headers = {'X-Appid': app_id,
                   'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
                   'X-CurTime': time_stamp,
                   'X-Param': 'eyJ1c2VyaWQiOiIxMyIsInNjZW5lIjoibWFpbiJ9',
                   'X-CheckSum': check_sum}
        url = url + base64_text
        
        r = requests.post(url,
                          headers=headers)
        try:
            json = r.json()
        except:
            return self.keyword_compare(text)

        try:
            intent = json['data']['service']
        except KeyError:
            return self.keyword_compare(text)
        except TypeError:
            return self.keyword_compare(text)

        if intent is not None:
            return [intent]
        else:
            return [None]

    def keyword_compare(self, text):

        """
        以关键词匹配方式获取意图
        :param text: 文本
        :return: str
        """
        returns = []
        for keyword in self.xiaolan_skills.keyword_intent_list.keys():
            if keyword in text:
                intent = self.xiaolan_skills.keyword_intent_list[keyword]
                returns.append(intent)

                if intent == "call_skill":
                    returns.append(self.xiaolan_skills.name_skill_list[text[2:len(text)]])
                return returns

        returns.append("talk")
        return returns


def do_intent(text, tok=""):
    sm = hass()
    m = xlMusic()
    services = {'musicurl_get': 'method=baidu.ting.song.play&songid=', 'search': 'method=baidu.ting.search.catalogSug&query=', 'hot': 'method=baidu.ting.song.getRecommandSongList&song_id=877578&num=12'}
    if text is not None:

        if '闹钟' in text:
                intent = 'clock'
                return intent
        elif '打开' in text:
                cortolthings = text[6:-2]
                print cortolthings
                cortolmode = 'turn_on'
                sm.cortol(cortolthings, cortolmode, tok)
        elif '关闭' in text:
                cortolthings = text[6:-2]
                cortolmode = 'turn_off'
                sm.cortol(cortolthings, cortolmode, tok)
        elif '天气' in text:
                intent = 'weather'
                return intent
        elif '重新说' in text or '重复' in text:
                intent = 'respeaker'
                return intent
        elif '翻译' in text:
                intent = 'translate'
                return intent
        elif '搜索' in text:
                intent = 'ser'
                return intent
        elif '闲聊' in text:
                intent = 'tuling'
                return intent
        elif '关机' in text:
                print ('SHUTDOWING...')
                os.system('sudo poweroff')
        elif '重启' in text:
                print ('REBOOTING...')
                os.system('sudo reboot')
        elif '怎么走' in text:
                intent = 'map'
                return intent
        elif '酒店' in text:
                intent = 'hotel'
                return intent
        elif '旅游' in text:
                intent = 'travel'
                return intent
        elif '做游戏' in text:
                intent = 'minigame'
                return intent
        elif '新闻' in text:
                intent = 'news'
                return intent
        elif '傻逼' in text:
                speaker.falu()
        elif '拍照' in text:
                intent = 'camera'
                return intent
        elif '邮件' in text or '邮件助手' in text:
                intent = 'mail'
                return intent
        elif '快递' in text:
                intent = 'experss'
                return intent
        elif '笑话' in text:
                intent = 'joke'
                return intent
        elif '训练' in text:
                intent= 'snowboytrain'
                return intent
        elif '播放' in text:
            if '音乐' in text:
                m.sui_ji(services, tok)
            else:
                songname = text[2:-1]
                m.sou_suo(services, songname, tok)
        elif "你知道我们现在在哪里" in text:
            baidu_tts().tts("我们现在在《中国少年说》的舞台上，如果我没记错的话，你回深圳的飞机票还没有买吧？", tok)
        elif "你要帮我买" in text:
            baidu_tts().tts("我可没有你的账户，但是我可以帮你查一下从北京到深圳的航班哦", tok)
            return "flight"
        elif '我想听' in text:
            if '音乐' in text:
                m.sui_ji(services, tok)
            else:
                songname = text[3:-1]
                m.sou_suo(services, songname, tok)
        else:
                tuling.start(text, tok)
    else:
        intent = 'no'
        return intent
