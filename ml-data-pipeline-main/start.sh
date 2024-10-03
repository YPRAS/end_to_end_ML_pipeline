#!bin/sh

#By using nohup, you can run a command in the background and ensure that it 
#continues to run even if you log out or close your terminal session.
nohup python producer_main.py &
python consumer_main.py