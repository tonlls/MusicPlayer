from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
from kivy.uix.widget import Widget

from MusicPlayerManager import DataModel

Builder.load_string('''
<SongListItem>:
	on_release:app.song_press(self)
<SongList>:
	viewclass: 'SongListItem'
	scroll_type: ['bars', 'content']
	scroll_wheel_distance: dp(114)
	bar_width: dp(10)
	RecycleBoxLayout:	
		default_size: None, dp(56)
		default_size_hint: 1, None
		size_hint_y: None
		height: self.minimum_height
		orientation: 'vertical'
		spacing: dp(2)
<PlayBar>:
	width:dp(20)
	height:dp(20)
	BoxLayout:
		orientation: 'horizontal'
		canvas.before:
			Color:
				rgba: 153/255.0, 0, 0, 1
			Rectangle:
				# self here refers to the widget i.e BoxLayout
				pos: self.pos
				size: self.size
		Label:
			id:tl
		Button:
			text: '<'
			on_release: app.past()
		Button:
			text:'||'
			on_release: app.pause()
		Button:
			text:'>'
			on_release: app.next()
		
''')

class PlayBar(Widget):
	song=ObjectProperty(None)

	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.bind(song=self._on_song_change)
	def get_name(self):
		if self.song is not None:
			return self.song.name
		else:
			return ''
	def _on_song_change(self,instance,value):
		self.ids['tl'].text=self.song.name

class SongListItem(Button):
	song = ObjectProperty()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# print(kwargs.get('my_string'))
		# Clock.schedule_once(self.finish_init, 0)
		self.bind(song=self._on_song_change)

	# it delays the end of the initialization to the next frame, once the widget are already created
	# and the properties properly initialized
	def _on_song_change(self, instance, value):
		self.text = self.song.name


class SongList(RecycleView):
	name_filter = StringProperty('')

	def __init__(self, **kwargs):
		super(SongList, self).__init__(**kwargs)
		songs = [{'song': DataModel.Song(str(x))} for x in range(20)]
		self.data = songs
		self.bind(name_filter=self._on_name_filter_change)

	def _on_name_filter_change(self, instance, value):
		pass

	def add_songs(self, d):
		self.data = [{'song': s} for s in d]
