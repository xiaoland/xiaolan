# xiaolan---中文的智能家居控制对话机器人

这是一个中文的智能家居控制对话机器人——由叮当衍生而来，目前还未100%完成，所以发上来，希望大家一起研发，一个人研发也没那么多点子和经验
- 一、本机器人的测试环境为：
  - 树莓派3B
  - python
  - 阵列麦克风（可换）
  - 海威特音响（可换）

- 二、使用方法：
  - 准备以上硬件
  - 将小蓝git下来 git clone
  - 安装一下东东：
    - sudo apt-get install omxplayer mplayer
    - sudo apt-get install cmake g++ gcc
    - sudo apt-get install python2.7 python3 python-pyaudio python3-pyaudio sox
    - sudo apt-get install pulseaudio
    - su root(如果还没有启用root账户，输入sudo passwd root, sudo passwd --unlock root)
    - pip install pyaudio
    - pip install python3-requests python-request python-demjson python3-demjson
    - sudo apt-get install python3-dev python-dev libatlas-base-dev
  - 启动:
    - cd /home/pi/xiaolan/xiaolan
    - python xldo.py
  - 使用：
    - 1、语音唤醒
    - 2、人脸唤醒
    - 3、唤醒之后调用技能：
      - 1、新闻
      - 2、笑话
      - 3、智能家居
      - 4、天气
      - 5、闹钟
      - 6、酒店
      - 7、搜索
      - 8、拍照
      - 9、包裹
      - 10、邮件
      - 11、翻译
      - 12、路线
      - 13、查票
      - 14、日历
      - 15、笑话
      - 16、故事
      - 17、游戏
      - 18、猜谜
      - 19、开关机
      - 20、音乐
      - 21、......（大家一起开发）
  - 修改/测试(可以在github修改了再提交
  - 使用wiki维基百科在这里： https://github.com/xiaoland/xiaolan/wiki/%E7%9B%AE%E5%BD%95

- 六、文件体系：
  - xiaolan：
    - xldo.py #中心文件
    - stt.py #语音转文字
    - tts.py #文字转语音
    - speaker.py #音响
    - recorder.py #录音
    - snowboy.py #snowboy主控
  
    - musiclib #音乐库：
      - ding.wav
      - dong.wav
      - welcome.mp3
      - kacha.mp3
      - speacilrecorde.mp3
      - say.mp3
     
    - skills #技能：
      - xlonly.py #父母私人助理技能
      - weather.py # 天气查询技能
      - news.py #新闻播技能
      - story.py #讲故事技能
      - joke.py #笑话技能
      - tuling.py #图灵机器人对话接入技能
      - clock.py #闹钟技能
    
    - snowboy #snowboy唤醒引擎：
      - snowboydecoder.py #snowboy主要文件
      - xiaolanxiaolan.pmdl #小蓝小蓝唤醒词
      - .....(不一一列举）

- 七、:
  - 写插件请放在skills下面
  - 写插件请按照规则写插件，否则会调用失败
  - 详细的插件规则和教程请看：https://github.com/xiaoland/xiaolan/wiki/%E5%A6%82%E4%BD%95%E5%86%99%E6%8F%92%E4%BB%B6

- 八、:
  - 各位的帮助我将感激不胜！！！
