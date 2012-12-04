#!/usr/bin/env python

import tweepy
from arduino import Arduino
from conf import conf
		
class StdOutListener(tweepy.StreamListener):
	a=Arduino(conf.arduini)
	#a=Arduino(['/dev/ttyACM1'])

	def on_data(self, data):
		d = json.loads(data)
		print d['user']['screen_name'] + " -  " + d['text']
		self.a.decode(d['text'])
		return True

	def on_error(self, status):
		print status

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

