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
    songplay_id serial primary key,
    start_time timestamp without time zone,
    user_id int not null,
    level varchar not null,
    song_id varchar,
    song_title varchar not null,
    artist_id varchar,
    artist_name varchar not null,
    session_id int not null,
    location varchar not null,
    user_agent varchar not null,
    stream_duration decimal not null
);

create table users
(
    user_id int not null primary key,
    first_name varchar not null,
    last_name varchar not null,
    gender varchar not null,
    level varchar not null
);

create table songs
(
    song_id varchar not null primary key,
    title varchar not null,
    artist_id varchar not null,
    year int not null,
    duration decimal not null
);


create table artists
(
    artist_id varchar not null primary key,
    name varchar not null,
    location varchar not null,
    latitude decimal not null,
    longitude decimal not null
);

create table time
(
    start_time timestamp without time zone not null primary key,
    hour int not null,
    day int not null,
    week int not null,
    month int not null,
    year int not null,
    weekday bool not null
);