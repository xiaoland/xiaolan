# xiaolan小蓝----中文交互式智能家居机器人
![Code主要语言](https://img.shields.io/badge/code-python-blue.svg)
![Version版本](https://img.shields.io/badge/version-dev-green.svg)
![build编写进度](https://img.shields.io/badge/build-54%25-brightgreen.svg)
![QQ](https://img.shields.io/badge/QQ-1481605673-yellow.svg)


这是一个中文的智能家居控制对话机器人——由叮当衍生而来，目前还未100%完成，所以发上来，希望大家一起研发，一个人研发也没那么多点子和经验

- 对不起！因为我只是一个刚上初一的小孩，所以如果有任何觉得使用不方便或者错误的地方，希望多多谅解
## 唤醒词问题：
- 由于本机器人的语音唤醒引擎是snowboy的
- 所以唤醒词英文的会比较准确，所以使用了唤醒词blueberry，比以前的中文唤醒词要好得多，翻译过来就是蓝莓，也没有脱离主题
- 但是snowboy的唤醒词是越多人训练则越准确，所以希望大家在使用小蓝的同时，打开下面的snowboy训练连接，只需要录制三次音频即可
- 网址：https://snowboy.kitt.ai/hotword/20710 （记得录音时说blueberry）
## 介绍以及本开源项目的所有请看：
### https://github.com/xiaoland/xiaolan-dev/wiki
![服务架构](https://github.com/xiaoland/xiaolan-dev/blob/master/%E5%B0%8F%E8%93%9D%E6%9C%8D%E5%8A%A1%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE.PNG)

## 重大更新：
- 利用讯飞AIUI平台实现了语义理解！
  - 已经完成云端的语义理解
  - 对客户的指令理解更加准确
- 实现开机自启！
  - 使用install_all.sh脚本进行一键安装，自带开机启动设置
- 说出唤醒词训练即可训练唤醒词！
