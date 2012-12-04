#!/usr/bin/env python

import sys
import tweepy
import json



class Arduino():
	'''
	Possono esserci fino a 10 arduini attaccati (fino a 100 luci)
	La classe viene inizializzata con una tupla di porte seriali, una per ogni arduino.

	Gli arduini vierranno gestiti come un unico arduino.
	
	se si riceve un messaggio tipo "on1-100" invia all'arduino giusto un numero da 1-100
	se si riceve un messaggio tipo "off1-100" invia all'arduino giusto un numero da 101-100
	
	L'arduino deve ricevere sulla porta seriale una stringa, trasformarla in intero e accendere/spegnere il led giusto.
	'''

	def __init__(self, ports):
		import serial
		self.s=list()
		for port in ports:
			self.s.append( serial.Serial(port=port, baudrate=9600))

	
	
	def decode(self, message):
		import re
		onstring="on[0-9]+"
		offstring="off[0-9]+"
		
		onmatches = re.findall(onstring,message)
		for match in onmatches:
			self.sendon(match.replace("on",""))

		offmatches = re.findall(offstring,message)
		for match in offmatches:
			self.sendoff(match.replace("off",""))
		

	def sendon(self, message):
		from time import sleep
		print("siamo in ON")	
		print(str(int(message)-(int(message)/10*10) ))
		self.s[int(message)/10].write(str(int(message)-(int(message)/10*10) ))
		sleep(0.2)
		

	def sendoff(self, message):
		from time import sleep
		print("siamo in OFF")	
		print(str(int(message)-(int(message)/10*10)+100))
		self.s[int(message)/10].write(str(int(message)-(int(message)/10*10)+100))
		sleep(0.2)
		
class StdOutListener(tweepy.StreamListener):
	#a=Arduino(['/dev/ttyACM0', '/dev/ttyACM1'])
	a=Arduino(['/dev/ttyACM0'])

	def on_data(self, data):
		d = json.loads(data)
		print d['user']['screen_name'] + " -  " + d['text']
		self.a.decode(d['text'])
		return True

	def on_error(self, status):
		print status

from conf import conf
CONSUMER_KEY=conf.CONSUMER_KEY
CONSUMER_SECRET=conf.CONSUMER_SECRET

ACCESS_KEY = conf.ACCESS_KEY
ACCESS_SECRET = conf.ACCESS_SECRET



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#api.update_status(sys.argv[1])


l = StdOutListener()
stream = tweepy.Stream(auth,l)
stream.filter(track=['#Arduino'])

