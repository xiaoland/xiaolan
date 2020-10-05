# coding=utf-8
# author: Lan_zhijiang
# description: xiaolan's startup
# date: 2020/10/1

import json
import os
from snowboy.snowboy import XiaolanSnowboy
from log import XiaolanLog
from recorder import XiaolanRecorder
from player import XiaolanPlayer
from nlu import XiaolanNlu
from skill_manager import XiaolanSkills
from tts import BaiduTts
from stt import BaiduStt


class XiaolanInit():

    def __init__(self):

        self.setting = json.load(open("./data/json/setting.json", "r", encoding="utf-8"))
        self.log = XiaolanLog()

        self.tts = BaiduTts(self.log, self.setting)
        self.stt = BaiduStt(self.log, self.setting)
        self.nlu = XiaolanNlu(self.log, self.setting)
        self.player = XiaolanPlayer(self.log, self.setting)
        self.recorder = XiaolanRecorder(self.log, self.setting)
        self.skills = XiaolanSkills(self.log, self.setting)
        self.snowboy = XiaolanSnowboy(self.log, self.setting)

    def run(self):

        """
        启动小蓝
        :return:
        """
        print("""
        
            ########################################
                  小蓝-中文智能家居语音交互机器人
              (c)Lan_zhijiang all rights reserved
             http://github.com/xiaoland/xiaolan-dev
                E-mail: lanzhijiang@foxmail.com
            ########################################
        
        """)
        self.log.add_log("Xiaolan start! ", 1)
        self.log.add_log("Self checking...", 1)

        self.player.welcome()

        self.log.add_log("Start pulseaudio", 1)
        os.system("pulseaudio --start")

        self.log.add_log("Run snowboy awaken engine", 1)
        self.snowboy.run(self.callback)

    def callback(self):

        """
        回调函数
        :return:
        """
        self.log.add_log("XiaolanInit: Detected awaken from snowboy", 1)
        self.conversation()

    def conversation(self):

        """
        开始对话
        :return:
        """
        self.log.add_log("XiaolanInit: Start new conversation", 1)

        self.player.ding()
        self.recorder.record()
        self.player.dong()

        text = self.stt.start()
        if text is None:
            self.log.add_log("XiaolanInit: text result null", 3)
            self.player.text_none()
            return
        else:
            intent = self.nlu.get_intent(text)
            if intent[0] is None:
                self.player.intent_none()
                return
            else:
                if intent[0] == "call_skill":
                    self.skills.skill_skills_list[intent[1]](self.log, self.setting, text).start()
                else:
                    self.skills.intent_skills_list[intent[0]](self.log, self.setting, text).start()
