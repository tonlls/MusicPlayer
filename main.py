def test():
	from MusicPlayerManager import Model,DataModel
	x=Model.StorageManager('MusicPlayerManager.Drivers.MySql.MySqlStorage')
	x.connect('localhost','ton','ton')
	t=x.data_storage.get_songs()
	print(t)
def Test():
	import MusicPlayerGUI
	from MusicPlayerGUI import test
	test._App().run()

Test()