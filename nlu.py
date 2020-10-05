# coding=utf-8
# author: Lan_zhijiang
# description: old_xiaolan's nlu engine
# date: 2020/10/3

import time
import requests
import base64
import hashlib
from skill_manager import XiaolanSkillsManager


class XiaolanNlu():

    def __init__(self, log, setting):

        self.log = log
        self.setting = setting

        self.nlu_settings = self.setting["apiSettings"]["nlu"]
        self.xiaolan_skills = XiaolanSkillsManager(log, setting)

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
                    returns.append(self.xiaolan_skills.name_skill_list[text[2:]])
                return returns

        returns.append("talk")
        return returns

    def skill_nlu(self, text, data):

        """
        技能专用nlu
        :param text: 要处理的文本
        :param data: 对应识别典
        :return:
        """
        intent = None
        slot = None

        for keyword in data.keys():
            if keyword in text:
                intent = data[keyword]
                slot = text[len(keyword)-1:]
                return intent, slot

        return intent, slot
