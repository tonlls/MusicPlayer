from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty

from MusicPlayerGUI.Screens import TestScreen
from MusicPlayerManager import DataModel


class _App(App):
	index=NumericProperty(0)
	queue=ObjectProperty(DataModel.Playlist())
	def next(self):
		self.index+=1
	def song_press(self,instance):
		self.s.ids['pb'].song=instance.song
	def build(self):
		self.s=TestScreen()

		return self.s
