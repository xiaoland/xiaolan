# -*- coding: utf-8 -*-
import sys
import os
import json
import requests
import pygame
import demjson
import time

intent = ''

def get_intent(text):
        ak = 'cd3c2238c7348d28363a1aad0b93d474'
        url = 'https://ai.aixxz.com'
        path = '/api?'

        data = {
                "city" = "中山"
                "nickname" = "tb"
                "text" = text
                "user" = "123456"
               }
        r = requests.post(url + path + data,
                          headers={'Authorization', 'APPCODE ' + appcode})
        json = r.json()
        domian = json['intent']
        return domain
        
        
def do_intent(domian, json)
        if intent == '':
            if domain == 'ticket':
                semantic = json['semantic']
                transportation = semantic['transportation']
                start_loc = semantic['start_loc']
                startdate = semantic['startdate']
                return startdate, start_loc, transportation
            elif domain == 'weather':
                semantic = json['semantic']
                city = semantic['city']
                return city
            elif domain == 'music':
                semantic = json['semantic']
                mode = semantic['mode']
                return mode
            elif domain == 'joke':
                sence = 'joke'
                return sence
            else:
                tuling = 'tuling'
                return tuling
        return domian
