# -*- coding: utf-8 -*-
#snowboy主控

import sys
import os
import json
import logging
import os
import signal
import sys
import xldo
sys.path.append('/home/pi/xiaolan/snowboy/')
import snowboydecoder

interrupted = False

def start(): # demo.py

    def signal_handler(signal, frame):
        global interrupted
        interrupted = True


    def interrupt_callback():
        global interrupted
        return interrupted

    model = '/home/pi/xiaolan/snowboy/xiaolanxiaolan.pmdl'
    
    # capture SIGINT signal, e.g., Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    print('Listening... Press Ctrl+C to exit')

    # main loop
    detector.start(detected_callback=xldo.convenstation,# 侦测到唤醒词后的操作（这里还好，但是还有BUG）
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)

    detector.terminate()
   
def stop():
    
    sys.exit(-1)

start()
            

