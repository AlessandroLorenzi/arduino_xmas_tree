#!/bin/sh


echo -n   "Starting TWITTER       [WORK]"
nohup ./server_twitter.py 2> ./log/twitter_erros > ./log/twitter_messages &
echo $! > pid/server_twitter.pid
echo -e "\rStarting TWITTER       [ OK ]"

echo -n   "Starting WEB           [WORK]"
nohup ./server_www.py 2> ./log/www_errors > ./log/www_messages &
echo $! > pid/server_www.pid
echo -e "\rStarting WEB           [ OK ]"

echo -n   "Starting RANDOM        [WORK]"
nohup ./server_random.py 2> ./log/random_errors > ./log/random_messages &
echo $! > pid/server_random.pid
echo -e "\rStarting RANDOM        [ OK ]"
