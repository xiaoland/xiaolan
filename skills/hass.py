# coding=utf-8
# author: Lan_zhijiang
# description: xiaolan skill: hass
# date: 2020/10/5

import requests
import json
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
        self.nlu = XiaolanNlu(log, setting)
        self.recorder = XiaolanRecorder(log, setting)
        self.player = XiaolanPlayer(log, setting)

        self.hass_settings = setting["skillSettings"]["hass"]
        self.hass_addr = self.hass_settings["hassAddress"]
        self.hass_token = self.hass_settings["token"]

        self.headers = {
            "Authorization": "Bearer " + self.hass_token,
            "Content-Type": "application/json"
        }

        self.components = self.hass_settings["components"]
        self.unit_system = self.hass_settings["unitSystem"]
        self.domain_services = self.hass_settings["domainServices"]
        self.entity_dict = self.hass_settings["entityDict"]
        self.friendly_name_dict = self.hass_settings["friendlyNameDict"]
        self.intent_service_list = self.hass_settings["intentToServiceList"]

        self.nlu_intent_dict = {
            "更新数据": "update_data",
            "打开": "turn_on",
            "关闭": "turn_off",
            "颜色": "set_color",
            "查看": "get_state",
            "设置": "set",
            "改": "set",
            "获取": "get_state",
            "是": "yes",
            "否": "no",
            "不": "no"
        }

    def start(self):

        """
        开始
        :return:
        """
        self.log.add_log("XiaolanSkillHass: Initializing...", 1)

        self.tts.start("Hi!~ 这里是智能家居控制系统~")

        self.main()

    def conversation(self):

        """
        对话（减少重复）
        :return:
        """
        self.player.ding()
        self.recorder.record()
        self.player.dong()

        text = self.stt.start()

        intent =  self.nlu.skill_nlu(text, self.nlu_intent_dict)
        if intent is None:
            self.log.add_log("XiaolanSkillHass: Intent is none, quit", 1)
            self.tts.start("不好意思，我没明白，退出咯~")
            return None
        return intent, text

    def main(self):

        """
        主逻辑程序（可多次对话）
        :return:
        """
        self.tts.start("有何贵干呐？敬请吩咐。若不明白如何操作，请查阅本技能的wiki")

        intent, text = self.conversation()
        if intent is None:
            return

        self.log.add_log("XiaolanSkillHass: Recognized intent: " + intent, 1)

        if intent == "update_data":
            self.update_data()
            self.tts.start("所有数据已更新")
        elif intent == "get_state":
            friendly_name = text[2:]
            state = self.get_state(self.friendly_name_dict[friendly_name])
            self.tts.start(friendly_name + "的状态是" + state["state"].replace("_", " "))

        self.tts.start("还要继续吗？")

        intent, text = self.conversation()
        if intent is None:
            return
        if intent == "yes":
            self.main()
        else:
            self.tts.start("好的，我走啦，下次再见~")

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

    def update_data(self):

        """
        更新所有数据
        :return:
        """
        self.log.add_log("XiaolanSkillHass: Update all data...", 1)
        self.get_services()
        self.get_entity_list()
        self.get_config()

        self.hass_settings["components"] = self.components
        self.hass_settings["unitSystem"] = self.unit_system
        self.hass_settings["domainServices"] = self.domain_services
        self.hass_settings["entityDict"] = self.entity_dict
        self.hass_settings["friendlyNameDict"] = self.friendly_name_dict

        self.setting["hassSettings"] = self.hass_settings

        json.dump(self.setting, open("./data/json/setting.json", "w", encoding="utf-8"))

        self.log.add_log("XiaolanSkillHass: Updated", 1)

    def get_config(self):

        """
        获取hass的配置
        :return:
        """
        self.log.add_log("XiaolanSkillHass: Get config", 1)
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
