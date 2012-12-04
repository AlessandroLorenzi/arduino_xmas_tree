#!/usr/bin/env python

from arduino import Arduino
from random import random 
from conf import conf
from time import sleep


a=Arduino(conf.arduini)

while (True):
	led=(int(random()*20))
	if(int((random()*2))):
		command="on"+str(led)
	else:
		command="off"+str(led)
	a.decode(command)
	sleep(2)

