from MusicPlayerManager import Model, DataModel
import requests


class APIRest:
	def __init__(self, baseurl, user=None, password=None):
		self.baseurl = baseurl
		self.user = user
		self.password = password

	def do_get_request(self, url, par):
		return requests.get(self.baseurl + url, params=par)

	def do_post_request(self, url, par):
		return requests.data(self.baseurl + url, data=par)

	@staticmethod
	def check_code(resp):
		return resp.status_code


class FileStorage(Model.FileStorage):
	def connect(self, host, user, password, db_name):
		self.server=APIRest(host,user,password)

	def add_song(self, song):
		pass

	def get_song(self, id=None, name=None):
		pass


class DataStorage(Model.DataStorage):
	def connect(self, host, user, password, db_name):
		self.server=APIRest(host,user,password)

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
