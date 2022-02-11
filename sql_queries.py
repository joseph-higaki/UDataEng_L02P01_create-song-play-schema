# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

songplay_table_create = ("""
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
""")

user_table_create = ("""
create table users
(
    user_id int not null primary key,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar
);
""")

song_table_create = ("""
create table songs
(
    song_id varchar not null primary key,
    title varchar,
    artist_id varchar,
    year int,
    duration decimal
);
""")

artist_table_create = ("""
create table artists
(
    artist_id varchar not null primary key,
    name varchar,
    location varchar,
    latitude decimal,
    longitude decimal
);
""")

time_table_create = ("""
create table time
(
  start_time timestamp without time zone not null primary key,
  hour int,
  day int,
  week int,
  month int,
  year int,
  weekday bool
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
insert into songplays 
(start_time,
user_id,
level,
song_id,
artist_id,
session_id,
location,
user_agent)
values
(%(start_time)s,
%(user_id)s,
%(level)s,
%(song_id)s,
%(artist_id)s,
%(session_id)s,
%(location)s,
%(user_agent)s)
""")

user_table_insert = ("""
insert into users
(user_id, first_name, last_name, gender, level)
values 
(%(user_id)s, %(first_name)s, %(last_name)s, %(gender)s, %(level)s)
on conflict (user_id) do update
set 
  first_name = %(first_name)s,
  last_name = %(last_name)s,
  gender = %(gender)s, 
  level = %(level)s
""")

song_table_insert = ("""
insert into songs
(song_id, title, artist_id, year, duration)
values 
(%(song_id)s, %(title)s, %(artist_id)s, %(year)s, %(duration)s)
on conflict (song_id) do update 
set 
  title = %(title)s, 
  artist_id = %(artist_id)s, 
  year = %(year)s, 
  duration = %(duration)s
""")

artist_table_insert = ("""
insert into artists
(artist_id, name, location, latitude, longitude)
values 
(%(artist_id)s, %(name)s, %(location)s, %(latitude)s, %(longitude)s)
on conflict (artist_id) do update 
set 
  name = %(name)s, 
  location = %(location)s, 
  latitude = %(latitude)s, 
  longitude = %(longitude)s
""")


time_table_insert = ("""
insert into time
(start_time, hour, day, week, month, year, weekday)
values 
(%(start_time)s, %(hour)s, %(day)s, %(week)s, %(month)s, %(year)s, %(weekday)s)
on conflict (start_time) do update 
set 
  hour = %(hour)s, 
  day = %(day)s, 
  week = %(week)s, 
  month = %(month)s, 
  year = %(year)s, 
  weekday = %(weekday)s
""")

# FIND SONGS

song_select = ("""
select s.song_id, s.artist_id
from songs s
join artists a on s.artist_id = a.artist_id
where s.title = %(song_title)s
and a.name = %(artist_name)s
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]