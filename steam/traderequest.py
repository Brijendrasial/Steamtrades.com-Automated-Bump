import lib.requests

class TradeRequest(object):
	
	def __init__(self, link, cookies):
		self.link = link
		self.cookies = cookies

	def get_request(self):
		self.site = lib.requests.get(self.link, cookies=self.cookies)
		return self.site.content
