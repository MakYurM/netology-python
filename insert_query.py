import sqlalchemy

db = 'postgresql://frkl:LoL2zx45YuK@localhost:5432/demodb'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

connection.execute("INSERT INTO artist(artist_name) VALUES ('Сплин')")
connection.execute("INSERT INTO artist(artist_name) VALUES ('КиШ')")
connection.execute("INSERT INTO artist(artist_name) VALUES ('Pink Floyd')")
connection.execute("INSERT INTO artist(artist_name) VALUES ('Нейромонах Феофан')")
connection.execute("INSERT INTO artist(artist_name) VALUES ('Mujuice')")
connection.execute("INSERT INTO artist(artist_name) VALUES ('Биртман')")
connection.execute("INSERT INTO artist(artist_name) VALUES ('Вася Обломов')")
connection.execute("INSERT INTO artist(artist_name) VALUES ('The Prodigy')")

connection.execute("INSERT INTO genre(genre_name) VALUES ('Rock')")
connection.execute("INSERT INTO genre(genre_name) VALUES ('Punk')")
connection.execute("INSERT INTO genre(genre_name) VALUES ('D&B')")
connection.execute("INSERT INTO genre(genre_name) VALUES ('Electronic music')")
connection.execute("INSERT INTO genre(genre_name) VALUES ('Indi')")
connection.execute("INSERT INTO genre(genre_name) VALUES ('Rave')")

connection.execute("INSERT INTO artist_genre(genre_id, artist_id) VALUES (1, 2)")
connection.execute("INSERT INTO artist_genre(genre_id, artist_id) VALUES (2, 3)")
connection.execute("INSERT INTO artist_genre(genre_id, artist_id) VALUES (1, 7)")
connection.execute("INSERT INTO artist_genre(genre_id, artist_id) VALUES (3, 15)")
connection.execute("INSERT INTO artist_genre(genre_id, artist_id) VALUES (4, 16)")
connection.execute("INSERT INTO artist_genre(genre_id, artist_id) VALUES (5, 17)")
connection.execute("INSERT INTO artist_genre(genre_id, artist_id) VALUES (5, 18)")
connection.execute("INSERT INTO artist_genre(genre_id, artist_id) VALUES (6, 19)")

connection.execute("INSERT INTO albums(album_name, release_date) VALUES ('Ели мясо мужики', 1999)")
connection.execute("INSERT INTO albums(album_name, release_date) VALUES ('Альтависта', 1999)")
connection.execute("INSERT INTO albums(album_name, release_date) VALUES ('The Wall', 1979)")
connection.execute("INSERT INTO albums(album_name, release_date) VALUES ('В душе драм, в сердце светлая Русь', 2015)")
connection.execute("INSERT INTO albums(album_name, release_date) VALUES ('Melancholium', 2021)")
connection.execute("INSERT INTO albums(album_name, release_date) VALUES ('Подбухну', 2019)")
connection.execute("INSERT INTO albums(album_name, release_date) VALUES ('Стабильность', 2012)")
connection.execute("INSERT INTO albums(album_name, release_date) VALUES ('Invaders Must Die', 2009)")

connection.execute("INSERT INTO artist_album(artist_id, albums_id) VALUES (2, 3)")
connection.execute("INSERT INTO artist_album(artist_id, albums_id) VALUES (3, 2)")
connection.execute("INSERT INTO artist_album(artist_id, albums_id) VALUES (7, 4)")
connection.execute("INSERT INTO artist_album(artist_id, albums_id) VALUES (15, 5)")
connection.execute("INSERT INTO artist_album(artist_id, albums_id) VALUES (16, 6)")
connection.execute("INSERT INTO artist_album(artist_id, albums_id) VALUES (17, 7)")
connection.execute("INSERT INTO artist_album(artist_id, albums_id) VALUES (18, 8)")
connection.execute("INSERT INTO artist_album(artist_id, albums_id) VALUES (19, 9)")

connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Ели мясо мужики', 157, 2)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Лесник', 193, 2)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Прыгну со скалы', 196, 2)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Камнем по голове', 171, 2)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Альтависта', 374, 3)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Молоко и мёд', 287, 3)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Пил-курил', 	296, 3)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Терпсихора', 169, 3)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Mother', 332, 4)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Hey You', 281, 4)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Another Brick in the Wall (Part 1)', 181, 4)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Another Brick in the Wall (Part 2)', 240, 4)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Холодно в лесу', 135, 5)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Под драм легко', 164, 5)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Нейромонах Феофан', 127, 5)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Светлая Русь', 224, 5)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Zodiac', 212, 6)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Rehab', 185, 6)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Ласточки', 275, 6)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Напрасные Надежды', 196, 6)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Тони Старк',	207, 7)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Подбухну', 172, 7)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Анапа', 169, 7)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Котоход', 165, 7)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Корпоративная', 176, 8)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Свадьба', 174, 8)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Поганенький у нас народ', 243, 8)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Рэп-молебен', 210, 8)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Invaders Must Die', 295, 9)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Omen', 216, 9)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Thunder', 248, 9)")
connection.execute("INSERT INTO tracks(track_name, track_time, albums_id) VALUES ('Colours', 207, 9)")

connection.execute("INSERT INTO collection_album(collection_name, collection_date) VALUES ('Сборник #1', 2014)")
connection.execute("INSERT INTO collection_album(collection_name, collection_date) VALUES ('Сборник #2', 2015)")
connection.execute("INSERT INTO collection_album(collection_name, collection_date) VALUES ('Сборник #3', 2016)")
connection.execute("INSERT INTO collection_album(collection_name, collection_date) VALUES ('Сборник #4', 2017)")
connection.execute("INSERT INTO collection_album(collection_name, collection_date) VALUES ('Сборник #5', 2018)")
connection.execute("INSERT INTO collection_album(collection_name, collection_date) VALUES ('Сборник #6', 2019)")
connection.execute("INSERT INTO collection_album(collection_name, collection_date) VALUES ('Сборник #7', 2020)")
connection.execute("INSERT INTO collection_album(collection_name, collection_date) VALUES ('Сборник #8', 2021)")

connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (1, 1)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (5, 1)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (9, 1)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (2, 2)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (13, 2)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (7, 3)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (3, 3)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (10, 4)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (14, 4)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (15, 5)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (11, 5)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (24, 6)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (16, 6)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (23, 7)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (8, 7)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (17, 8)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (18, 8)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (21, 8)")
connection.execute("INSERT INTO tracks_collection_album(tracks_id, collection_album_id) VALUES (22, 8)")