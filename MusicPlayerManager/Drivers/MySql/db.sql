CREATE DATABASE MusicPlayer;
USE MusicPlayer;

CREATE TABLE artist(
	id INT PRIMARY KEY,
	name VARCHAR(50) NOT NULL
);

CREATE TABLE album(
	id INT PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	artist_id INT,

	FOREIGN KEY (artist_id) REFERENCES artist(id)
);

CREATE TABLE song(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	data BLOB,
	artist_id INT,
	album_id INT,

	FOREIGN KEY (artist_id) REFERENCES artist(id),
	FOREIGN KEY (album_id) REFERENCES album(id)
);
