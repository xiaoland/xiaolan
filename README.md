# 小蓝--中文交互式智能家居机器人(在树莓派raspberrypi上运行)
![Code主要语言](https://img.shields.io/badge/main_code-python-blue.svg)
![Version版本](https://img.shields.io/badge/last_version-V2.5.7-green.svg)
![build编写进度](https://img.shields.io/badge/first_ver-68%25-brightgreen.svg)
![QQ](https://img.shields.io/badge/QQ-1481605673-yellow.svg)


这是一个中文的智能家居控制对话机器人——由叮当衍生而来，目前还未100%完成，所以发上来，希望大家一起研发，一个人研发也没那么多点子和经验

- 对不起！因为我只是一个刚上初一的小孩，所以如果有任何觉得使用不方便或者错误的地方，希望多多谅解
- 如果大家有点子的话，加我QQ：1481605673，我真诚的邀请您成为小蓝的开发者

# 注意：小蓝即将下架一段时间，重新整顿代码，这段时间内将会无法git clone本项目，敬请谅解

## 唤醒词问题：
- 由于本机器人的语音唤醒引擎是snowboy的
- 所以唤醒词英文的会比较准确，所以使用了唤醒词blueberry，比以前的中文唤醒词要好得多，翻译过来就是蓝莓，也没有脱离主题
- 但是snowboy的唤醒词是越多人训练则越准确，所以希望大家在使用小蓝的同时，打开下面的snowboy训练连接，只需要录制三次音频即可
- 网址：https://snowboy.kitt.ai/hotword/20710 （记得录音时说blueberry）
## 介绍本开源项目和WIKI请看：
### https://github.com/xiaoland/xiaolan-dev/wiki
![服务架构](https://github.com/xiaoland/xiaolan-dev/blob/master/%E5%B0%8F%E8%93%9D%E6%9C%8D%E5%8A%A1%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE.PNG)

## 更新：（有时间先后顺序）
- 利用讯飞AIUI平台实现了语义理解（NLU）！
  - 已经完成云端的语义理解（NLU）
  - 对客户的指令理解更加准确
- 实现开机自启！（使用install_all.sh脚本进行一键安装，自带开机启动设置）
- 说出唤醒词训练即可训练唤醒词！
- 智能家居插件已经可以控制灯、开关、遥控和获取传感器的数据（可以控制灯的颜色）
- 新闻、翻译、智能家居、音乐等插件已经加入了一句话功能
- 使用Alexa.pmdl唤醒可以三米以内唤醒
- 发布了[小蓝-V2.5 成熟稳定版本](https://github.com/xiaoland/xiaolan-dev/releases)
- 一句话功能放置到nlp.py中，加快速度
- 加快tuling.py的相应速度
- 删去不必要的元素
- 开机只需请求一次百度token，大大提升速度
- 添加百度音乐技能
- 添加第三方邮箱邮件发送技能
