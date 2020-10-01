# coding=utf-8
# author: Lan_zhijiang
# description: xiaolan's startup
# date: 2020/10/1

import pyaudio
import queue


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
