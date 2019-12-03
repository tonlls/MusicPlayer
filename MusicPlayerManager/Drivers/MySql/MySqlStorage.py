import os
from MusicPlayerManager import Model, DataModel
import mysql.connector


class MySql:
	__MYDB = None
	RESET_BD = False

	def __init__(self, host, user, password, db_name, connect=True):
		self.host = host
		self.user = user
		self.password = password
		self.db_name = db_name
		if connect:
			self._connect()

	@staticmethod
	def _commit():
		MySql.__MYDB.commit()

	@staticmethod
	def _rollback():
		MySql.__MYDB.rollback()

	@staticmethod
	def _get_cursor():
		return MySql.__MYDB.cursor()

	@staticmethod
	def _check_db():
		if MySql.__MYDB is None:
			raise Model.StorageError('DB not connected')

	@staticmethod
	def _run_count(sql):
		MySql._check_db()
		cursor = MySql._get_cursor()
		cursor.execute(sql)
		return cursor.fetchone()[0]

	@staticmethod
	def _run(sql):
		MySql._check_db()
		cursor = MySql._get_cursor()
		cursor.execute(sql)

	@staticmethod
	def _run_select(sql):
		MySql._check_db()
		cursor = MySql._get_cursor()
		cursor.execute(sql)
		return cursor.fetchall()

	@staticmethod
	def _run_insert(sql, val):
		cursor = MySql._get_cursor()
		cursor.execute(sql, val)
		MySql._commit()
		return cursor.lastrowid

	@staticmethod
	def _run_delete(sql):
		cursor = MySql._get_cursor()
		cursor.execute(sql)
		MySql.commit()

	@staticmethod
	def _run_script(path):
		cursor = MySql._get_cursor()
		with open(path) as file:
			sql = file.read()
		sql = sql.split(';')
		for command in sql:
			try:
				if command.strip() != '':
					cursor.execute(command)
			except Exception as e:
				MySql._rollback()
				raise e
		MySql._commit()

	def _connect(self):
		if MySql.__MYDB is None:
			MySql.__MYDB = mysql.connector.connect(
				host=self.host,
				user=self.user,
				passwd=self.password
			)
			if MySql.RESET_BD:
				MySql._run_script(os.path.join(os.path.dirname(__file__), 'del_db.sql'))
			sql = 'SELECT COUNT(SCHEMA_NAME) FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = \'' + self.db_name + '\''
			res = MySql._run_count(sql)
			if res == 0:
				MySql._run_script(os.path.join(os.path.dirname(__file__), 'db.sql'))
			else:
				MySql._run('USE ' + self.db_name + ';')


class DataStorage(Model.DataStorage):

	def connect(self, host, user, password, db_name):
		MySql(host, user, password, db_name)

	def add_song(self, song):
		sql = 'INSERT INTO song(name,artist_id,album_id) VALUES(%s,%s,%s)'
		val = (song.name, song.artist_id, song.album_id)
		return MySql._run_insert(sql, val)

	def get_song(self, id=None, name=None):
		if id is None and name is None:
			raise Exception()
		elif id is not None:
			sql = 'SELECT id,name,data,artist_id,album_id FROM song WHERE id=' + str(id) + ';'
			res = MySql._run_select(sql)
			song = DataModel.Song(res[1], res[2], self.get_artist(res[3]), self.get_album(res[4]))
			song.id = res[0]
			return song

	def add_album(self, album):
		pass

	def get_album(self, id=None, name=None):
		return None

	def get_album_id(self, name):
		pass

	def add_artist(self, artist):
		pass

	def get_artist(self, id=None, name=None):
		return None

	def get_artist_id(self, name):
		pass


class FileStorage(Model.FileStorage):

	def connect(self, host, user, password, db_name):
		MySql(host, user, password, db_name)

	def add_song(self, song):
		pass

	def get_song(self, id=None, name=None):
		pass
