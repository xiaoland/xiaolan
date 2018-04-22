# -*- coding: utf-8 -*-
# 录制系统

import wave, pyaudio
import numpy as np
import sys
import os


CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 16000
CHANNELS = 1
RECORD_SECONDS = 5
SRECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "voice.wav"
TRAIN_F = "train_f.wav"
TRAIN_S = "train_s.wav"
TRAIN_T = "train_t.wav"

class recorder(object):
    def __init__(self):
        
        pass
    
    def record(self): # 录制指令（这里没有问题）
        p = pyaudio.PyAudio()
        stream = p.open(format = FORMAT,
                        channels = CHANNELS,
                        rate = RATE,
                        input = True,
                        frames_per_buffer=CHUNK)
        print "* recording"
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print "* done recording"

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
    
    def train_f_record(self): # 录制指令（这里没有问题）
        p = pyaudio.PyAudio()
        stream = p.open(format = FORMAT,
                        channels = CHANNELS,
                        rate = RATE,
                        input = True,
                        frames_per_buffer=CHUNK)
        print "* recording"
        frames = []
        for i in range(0, int(RATE / CHUNK * SRECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print "* done recording"

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(TRAIN_F, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        
     def train_s_record(self): # 录制指令（这里没有问题）
        p = pyaudio.PyAudio()
        stream = p.open(format = FORMAT,
                        channels = CHANNELS,
                        rate = RATE,
                        input = True,
                        frames_per_buffer=CHUNK)
        print "* recording"
        frames = []
        for i in range(0, int(RATE / CHUNK * SRECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print "* done recording"

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(TRAIN_S, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        
     def train_t_record(self): # 录制指令（这里没有问题）
        p = pyaudio.PyAudio()
        stream = p.open(format = FORMAT,
                        channels = CHANNELS,
                        rate = RATE,
                        input = True,
                        frames_per_buffer=CHUNK)
        print "* recording"
        frames = []
        for i in range(0, int(RATE / CHUNK * SRECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print "* done recording"

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(TRAIN_T, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()


