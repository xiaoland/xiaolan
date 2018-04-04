#! /usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'Caibiy'

import Adafruit_DHT,os,time,datetime,sqlite3,uuid
conn,cursor=(None,None)
#gpio
@unique
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
class smartHome(object):
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
		humidity,temperature = Adafruit_DHT.read_retry(self.sensor,gpio.pdht11.value)
		if humidity is not None and temperature is not None:
			print('temp:%s,humidity%d' % (humidity,temperature))
			saveDth(temperature,humidity)
			return (humidity,temperature)
	def saveDth(self,temp,humidity):
		executeDb('insert into dth (id,temp,humidity) VALUES (\'%s\',\'%s\',\'%s\') ' %  (uuid.uudi1(),temp,humidity))
		
#USB摄像头
class usbCamera(object):
	def __init__(self):
		pass
	def takePhoto(self):
		nowTime = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
		os.system('fswebcam  -r 1280x720 --no-banner ../img/%s.jpg' % nowTime)
		saveTime(nowTime)
	def saveTime(self,time):
		executeDb('insert into pic (id,time) VALUES (\'%s\',\'%s\') ' %  (uuid.uuid1(),time))
def init():
	global conn,cursor
	os.system('bash ./check.sh')
	s = smartHome()
	initDb()
	#humidity,temperature=s.readDth()
	#if humidity is not None and temperature is not None:
	#	if
	#释放资源
	conn.close()
	cursor.close();
	#uc = usbCamera()
	#uc.takePhoto()	
	

if __name__ =='__main__':
	init()
