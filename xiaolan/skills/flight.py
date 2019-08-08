# -*- coding: utf-8 -*-
import requests
import time
import json
sys.path.append('/home/pi/xiaolan/xiaolan/')
from stt import baidu_stt
from tts import baidu_tts
import speaker
import recorder


def request_csairlines(dep, arr, date, cities_info_list, token):

    flight_list = {}
    url = "https://b2c.csair.com/portal/flight/direct/query"
    dep_code = cities_info_list[dep][0]
    arr_code = cities_info_list[arr][0]
    baidu_tts().tts("dep city code:", dep_code)
    baidu_tts().tts("arr city code:", arr_code)
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
        baidu_tts().tts("Error!!!FlightSearchFaild", token)
        baidu_tts().tts("Error code:" + res["errorCode"], token)
        baidu_tts().tts("Error msg:" + res["errorMsg"], token)
        baidu_tts().tts(str(res))
    return flight_list


def get_cities_info_list():

    cities_info_list = {}
    url = "https://www.csair.com/cn/scripts/city/getcitylist.html?callback=getB2CCmsCity&_=1564394534382"
    r = requests.get(url)
    content = r.content.decode().replace("getB2CCmsCity(", "").replace(")", "")
    res = json.loads(content)

    for i in res["cities"]:
        cities_info_list[i[0]] = [i[4], i[11]]
    return cities_info_list


def main(token):

    baidu_tts().tts("Welcome using the FlightTracer")
    baidu_tts().tts("Made by Lan_zhijiang")
    baidu_tts().tts("Loading cities... please wait...")
    cities_info_list = get_cities_info_list()
    baidu_tts().tts("Load finished")
    dep = "北京"
    arr = "深圳"
    date = "20190811"

    baidu_tts().tts("Staring confirm info", token)

    baidu_tts().tts("Information confirm completed", token)
    baidu_tts().tts("Searching for the flight...please wait...", token)
    flight_list = request_csairlines(dep, arr, date, cities_info_list, token)
    flight_num_list = list(flight_list.keys())
    for i in flight_num_list:
        dep_time = flight_list[i]["depTime"][0:2] + ":" + flight_list[i]["depTime"][2:4]
        arr_time = flight_list[i]["arrTime"][0:2] + ":" + flight_list[i]["arrTime"][2:4]
        baidu_tts().tts(i + "，这趟航班的经济舱价格是" + flight_list[i]["cabin"][-1]["adultPrice"] + "，出发时间是" + dep_time + "，到达时间是" + arr_time, token)
