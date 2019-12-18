class Playlist:
	def __init__(self, songs=[]):
		if all(isinstance(x, Song) for x in songs):
			self.songs = songs
		else:
			raise Exception('songs must be from type Song')

	def add(self, song):
		if isinstance(song, Song):
			self.songs.append(song)
		else:
			raise Exception('you can not add a non Song type object')


class Song:
	def __init__(self, name, id=None, data='', artist=None, album=None, path=None, check=True):
		self.id = id
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
		return {'name': self.name, 'data': self.data, 'artist_id': self.artist_id, 'artist_id': self.artist_id};

	# return {'id':self.id,'name':self.name,'data':self.data,'artist_id':self.artist_id,'artist_id':self.artist_id};
	@staticmethod
	def from_dict(dict):
		return Song(dict['id'], dict['name'], dict['data'])

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
