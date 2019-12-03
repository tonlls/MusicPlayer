from MusicPlayerManager import Model,DataModel
x=Model.StorageManager('Drivers.MySql.MySqlStorage')
x.connect('localhost','ton','ton')
# x.add_song(DataModel.Song('test'))
x.get_song(1)