create table if not exists genre (
    id serial primary key,
    genre_name varchar(25) not null unique
);

create table if not exists artist (
	id serial primary key,
	artist_name varchar(40) not null unique
);

create table if not exists albums (
    id serial primary key,
    album_name varchar(60) not null,
    release_date integer
);

create table if not exists collection_album (
    id serial primary key,
    collection_name varchar(100) not null,
    collection_date integer
);

create table if not exists tracks (
    id serial primary key,
    track_name varchar(120) not null,
    track_time integer,
    albums_id integer references Albums(id)
);

create table if not exists artist_genre (
    genre_id integer references genre(id),
    artist_id integer references artist(id),
    constraint artist_genre_table primary key (genre_id, artist_id)
);

create table if not exists artist_album (
    artist_id integer references artist(id),
    albums_id integer references albums(id),
    constraint artist_albums_table primary key (artist_id, albums_id)
);

create table if not exists tracks_collection_album (
    tracks_id integer references tracks(id),
    collection_album_id integer references collection_album(id),
    constraint tracks_collection_album_table primary key (tracks_id, collection_album_id)
);


