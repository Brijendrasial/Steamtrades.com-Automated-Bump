import lib.requests
import time
from time import gmtime, strftime
import os
from steam.scraper import TradeScrapper as ts
from steam.traderequest import TradeRequest as tr
import random

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
	sleep_time_range = time_data[0]
	range1,range2 = sleep_time_range.split('-')
	print range1
	print range2
	range1 = int(range1)
	range2 = int(range2)
	print'\nTime range is %s - %s\n'%(range1,range2)

except IOError,e:
	range1 = 2100
	range2 = 2400
	print'\nTime range is %s - %s\n'%(range1,range2)
	

cookies = {'PHPSESSID':cookie_data[0]}

def timer(sleep_time):
	print sleep_time
	min_left = sleep_time/60
	min_sleep = min_left*60
	sec_left = sec_sleep = sleep_time%60
	min = 0
	while min != min_sleep:
		print 'wait for %s min and %s sec'%(min_left,sec_left)
		time.sleep(60)
		min = min+60
		print '%s == %s'%(min, sleep_time)
		min_left -= 1
	
	if sec_left > 0:
		sec = 0
		while sec != sec_sleep:
			print 'wait %s sec'%(sec_left)
			time.sleep(1)
			sec += 1 
			print '%s == %s'%(min, sleep_time)
			sec_left -= 1



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
	timer(random.randint(range1,range2))