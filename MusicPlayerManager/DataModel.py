class Song:
	def __init__(self, name, data='', artist=None, album=None, path=None, check=True):
		self.id = None
		self.name = name
		self.path = path
		self.data = data
		self.artist = artist
		if artist is None:
			self.artist_id = None
		else:
			self.artist_id = self.artist.id
		self.album = album
		if album is None:
			self.album_id = None
		else:
			self.album_id = self.album.id

		if check:
			self.check()

	def to_dict(self):
		return self.__dict__;

	def check(self):
		if self.name is None or type(self.name) is not str or len(self.name) < 1:
			raise Exception("name propperty isn't correct")

	def load_data(self):
		if self.data is not None:
			with open(self.path) as file:
				self.data = file.read()

	def copy(self):
		return Song(self.name, self.path, self.data, self.artist, self.album)


class Artist:
	def __init__(self, name):
		self.name = name

	def to_dict(self):
		return self.__dict__;


class Album:
	def __init__(self, name, artist=None):
		self.name = name
		self.artist = artist
		if self.artist is not None:
			self.artist_id = artist.id
		else:
			self.artist_id = None

	def to_dict(self):
		return self.__dict__;
