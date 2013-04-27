import requests

class ACDataClient(object):
	def __init__(self, url):
		self.url = url

	def get_parks(self):
		url = "https://data.acgov.org/id/k9se-aps6.json?"
		response = requests.get(url)
		return response.json()

	def get_poi(self):
		url = "https://data.acgov.org/id/xzcz-7uep.json?"
		response = requests.get(url)
		return response.json()
