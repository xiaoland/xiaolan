# coding=utf-8
# author: Lan_zhijiang
# description: snowboy engine
# date: 2020/10/3

import snowboydecoder


class XiaolanSnowboy():

    def __init__(self, log, setting):

        self.log = log
        self.setting = setting

    def run(self, callback):

        """
        启动snowboy
        :param callback: 回调函数
        :return:
        """
        detector = snowboydecoder.HotwordDetector(self.setting["snowboySettings"]["hotwordPath"],
                                                  sensitivity=0.5,
                                                  audio_gain=1)
        detector.start(callback)

# awaken()
