# -*- coding: utf-8 -*-
# 录制系统

import wave
import pyaudio


class XiaolanRecorder():

    def __init__(self, log, setting):
        
        self.log = log
        self.setting = setting

        self.record_setting = setting["recordSettings"]
        self.format = pyaudio.paInt16
    
    def record(self, time=5):

        """
        录音
        :param time: 录音时间
        :return:
        """
        p = pyaudio.PyAudio()
        stream = p.open(format = self.format,
                        channels = self.record_setting["channel"],
                        rate = self.record_setting["rate"],
                        input = True,
                        frames_per_buffer=self.record_setting["chunk"])

        self.log.add_log("XiaolanRecorder: Recording...", 1)

        frames = []
        for i in range(0, int(self.record_setting["rate"] / self.record_setting["chunk"] * time)):
            data = stream.read(self.record_setting["chunk"])
            frames.append(data)

        self.log.add_log("XiaolanRecorder: Record end", 1)

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(self.record_setting["outputPath"], 'wb')
        wf.setnchannels(self.record_setting["channel"])
        wf.setsampwidth(p.get_sample_size(self.format))
        wf.setframerate(self.record_setting["rate"])
        wf.writeframes(b''.join(frames))
        wf.close()
