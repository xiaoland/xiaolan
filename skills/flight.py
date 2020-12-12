# -*- coding: utf-8 -*-
import requests
import json
import sys
import time
from tts import BaiduTts
from stt import BaiduStt
from player import XiaolanPlayer
from recorder import XiaolanRecorder


class XiaolanSkillFlightSearcher:

    def __init__(self, log, setting, text):

        self.log = log
        self.setting = setting
        self.text = text

        self.tts = BaiduTts(log, setting)
        self.stt = BaiduStt(log, setting)
        self.recorder = XiaolanRecorder(log, setting)
        self.player = XiaolanPlayer(log, setting)

    def request_csairlines(self, dep, arr, date, cities_info_list, token):

        flight_list = {}
        url = "https://b2c.csair.com/portal/flight/direct/query"
        dep_code = cities_info_list[dep.decode()][0]
        arr_code = cities_info_list[arr.decode()][0]
        self.log.add_log("Skill-FlightSearcher: dep city code: " + dep_code, 1)
        self.log.add_log("Skill-FlightSearcher: arr city code: " + arr_code, 1)
        param = {
            "depCity": dep_code,
            "arrCity": arr_code,
            "flightDate": str(date),
            "adultNum": "1",
            "childNum": "0",
            "infantNum": "0",
            "cabinOrder": "0",
            "airLine": 1,
            "flyType": 0,
            "international": "0",
            "action": "0",
            "segType": "1",
            "cache": 1,
            "preUrl": "",
            "isMember": ""
        }
        r = requests.post(url,
                      data=json.dumps(param),
                      headers={"Content-Type": "application/json"})
        res = r.json()
        if res["success"] is True:
            res_data = res["data"]["segment"][0]["dateFlight"]
            for i in res_data["flight"]:
                flight_list[i["flightNo"]] = i
        else:
            self.log.add_log("Skill-FlightSearcher: Flight search fail", 3)
            self.log.add_log("    Error code:" + res["errorCode"], 3)
            self.log.add_log("    Error msg:" + res["errorMsg"], 3)
            self.log.add_log("    The response: \n" + str(res), 3)
        return flight_list


    def get_cities_info_list(self):

        cities_info_list = {}
        url = "https://www.csair.com/cn/scripts/city/getcitylist.html?callback=getB2CCmsCity&_=1564394534382"
        r = requests.get(url)
        content = r.content.decode().replace("getB2CCmsCity(", "").replace(")", "")
        res = json.loads(content)

        for i in res["cities"]:
            cities_info_list[i[0]] = [i[4], i[11]]
        return cities_info_list
    
    def main(self):

        self.tts.start("Welcome using the FlightTracer. Made by Lan_zhijiang")
        self.tts.start("Loading cities... please wait...")
        cities_info_list = self.get_cities_info_list()
        self.tts.start("Load finished")
        
        self.tts.start("请问你要从哪里出发？请说出城市名")
        self.player.ding()
        self.recorder.record()
        self.player.dong()
        dep = self.stt.start()

        self.tts.start("请问你要到哪里去？请说出城市名")
        self.player.ding()
        self.recorder.record()
        self.player.dong()
        arr = self.stt.start()

        date = self.log.get_date()
        self.tts.start("请问你要什么时候出发？月份+日期，今天是" + date)
        self.player.ding()
        self.recorder.record()
        self.player.dong()
        date = "20190811"

        self.log.add_log("Skill-FlightSearcher: Confirming info...", 1)

        self.log.add_log.tts("Information confirm completed", 1)
        self.log.add_log("Searching for the flight...please wait...", 1)
        flight_list = self.request_csairlines(dep, arr, date, cities_info_list, 1)
        flight_num_list = list(flight_list.keys())
        for i in flight_num_list:
            dep_time = flight_list[i]["depTime"][0:2] + ":" + flight_list[i]["depTime"][2:4]
            arr_time = flight_list[i]["arrTime"][0:2] + ":" + flight_list[i]["arrTime"][2:4]
            self.tts.start(i + "，这趟航班的经济舱价格是" + 
                    str(flight_list[i]["cabin"][-1]["adultPrice"]) + 
                    "，出发时间是" + str(dep_time) + 
                    "，到达时间是" + str(arr_time))
