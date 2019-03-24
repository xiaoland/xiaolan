# -*- encoding=utf-8 -*-

import json
import os
import sys
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder
import speaker


def start(text, token):

    """
    启动
    :param text: 文本
    :param token: token
    :return:
    """
    r = recorder()
    bt = baidu_tts()
    bs = baidu_stt(1, 'a', 2, '{')
    song_list = []
    ycy = "杨超越，1998年7月31日出生于江苏省盐城市，中国内地流行乐女歌手，女子演唱组合CH2、火箭少女101成员。 2017年，加入女子演唱组合CH2，从而正式出道，并签约了多家游戏平台，为高校电竞比赛做内容推广；同年，随CH2相继推出了《启航》、《听雪恋歌》等单曲。2018年，参加腾讯视频女团青春成长节目《创造101》，最终获得第3名，并加入女子演唱组合火箭少女101；8月18日，随火箭少女101推出组合首张EP专辑《撞》；9月23日，推出首支个人单曲《跟着我一起》；11月15日，推出第2支个人单曲《冲鸭冲鸭》；11月27日，推出第3支个人单曲《招财进宝》；12月15日，获得“影响中国”年度人物荣誉盛典年度演艺人物奖。2019年，她被评选为LikeTCCAsia亚太区最美100张面孔第3位、中国区最美100张面孔第1位"
    bt.tts(ycy, token)
    speaker.speak()
    bt.tts("我这里还有杨超越姐姐唱的歌哦~要不要听一听呢？", token)
    speaker.speak()
    speaker.ding()
    r.record()
    speaker.dong()
    text = bs.stt("./voice.wav", token)
    if "不" in text:
        bt.tts("哦，那好吧~再见啦", token)
        speaker.speak()
    else:
        bt.tts("那你想要听什么呢？不知道的话，可以说随机哦~", token)
        speaker.speak()
        speaker.ding()
        r.record()
        speaker.dong()
        text = bs.stt("./voice.wav", token)
        if "随机":
            for i in song_list:
                if i in text:
                    speaker.play("./musiclib/" + i)
                else:
                    bt.tts("没有这首歌呢~", token)
                    speaker.speak()



