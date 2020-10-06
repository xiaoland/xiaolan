# coding=utf-8
# author: Lan_zhijiang
# description: XiaolanSkill: music player
# date: 2020/10/6

import requests
import urllib.parse
from stt import BaiduStt
from tts import BaiduTts
from player import XiaolanPlayer
from recorder import XiaolanRecorder
from nlu import XiaolanNlu


class XiaolanSkillMusicPlayer(object):
    
    def __init__(self, log, setting, text):
        
        self.log = log
        self.setting = setting
        self.text = text

        self.stt = BaiduStt(log, setting)
        self.tts = BaiduTts(log, setting)
        self.nlu = XiaolanNlu(log, setting)
        self.player = XiaolanPlayer(log, setting)
        self.recorder = XiaolanRecorder(log, setting)

        self.play_list = {}

        self.nlu_dict = {
            "恢复": "resume",
            "播放": "play",
            "暂停": "pause",
            "下一首": "next",
            "上一首": "previous",
            "添加": "add",
            "退出": "quit"
        }

    def start(self):

        """
        启动
        :return:
        """
        self.log.add_log("XiaolanSkillMusicPlayer: Start", 1)

        self.tts.start("请问你要听什么音乐呢？")
        self.main()

    def conversation(self):

        """
        对话（减少重复代码）
        :return:
        """
        self.player.ding()
        self.recorder.record()
        self.player.dong()

        text = self.stt.start()

        intent, slot = self.nlu.skill_nlu(text, self.nlu_dict)
        if intent is None:
            self.log.add_log("XiaolanSkillMusicPlayer: Intent is none, quit", 1)
            self.tts.start("不好意思，我没明白，退出咯~")
            intent, text, slot = None, None, None
        self.log.add_log("XiaolanSkillMusicPlayer: Intent: " + intent + " Text: " + text
                         + " Slot: " + slot, 1)
        return intent, text, slot

    def main(self):

        """
        主业务逻辑
        :return:
        """
        intent, text, slot = self.conversation()

        if intent == "quit":
            self.tts.start("好的，那么bye~")
            return
        elif intent == "play":
            result = self.search(slot)
            if result is None:
                self.tts.start("没有找到你要找的曲目，你可以试着换个说法")
                self.main()
            else:
                self.play(result)
        else:
            pass
            # NOT FINISHED

        self.tts.start("还要继续吗？")

        intent, text, slot = self.conversation()
        if intent is None:
            return
        if intent == "yes":
            self.main()
        else:
            self.tts.start("好的，我走啦，下次再见~")

    def play(self, data):

        """
        播放
        :param data: 播放参数
        :return:
        """
        self.log.add_log("XiaolanSkillMusicPlayer: Start play...", 1)

        url = "https://wwwapi.kugou.com/yy/index.php?"
        param = {
            "r": "play/getdata",
            "hash": data["fileHash"]
        }
        param = urllib.parse.urlencode(param)

        r = requests.get(url+param)
        if r.status_code == 200:
            res = r.json()
            play_url = res["data"]["play_url"].replace("\\\\", "")

            self.log.add_log("XiaolanSkillMusicPlayer: Play url: " + play_url, 1)

            r2 = requests.get(play_url)
            file = open("./data/audio/music" + data["fileFormat"], "wb")
            file.write(r2.content)
            file.close()

            self.player.format_converter("/data/audio/music"+data["fileFormat"], data["fileFormat"], ".wav")

            self.player.play("./data/audio/music.wav")
        else:
            self.log.add_log("XiaolanSkillMusicPlayer: Can't get: " + data["fileHash"] + " 's play url. Http error", 3)
            return None

    def search(self, keyword):

        """
        搜索曲目
        :param keyword: 关键词
        :return:
        """
        self.log.add_log("XiaolanSkillMusicPlayer: Search for song named: " + keyword, 1)

        url = "https://complexsearch.kugou.com/v2/search/song?"

        param = {
            "callback": "callback123",
            "keyword": keyword,
            "page": 1,
            "pagesize": 30,
            "bitrate": 0,
            "isfuzzy": 0,
            "tag": "em",
            "inputtype": 0,
            "platform": "WebFilter",
            "userid": -1,
            "clientver": 2000,
            "iscorrection": 1,
            "privilege_filter": 0,
            "srcappid": 2919,
            "clienttime": 1601950702328,
            "mid": 1601950702328,
            "uuid": 1601950702328,
            "dfid": "-",
            "signature": "10C3F1C841892B24FD43DE172EB765EA"
        }
        param = urllib.parse.urlencode(param)

        r = requests.get(url+param)
        if r.status_code == 200:
            res = r.json()
            data = res["data"]["lists"]
            file_format = "." + data[0]["HQExtName"]
            song_name = data[0]["SongName"].replace("em>", "").replace("<", "").replace("/", "")
            singer_name = data[0]["SingerName"]
            file_hash = data[0]["HQFileHash"]

            self.log.add_log("XiaolanSkillMusicPlayer: song: " + song_name + " singer: " + singer_name
                             + " file hash: " + file_hash, 1)

            return {
                "fileFormat": file_format,
                "fileHash": file_hash,
                "songName": song_name,
                "singerName": singer_name
            }
        else:
            self.log.add_log("XiaolanSkillMusicPlayer: Search: " + keyword + " failed. Http error", 3)
            return None

