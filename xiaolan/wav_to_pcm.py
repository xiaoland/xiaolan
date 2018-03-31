# -*- coding: utf-8 -*-
# wav文件转pcm

import os
import sys
import json
import numpy as np
import wave
       
def wav_to_pcm():
    f = open("voice.wav")
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype=np.int16)
    data.tofile("voice.pcm")
