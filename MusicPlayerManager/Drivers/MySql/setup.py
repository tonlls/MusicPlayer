from setuptools import setup

setup(
	name='MySqlDriver',
	version='1.0',
	description='MusicPlayerManager driver for mysql',
	author='Ton Llucià Senserrich',
	author_email='m2tllucia@gmail.com',
	packages=['MySql'],
	install_requires=['mysql','os','MusicPlayerManager'],
)