# coding=utf-8
# author: Lan_zhijiang
# description: xiaolan skill: hass
# date: 2020/10/5

import requests
from stt import BaiduStt
from tts import BaiduTts
from nlu import XiaolanNlu
from recorder import XiaolanRecorder
from player import XiaolanPlayer


class XiaolanSkillHass():

    def __init__(self, log, setting, text):

        self.log = log
        self.setting = setting
        self.text = text

        self.stt = BaiduStt(log, setting)
        self.tts = BaiduTts(log, setting)
        self.recorder = XiaolanRecorder(log, setting)
        self.player = XiaolanPlayer(log, setting)

        self.hass_settings = setting["skillSettings"]["hass"]
        self.hass_addr = self.hass_settings["hassAddress"]
        self.hass_token = self.hass_settings["token"]

        self.headers = {
            "Authorization": "Bearer " + self.hass_token,
            "Content-Type": "application/json"
        }

        self.components = []
        self.unit_system = {}
        self.domain_services = {}
        self.entity_dict = {}
        self.friendly_name_dict = {}

    def start(self):

        """
        开始
        :return:
        """

    def request(self, url, type, param=None):

        """
        使用requests库进行get/post请求（减少重复代码）
        :param url: 请求的地址
        :param param: 请求的数据 post才需要
        :param type: 请求类型 get/post
        :return:
        """
        if type == "get":
            r = requests.get(url,
                             headers=self.headers)
        elif type == "post":
            r = requests.post(url,
                              data=param,
                              headers=self.headers)
        else:
            return None

        if r.status_code == 200:
            return r
        else:
            self.log.add_log("XiaolanSkillHass: Request " + str(r.status_code), 3)
            self.log.add_log("    Data: " + str(param), 1)
            self.log.add_log("    Res: " + str(r.text), 1)
            return None

    def get_config(self):

        """
        获取hass的配置
        :return:
        """
        r = self.request(self.hass_addr+"/api/config",
                         "get")
        if r is not None:
            res = r.json()
            self.components = res["components"]
            self.unit_system = res["unit_system"]

    def get_services(self):

        """
        获取所有服务
        :return:
        """
        self.log.add_log("XiaolanSkillHass: Get all services' info", 1)

        r = self.request(self.hass_addr+"/api/services",
                         "get")
        if r is not None:
            res = r.json()
            for event in res:
                self.domain_services[event["domain"]] = event["services"]

    def get_entity_list(self):

        """
        获取所有对象的状态
        :return:
        """
        self.log.add_log("XiaolanSkillHass: Get all entities' info", 1)

        r = self.request(self.hass_addr + "/api/states",
                         "get")
        if r is not None:
            res = r.json()
            for event in res:
                state = self.get_state(event["entity_id"])
                self.entity_dict[event["entity_id"]] = {
                    "attr": state["attributes"],
                    "state": state["state"],
                    "friendly_name": state["friendly_name"]
                }
                self.friendly_name_dict[state["friendly_name"]] = event["entity_id"]

    def get_state(self, entity_id):

        """
        获取指定对象的状态
        :param entity_id: 实体id
        :return:
        """
        self.log.add_log("XiaolanSkillHass: Get state of" + entity_id, 1)

        r = self.request(self.hass_addr + "/api/states/" + entity_id,
                         "get")
        if r is not None:
            res = r.json()
            if r.status_code == 404:
                self.log.add_log("XiaolanSkillHass: Can't find " + entity_id + "'s state", 3)
                return None
            return res

    def call_service(self, domain, service, param):

        """
        呼叫某个服务
        :param domain: 服务所属领域
        :param service: 服务名
        :param param: 服务参数
        :return:
        """
        self.log.add_log("XiaolanSkillHass: Call " + domain + "/" + service + " with " +
                         str(param), 1)
        r = self.request(self.hass_addr + "/api/services/" + domain + "/" + service,
                         "post", param)
        if r is not None:
            res = r.json()
            return res
