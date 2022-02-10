DROP DATABASE IF EXISTS sparkifydb;

CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0;

SELECT session_user, current_database();
\c sparkifydb;


drop table if exists songplays;
drop table if exists users;
drop table if exists songs;
drop table if exists artists;
drop table if exists time;

create table songplays
(
    songplay_id int not null primary key,
    start_time date,
    user_id int,
    level varchar,
    song_id varchar,
    artist_id varchar,
    session_id int,
    location varchar,
    user_agent varchar
);

create table users
(
    user_id int not null primary key,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar
);

create table songs
(
    song_id varchar not null primary key,
    title varchar,
    artist_id varchar,
    year int,
    duration decimal
);


create table artists
(
    artist_id varchar not null primary key,
    name varchar,
    location varchar,
    latitude decimal,
    longitude decimal
);

create table time
(
    start_time date not null primary key,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday bool
);