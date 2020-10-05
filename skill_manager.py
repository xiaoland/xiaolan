# coding=utf-8
# author: Lan_zhijiang
# description: To saving the keyword skill class
# date: 2020/10/4

from skills.clock import XiaolanSkillClock
from skills.tuling import XiaolanSkillTuling

class XiaolanSkills():

    def __init__(self, log, setting):

        self.log = log
        self.setting = setting

        self.keyword_intent_list ={
            "闹钟": "clock",
            "打开": "call_skill",
            "天气": "weather",
            "翻译": "translate",
            "搜索": "search",
            "聊天": "talk",
            "闲聊": "talk",
            "关机": "shutdown",
            "重启": "reboot",
            "怎么走": "map",
            "订": "book",
            "新闻": "news",
            "笑话": "joke",
            "播放": "play"
        }
        self.name_skill_list = {
            "智能家居": "hass",
            "酷狗音乐": "kugou_music",
            "航班查询": "flight_searcher"
        }
        self.intent_skills_list = {
            "clock": XiaolanSkillClock,
            "weather": XiaolanSkillTuling,
            "talk": XiaolanSkillTuling,
            "joke": XiaolanSkillTuling
        }
        self.skill_skills_list = {
            "hass": XiaolanSkillHass,
            "kugou_music": XiaolanSkillMusicPlayer,
            "flight_searcher": XiaolanSkillFlightSearcher
        }