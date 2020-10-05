import sys
import RPi.GPIO as gpio

sys.path.append('/home/pi/xiaolan/xiaolan/')
from xiaolan import speaker
from stt import baidu_stt
from tts import baidu_tts

__author__ = 'Caibiy'

import Adafruit_DHT,os,time, sqlite3

conn,cursor=(None,None)
#gpio
@unique

def start(tok):
  
	main(tok)

def main(tok):
	initDb()
  s = sth()
	s.readDth()
  
class gpio(Enum):
	pdht11=1
	pmq2=2
	pbuzzer=3

#初始化数据库
def initDb():
	global conn,cursor
	conn = sqlite3.connect("./db/smarthome.db")
	cursor = conn.cursor()
	#图片表
	cursor.execute('''CREATE TABLE IF NOT EXISTS pic (
	 		picid  INT UNSIGNED  PRIMARY KEY ,
	 		time  VARCHAR (100) NOT NULL
			)''')
	#温度表
	cursor.execute('''CREATE TABLE IF NOT EXISTS dth (
	 		dthid  INT UNSIGNED  PRIMARY KEY ,
	 		temp  VARCHAR (100) NOT NULL,
			humidity VARCHAR(100) NOT NULL
			)''')
	#mq2表
	cursor.execute('''CREATE TABLE IF NOT EXISTS mq2 (
	 		mq2id  INT UNSIGNED  PRIMARY KEY ,
	 		lpg  VARCHAR (100) NOT NULL,
			co VARCHAR(100) NOT NULL,
			smoke VARCHAR(100) NOT NULL
			)''')
	#操作记录表
	cursor.execute('''CREATE TABLE IF NOT EXISTS operalog (
	 		id  INT UNSIGNED  PRIMARY KEY ,
			time VARCHAR(100) NOT NULL,
			operaid VARCHAR(100) NOT NULL,
			type VARCHAR(100) NOT NULL
			)''')
	conn.commit()
#执行sql
def executeDb(sql):
	global conn,cursor
	cursor.execute(sql)
	conn.commit()	
#主控包含传感器、蜂鸣器
class sth(object):
	sensor = Adafruit_DHT.DHT11
	@property
	def sensor(self):
		return self.sensor
	def __init__(self):
		#初始化mode
		os.system('gpio -g mode %s out' % gpio.pdht11.value)
		os.system('gpio -g mode %s out' % gpio.pmq2.value)
		os.system('gpio -g mode %s out' % gpio.pbuzzer.value)
	#蜂鸣器
	def buzzer(self):
		os.system('gpio -g write %s 1' % gpio.pbuzzer.value)
		time.sleep(0.5)
		os.system('gpio -g write %s 0' % gpio.pbuzzer.value)
	#读取dth11温度
	def readDth(self):
    bt = baidu_tts()
    bs = baidu_stt(1, 'a', '{', 3)
		humidity,temperature = Adafruit_DHT.read_retry(self.sensor,gpio.pdht11.value)
		if humidity is not None and temperature is not None:
			saytext = '湿度是,' + humidity + '温度是' + temperature
      tok = bt.get_token()
      bt.tts(saytext, tok)
      speaker.speak()
      
    
