import abc

from kivy import Logger
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from MusicPlayerGUI import Widgets
from MusicPlayerManager import Model


class _Screen(object):


	def menu_press(self, instance, value):
		pass


kv = '''
<TestScreen>:
	SongList:
		id: sl
	PlayBar:
		id: pb
'''
Builder.load_string(kv)


class TestScreen(_Screen, BoxLayout):
	DB = None

	def __init__(self, **kwargs):
		super(TestScreen, self).__init__(**kwargs)
		TestScreen.DB = Model.StorageManager('MusicPlayerManager.Drivers.MySql.MySqlStorage')
		TestScreen.DB.connect('localhost', 'ton', 'ton')
		self.ids['sl'].add_songs(TestScreen.DB.data_storage.get_songs())
		# Logger.info('title: This is a info message.')


