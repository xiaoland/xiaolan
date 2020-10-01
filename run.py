# coding=utf-8
# author: Lan_zhijiang
# description: xiaolan's startup
# date: 2020/10/1

import json
from log import XiaolanLog
from tts import BaiduTts

class XiaolanInit():

    def __init__(self):

        self.setting = json.load(open("./data/json/setting.json", "r", encoding="utf-8"))
        self.log = XiaolanLog()

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


