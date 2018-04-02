import Adafruit_DHT,os,time,datetime,sqlite3
conn,cursor=(None,None)

#初始化数据库
def initDb():
	global conn,cursor
	conn = sqlite3.connect("./db/smarthome.db")
	cursor = conn.cursor()
	#图片表如果不存在则创建
	cursor.execute('''CREATE TABLE IF NOT EXISTS pic (
	 		picid  INT UNSIGNED AUTO_INCREMENT PRIMARY KEY ,
	 		time  VARCHAR (100) NOT NULL
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
	def __init__(self,pdht11,pmq2,pbuzzer):
		self.__pdht11 = pdht11
		self.__pmq2 = pmq2
		self.__pbuzzer = pbuzzer
		#初始化mode
		os.system('gpio -g mode %s out' % pdht11)
		os.system('gpio -g mode %s out' % pmq2)
		os.system('gpio -g mode %s out' % pbuzzer)
	#蜂鸣器
	def buzzer(self):
		os.system('gpio -g write %s 1' % self.__pbuzzer)
		time.sleep(0.5)
		os.system('gpio -g write %s 0' % self.__pbuzzer)
	def readDth(self):
		humidity,temperature = Adafruit_DHT.read_retry(self.sensor,self.__pdht11)
		if humidity is not None and temperature is not None:
			print('temp:%s,humidity%d' % (humidity,temperature))
			return (humidity,temperature)
