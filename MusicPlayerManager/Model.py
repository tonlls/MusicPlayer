import importlib
import abc
from abc import ABC


class StorageError(Exception):
	"""Base class for other exceptions"""

	class FileStorageError:
		pass

	class DataStorageError:
		pass


class StorageManager:
	DB_NAME = 'MusicPlayer'

	def __init__(self, module, data_class='DataStorage', file_class='FileStorage'):
		self.module = importlib.import_module(module)
		self.file_class = getattr(self.module, file_class)
		self.data_class = getattr(self.module, data_class)
		self.file_storage = self.file_class()
		self.data_storage = self.data_class()

	def connect(self, host, user, password, db_name=DB_NAME):
		self.file_storage.connect(host, user, password, db_name)
		self.data_storage.connect(host, user, password, db_name)

	def add_song(self, song):
		id = self.data_storage.add_song(song)
		self.file_storage.add_song(song)

	def get_song(self,id=None,name=None):
		song = self.data_storage.get_song(id,name)
		song = self.file_storage.get_song(id,name)


class Storage:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def connect(self, host, user, password, db_name):
		pass

	@abc.abstractmethod
	def add_song(self, song):
		pass

	@abc.abstractmethod
	def get_song(self, id=None, name=None):
		pass


class FileStorage(Storage, ABC):
	__metaclass__ = abc.ABCMeta


class DataStorage(Storage, ABC):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def add_album(self, album):
		pass

	@abc.abstractmethod
	def get_album(self, id=None, name=None):
		pass

	@abc.abstractmethod
	def get_album_id(self, name):
		pass

	@abc.abstractmethod
	def add_artist(self, artist):
		pass

	@abc.abstractmethod
	def get_artist(self, id=None, name=None):
		pass

	@abc.abstractmethod
	def get_artist_id(self, name):
		pass
