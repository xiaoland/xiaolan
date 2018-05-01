# -*- coding: UTF-8 -*-
import sys
import base64
import requests
import os
import json
import demjson
import base64
sys.path.append('/home/pi/xiaolan/xiaolan/')
import speaker
from stt import baidu_stt
from tts import baidu_tts
from recorder import recorder

def start():
    
    main()

def get_wave(fname):
    with open(fname) as infile:
        return base64.b64encode(infile.read())


endpoint = "https://snowboy.kitt.ai/api/v1/train/"


############# MODIFY THE FOLLOWING #############
token = "78ee816d9bfc8fb0e01341d4408e3f23fbbc9b03"
hotword_name = "blueberry"
language = "en"
age_group = "20_29"
gender = "M"
microphone = "macbook microphone"
############### END OF MODIFY ##################


def main():
    
    r = recorder()
    bt = baidu_tts()
    tok = bt.get_token()
    url = 'https://snowboy.kitt.ai/api/v1/train/'
    apikey = '78ee816d9bfc8fb0e01341d4408e3f23fbbc9b03'
    askf = '第一次训练录音开始，请在滴一声之后说出，blueberry'
    asks = '第二次训练录音开始，请在滴一声之后说出，blueberry'
    askt = '第三次训练录音开始，请在滴一声之后说出，blueberry'
    bt.tts(askf, tok)
    speaker.speak()
    speaker.ding()
    r.train_f_record()
    speaker.dong()
    bt.tts(asks, tok)
    speaker.speak()
    speaker.ding()
    r.train_s_record()
    speaker.dong()
    bt.tts(askt, tok)
    speaker.speak()
    speaker.ding()
    r.train_t_record()
    speaker.dong()
    wav1 = "/home/pi/xiaolan/xiaolan/train_f.wav"
    wav2 = "/home/pi/xiaolan/xiaolan/train_s.wav"
    wav3 = "/home/pi/xiaolan/xiaolan/train_t.wav"
    out = "/home/pi/xiaolan/xiaolan/snowboy/blueberry.pmdl"
    data = {
        "name": hotword_name,
        "language": language,
        "age_group": age_group,
        "gender": gender,
        "microphone": microphone,
        "token": token,
        "voice_samples": [
            {"wave": get_wave(wav1)},
            {"wave": get_wave(wav2)},
            {"wave": get_wave(wav3)}
        ]
    }

    response = requests.post(endpoint, json=data)
    if response.ok:
        with open(out, "w") as outfile:
            outfile.write(response.content)
        print "Saved model to '%s'." % out
        trueback = "Saved model to '%s'." % out
        bt.tts(tureback, tok)
        speaker.speak()
    else:
        print "Request failed."
        print response.text
