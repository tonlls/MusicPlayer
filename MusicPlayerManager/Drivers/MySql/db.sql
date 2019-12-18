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
	data BLOB DEFAULT NULL,
	artist_id INT DEFAULT NULL,
	album_id INT DEFAULT NULL,

	FOREIGN KEY (artist_id) REFERENCES artist(id),
	FOREIGN KEY (album_id) REFERENCES album(id)
);

CREATE TABLE song_data(
    id INT PRIMARY KEY,
	song_id INT NOT NULL,
    data BLOB,

	FOREIGN KEY (song_id) REFERENCES song(id)
);

CREATE TABLE user(
	id INT PRIMARY KEY,
	username VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL
);

CREATE TABLE playlist(
	id INT PRIMARY KEY,
	user_id INT NOT NULL,
	creation_date DATE,

	FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE playlist_song(
	id INT PRIMARY KEY,
	playlist_id INT NOT NULL,
	song_id INT NOT NULL,
	position INT NOT NULL,
	add_date DATE,

	FOREIGN KEY (playlist_id) REFERENCES playlist(id),
	FOREIGN KEY (song_id) REFERENCES song(id)
)

INSERT INTO song(name) VALUES ('test song 1'),('what a song'),('are you kidding');