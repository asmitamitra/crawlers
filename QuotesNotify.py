import subprocess
import random
import time
import sys

title = 'Quotes'
notification_delay = 30
check_delay = 60

file = open('_quotes.txt', 'r')
quotes = file.read()
quotes = quotes.split("\n")
apple_cmd = "osascript -e '{0}'"
while True:
	i = random.randint(0, 2002)
	if(i%2 == 0):
		if len(quotes[i]) < 118:
			message = quotes[i]
			_notification = message
			print (len(_notification))
			print(_notification)
			base_cmd = 'display notification "{0}" with title "{1}"'.format(_notification, quotes[i+1])
			cmd = apple_cmd.format(base_cmd)
			subprocess.Popen([cmd], shell=True)
			time.sleep(notification_delay)
		else:
			time.sleep(check_delay)
	else:
		continue