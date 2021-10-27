import sqlalchemy

db = 'postgresql://frkl:LoL2zx45YuK@localhost:5432/demodb'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

print('=== 1 ===')
album_date = connection.execute("SELECT album_name FROM albums WHERE release_date = 1999;").fetchall()
print(f'Альбомы вышедшие в 1999 году {album_date}')
album_date = connection.execute("SELECT album_name FROM albums WHERE release_date = 2019;").fetchall()
print(f'Альбомы вышедшие в 2019 году {album_date}')

print('=== 2 ===')
max_length_track = connection.execute("SELECT track_name FROM tracks WHERE track_time = (SELECT MAX(track_time) FROM tracks);").fetchall()
name_track = max_length_track[0][0]
track_sec = connection.execute("SELECT MAX(track_time) FROM tracks ;").fetchall()
b = track_sec[0][0]
print(f'Самый длинный трек: {name_track} - {b//60}:{b-((b//60)*60)}')

print('=== 3 ===')
tracks = connection.execute("SELECT track_name FROM tracks WHERE track_time >= 210;").fetchall()
track_list = []
for i in tracks:
    track_list.append(i[0])
print(f'Список треков, дпродолжительность которых не менее 3,5 минуты:\n {track_list}')

print('=== 4 ===')
collections = connection.execute("SELECT collection_name FROM collection_album WHERE collection_date BETWEEN 2018 AND 2020;").fetchall()
print(f'Сборники вышедшие в период с 2018 по 2020 год включительно: {collections}')

print('=== 5 ===')
artistname = connection.execute("SELECT artist_name FROM artist WHERE array_length(regexp_split_to_array(artist_name, '\s+'), 1) = 1;").fetchall()
print(f'Исполнители, чье имя состоит из 1 слова: {artistname}')

print('=== 6 ===')
tracks_with_word = connection.execute("SELECT track_name FROM tracks WHERE track_name LIKE '%%Wall%%';").fetchall()
print(f'Название треков, которые содержат слово - Wall: {tracks_with_word}')