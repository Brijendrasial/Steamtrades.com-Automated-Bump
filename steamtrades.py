import lib.requests
import time
from time import gmtime, strftime

def enter_sleep_time():
	global sleep_time
	t = raw_input()

	if t is '':
		sleep_time = 2100
		print('\nDefault time 35 min is set\n')

	
	else:
		try:
			t = int(t)
			if t < 2100:
				print '\nTime can not be less than 35 min\nEnter again\n'
				enter_sleep_time()
			else:
				sleep_time = t
		except ValueError, e:
			print '\n Enter integer value\n'
			enter_sleep_time()



print '\nEnter the time for sleep in seconds (default 35 min)\n'
print'\nEg 40 min then enter 2400\n'
enter_sleep_time()



no_of_bumps = 0
link_data = [line.strip() for line in open('links_steam_trades.txt')]
cookie_data = [line.strip() for line in open('cookie_steam_trades.txt')]
cookies = {cookie_data[0]:cookie_data[1]}
payload = {'form_key':'3b4378d8c868c9748090045ea6d66f42', 
'do':'bump'}

def bump():

	for link in link_data:
	      r = lib.requests.post(link, data=payload, cookies=cookies)
	      bumped_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	      message = '\nBumped %s %s times\n at %s'%(link,no_of_bumps, bumped_time) 
	      print message
	      f = open('output.txt', 'a')
	      
	      f.write(message)
	      f.close()
	print '\n Total bumped %s time\n'%no_of_bumps

while True:
	print '\nBump Started.....\n'
	no_of_bumps += 1
	bump()
	min_time = sleep_time/60
	print '\nSleeping for %s min\n'%min_time
	time.sleep(sleep_time)