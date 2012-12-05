#!/bin/sh
kill `cat pid/server_twitter.pid`
kill `pid/server_www.pid`
kill `pid/server_random.pid`


rm pid/server_twitter.pid pid/server_www.pid pid/server_random.pid
