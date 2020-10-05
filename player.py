# coding=utf-8
# author: Lan_zhijiang
# description: old_xiaolan's startup
# date: 2020/10/1

import pyaudio
import queue
import wave
from tts import BaiduTts


class XiaolanPlayer():

    def __init__(self, log, setting):

        self.log = log
        self.setting = setting
        self.tts = BaiduTts(log, setting)

        self.p = pyaudio.PyAudio()

        self.output_queue = queue.Queue(8)

    def put(self, data):

        """
        将块音频数据放入输出队列
        :param data: 要被放入的块数据
        :return:
        """
        self.log.add_log("Player: Receive data from tts, put in", 0, is_print=False)
        self.output_queue.put(data)

    def stream_output(self):

        """
        流式输出音频
        :param data: 二进制音频数据
        :return:
        """
        self.log.add_log("Player: Stream output start", 1)

        stream = self.p.open(
            format=self.p.get_format_from_width(2),
            channels=1,
            rate=160000,
            output=True)

        c_data = self.output_queue.get()
        while c_data != '':
            stream.write(c_data)
            c_data = self.output_queue.get()

        stream.stop_stream()
        stream.close()

        self.p.terminate()

    def welcome(self):

        """
        播放欢迎语（在线合成）
        :return:
        """
        self.log.add_log("XiaolanPlayer: Play the welcome speech(online tts)", 1)
        self.tts.start("你好啊，主人~这里是小蓝哦！")

    def text_none(self):

        """
        当stt结果为none时的播放
        :return:
        """
        self.log.add_log("XiaolanPlayer: Text is none, play text_none(online tts)", 1)
        self.tts.start("抱歉，我好像没听清")

    def intent_none(self):

        """
        当intent结果为none时的播放
        :return:
        """
        self.log.add_log("XiaolanPlayer: Intent is none, play intent_none(online tts)", 1)
        self.tts.start("我不是很明白你的意思")

    def play(self, fp):

        """
        基本play
        :param fp: 文件路径
        :return:
        """
        try:
            wf = wave.open(fp)
        except wave.Error:
            self.log.add_log("XiaolanPlayer: Cannot open the file", 3)
            return

        stream = self.p.open(
            format=self.p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )

        data = wf.readframes(1024)
        while data != "":
            stream.write(data)
            data = wf.readframes(1024)

        stream.stop_stream()
        stream.close()
        self.p.terminate()


    def say(self):

        """
        播放say.wav
        :return:
        """
        self.log.add_log("XiaolanPlayer: Now playing say.wav", 1)
        self.play(r"./data/audio/say.wav")

    def ding(self):

        """
        播放ding.wav
        :return:
        """
        self.log.add_log("XiaolanPlayer: Now playing ding.wav", 1)
        self.play(r"./data/audio/ding.wav")

    def dong(self):

        """
        播放dong.wav
        :return:
        """
        self.log.add_log("XiaolanPlayer: Now playing dong.wav", 1)
        self.play(r"./data/audio/dong.wav")
