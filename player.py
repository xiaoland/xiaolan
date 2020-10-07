# coding=utf-8
# author: Lan_zhijiang
# description: old_xiaolan's startup
# date: 2020/10/1

import pyaudio
import queue
import wave
import os


class XiaolanPlayer():

    def __init__(self, log, setting):

        self.log = log
        self.setting = setting

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

    def stream_output(self, data):

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

    def format_converter(self, fp, ori, goal):

        """
        音频文件格式转换器
        :param fp: 文件路径
        :param ori: 原格式
        :param goal: 目标格式
        :return:
        """
        self.log.add_log("XiaolanPlayer: Convert " + fp + " to " + goal, 1)
        soundpcm = os.getcwd() + fp.replace(ori, goal)
        cmd = 'ffmpeg -y -i ' + os.getcwd() + fp + ' -acodec pcm_u16 ' + soundpcm + ' '
        os.system(cmd)
