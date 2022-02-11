select s.song_id, s.artist_id
from songs s
join artists a on s.artist_id = a.artist_id
where s.title = 'I Didn''t Mean To'
and a.name = 'Casual'


select s.song_id, s.artist_id
from songs s
-- left join artists a on s.artist_id = a.artist_id
where s.title = 'You Gotta Be'

select  * from songs
where title like '%otta%'

select * from songplays
where song_id is not null
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND
    schemaname != 'information_schema'

-- truncate table songs

select * from artists


select * from time