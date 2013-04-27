import requests

class ACDataClient(object):
	def __init__(self):
		return

	def get_parks(self):
		url = "https://data.acgov.org/id/k9se-aps6.json?"
		response = requests.get(url)
		return response.json()

	def get_poi(self):
		url = "https://data.acgov.org/id/xzcz-7uep.json?"
		response = requests.get(url)
		return response.json()

	def get_crime_reports(self):
		url = "https://data.acgov.org/id/8khs-56kk.json?"
		response = requests.get(url)
		return response.json()

	def get_shelters(self):
		url = "https://data.acgov.org/id/wu33-vg7m.json?"
		response = requests.get(url)
		return requests.get()
