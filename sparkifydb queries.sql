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

select *
from songplays sp
left join time t on sp.start_time = t.start_time
where t.start_time is null

select *
from songplays sp
left join users u on sp.user_id = u.user_id
where u.user_id is null

select concat(u.first_name, ' ', u.last_name), count(sp.start_time)
from songplays sp
left join users u on sp.user_id = u.user_id
group by concat(u.first_name, ' ', u.last_name)
order by 2 desc
limit 5

select u.first_name, sum(sp.stream_duration)
from songplays sp
left join users u on sp.user_id = u.user_id
group by u.first_name
order by 2 desc


select t.hour, count(sp.start_time) as stream_count
from songplays sp
left join time t on sp.start_time = t.start_time
group by t.hour
order by 2 desc
limit 5

select sp.location, t.hour, count(sp.start_time)
from songplays sp
left join time t on sp.start_time = t.start_time
group by sp.location, t.hour
order by 3 desc

select
sp.location,
sp.artist_name, count(sp.start_time)
from songplays sp
group by
sp.location,
    sp.artist_name
order by 3 desc

select
SPLIT_PART(sp.location, ',', 2) as state,
count(sp.start_time) as stream_count,
sum(sp.stream_duration) as stream_duration
from songplays sp
group by
SPLIT_PART(sp.location, ',', 2)
order by 2 desc, 3 desc
limit 5


with cte_artists_by_state as
    (
        select
            SPLIT_PART(sp.location, ',', 2) as state,
            sp.artist_name,
            row_number()
                over (partition by SPLIT_PART(sp.location, ',', 2)
                    order by
                        count(sp.start_time) desc,
                        sum(sp.stream_duration) desc
                    ) as rank,
        count(sp.start_time) as stream_count,
        sum(sp.stream_duration) as stream_duration
        from songplays sp
        group by SPLIT_PART(sp.location, ',', 2),
        sp.artist_name
    )
select
state, artist_name, stream_count, stream_duration
from cte_artists_by_state
where rank = 1
order by stream_count desc

