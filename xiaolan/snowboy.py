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
import speaker
import time
sys.path.append('/home/pi/xiaolan/xiaolan/snowboy/')
import snowboydecoder

interrupted = False

def start():

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
    detector.start(detected_callback=back,
                   interrupt_check=interrupt_callback,
                   sleep_time=0.03)

    detector.terminate()
    
    
def back():

    xldo.convenstation()
    stop()

def stop():
    
    os._exit(0)
    

start()
            

