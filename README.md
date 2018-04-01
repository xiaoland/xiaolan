# xiaolan---中文的智能家居控制对话机器人

这是一个中文的智能家居控制对话机器人——由叮当衍生而来，目前还未100%完成，所以发上来，希望大家一起研发，一个人研发也没那么多点子和经验
- 一、本机器人的测试环境为：
  - 树莓派3B
  - python
  - 阵列麦克风（可换）
  - 海威特音响（可换）

- 二、使用方法：
  - 准备以上硬件
  - 将小蓝git下来
  - 安装一下东东：
    - sudo apt-get install cmake g++ gcc
    - sudo apt-get install python2.7 python3 python-pyaudio python3-pyaudio sox
    - su root(如果还没有启用root账户，输入sudo passwd root, sudo passwd --unlock root)
    - pip install pyaudio
    - sudo apt-get install python3-dev python-dev libatlas-base-dev
  - 修改/测试(可以在github修改了再提交

- 三、文件体系：
xiaolan:
  - xldo.py #中心文件
  - stt.py #语音转文字
  - tts.py #文字转语音
  - speaker.py #音响
  - recorder.py #录音
  - snowboy.py #snowboy主控
  
  - musiclib #音乐库
    - ding.wav
    - dong.wav
    - welcome.mp3
  - skills #技能
    - xlonly.py #父母私人助理技能
    - weather.py # 天气查询技能
    - news.py #新闻播技能
    - story.py #讲故事技能
    - joke.py #笑话技能
    - tuling.py #图灵机器人对话接入技能
    - clock.py #闹钟技能
    
  - snowboy #snowboy唤醒引擎
    - demo.py
    - snowboydecoder.py #snowboy主要文件
    - xiaolanxiaolan.pmdl #小蓝小蓝唤醒词
    - .....(不一一列举）
  
- 五、
  各位的帮助我将感激不胜！！！
  有更新请写在xiaolanupdate.txt里面
  更新格式：
  日期：
  事件  （谁做的）
