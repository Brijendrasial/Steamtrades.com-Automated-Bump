from lib.bs4 import BeautifulSoup as bs

class TradeScrapper(object):
	
	def __init__(self, contents):
		self.soup = bs(contents)
		self.form = self.soup.find('form',id="bump_discussion")

	def get_payload(self):
		self.data = {}
		try:
			for input_values in self.form.findAll('input'):
				data = {input_values['name']:input_values['value']}
				self.data.update(data)

			return self.data

		except AttributeError, e:
			return None


