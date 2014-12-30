import lib.requests
import time
from time import gmtime, strftime
import os
from lib.scraper import TradeScrapper as ts
from lib.traderequest import TradeRequest as tr

path = os.path.dirname(__file__)
path+'data/sleep_time.txt'
no_of_bumps = 0
try:
	link_data = [line.strip() for line in open(path+'data/links_steam_trades.txt')]
except IOError, e:
	print ('\nCannot find links_steam_trades.txt file\n')
	exit()

try:
	cookie_data = [line.strip() for line in open(path+'data/cookie_steam_trades.txt')]
except IOError, e:
	print ('\nCannot find cookie_steam_trades.txt file\n')
	exit()

try:
	time_data = [line.strip() for line in open(path+'data/sleep_time.txt')]
	sleep_time = time_data
	print('\nSleep time is %s\n'%sleep_time)
except IOError, e:
	sleep_time = 2100
	print('\nSleep time is %s\n'%sleep_time)
	

cookies = {'PHPSESSID':cookie_data[0]}
def bump():
	for links in link_data:
		
		link = tr(links, cookies)
		link_contents = link.get_request()
		data = ts(link_contents)
		payload = data.get_payload()
		if payload == None:
			print('\nAUTHENTICATION FAILURE for link %s'%links)
			print '\nUpdate cookie\n'
		else:
			lib.requests.post(links, data=payload, cookies=cookies)
			bumped_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			message = '\nBumped %s %s times\n at %s'%(links,no_of_bumps, bumped_time) 
			print message
			f = open(path+'output/output.txt', 'a')
			
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