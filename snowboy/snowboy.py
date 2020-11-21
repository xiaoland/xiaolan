# coding=utf-8
# author: Lan_zhijiang
# description: snowboy engine
# date: 2020/10/3

import snowboy.snowboydecoder


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
        detector = snowboy.snowboydecoder.HotwordDetector(self.setting["snowboySettings"]["hotword"],
                                                  sensitivity=self.setting["snowboySettings"]["sensitivity"],
                                                  audio_gain=1)
        detector.start(callback)

# awaken()
