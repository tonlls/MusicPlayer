from MusicPlayerManager import Model, DataModel
import requests


class APIRest:
	API = {}

	def __init__(self):
		self.baseurl = None
		self.user = None
		self.password = None

	def __init(self, baseurl, user, password):
		self.baseurl = baseurl
		self.user = user
		self.password = password

	@staticmethod
	def init(id, baseurl, user=None, password=None):
		if id in APIRest.API:
			return APIRest.API[id]
		else:
			return APIRest().__init(baseurl, user, password)

	def do_get_request(self, url, par):
		return requests.get(self.baseurl + url, params=par)

	def do_post_request(self, url, par):
		return requests.data(self.baseurl + url, data=par)

	@staticmethod
	def check_code(resp):
		return resp.status_code


class FileStorage(Model.FileStorage):
	def connect(self, host, user, password, db_name):
		self.server = APIRest(1, host, user, password)

	def add_song(self, song):
		self.server.do_post_request('/song_data')

	def get_song(self, id=None, name=None):
		self.server.do_post_request('/song_data')


class DataStorage(Model.DataStorage):
	def connect(self, host, user, password, db_name):
		self.server = APIRest(1, host, user, password)

	def add_song(self, song):
		pass

	def get_song(self, id=None, name=None):
		pass

	def add_album(self, album):
		pass

	def get_album(self, id=None, name=None):
		pass

	def add_artist(self, artist):
		pass

	def get_artist(self, id=None, name=None):
		pass
