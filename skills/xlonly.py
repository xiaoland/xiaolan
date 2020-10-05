# -*- coding: utf-8 -*-
'''小蓝技能——父母私人助理，孝顺好帮手'''
import sys

sys.path.append('/home/pi/old_xiaolan/old_xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import recorder
from xiaolan import speaker


def xlonly(tok):
    
    saytext1 = '老爸，老妈，你们好啊，我是你们儿女派来的私人助理，小蓝'
    saytext3 = '有什么吩咐吗？'

    saytext2 = saytext1.encode('utf-8','strict')
    saytext4 = saytext3.encode('utf-8','strict')
    bt = baidu_tts()
    bt.tts(saytext2, tok)
    speaker.speak()
    bt.tts(saytext4, tok)
    speaker.speak()
    speaker.ding()
    recorder.record()
    speaker.dong()
    bs = baidu_stt(1, token, 2, '{')
    
    
    
