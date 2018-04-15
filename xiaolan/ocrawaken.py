import sys
import os
import requests
import base64
import json
import demjson
import xldo

class ocrawaken(object):
    
    def __init__(self):
      
        pass

    def get_token(self):
        AK = 'GuagSnlhsP8qKX2Lj7RbLomq'
        SK = 'PiwvPvXIyFdIO3Bc0F2GHtsGdAaeG73D'
        url = 'http://openapi.baidu.com/oauth/2.0/token'
        params = urllib.urlencode({'grant_type': 'client_credentials',
                                   'client_id': AK,
                                   'client_secret': SK})
        r = requests.get(url, params=params)
        try:
            r.raise_for_status()
            token = r.json()['access_token']
            return token
        except requests.exceptions.HTTPError:
            self._logger.critical('Token request failed with response: %r',
                                  r.text,
                                  exc_info=True)
            return token
      
    def ocrawaken(self, tok):
        os.system('fswebcam --no-banner -r 480x480 /home/pi/xiaolan/xiaolan/face.jpg')
        picture = '/home/pi/xiaolan/xiaolan/face.jpg'
        f = open(picture, 'rb')
        img = base64.b64encode(f.read())
        url = 'https://aip.baidubce.com/rest/2.0/face/v1/detect'
        
        data = {
                "image": img,
                "face_fields": "age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities"}
        
        r = requests.post(url,
                          data=data,
                          headers={'content-type': 'application/x-www-form-urlencoded'})
        
        json = r.json()
        faceyn = json['result'][0]['face_probability']
        if faceyn == 1:
            speaker.ocrawaken()
            xldo.convenstation()
        else:
            o = ocrawaken()
            tok = o.get_token()
            o.ocrawaken(tok)
