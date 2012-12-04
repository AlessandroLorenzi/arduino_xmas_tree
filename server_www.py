#!/usr/bin/env python


from time import sleep
import httplib
from arduino import Arduino
from conf import conf

a=Arduino(conf.arduini)

while (True):
	
	try:
		conn = httplib.HTTPConnection('whitelabox.altervista.org')
		conn.request("GET", "/accensioneluci.txt")
		for command in conn.getresponse().read().split("\n"):
			a.decode(command)
		#print conn.getresponse().read()
		conn.close()
	except:
		print("error")

	sleep(2)

