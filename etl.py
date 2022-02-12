import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import db_connection_config as config 

def process_song_file(cur, filepath):
    """processes (upserts) song and artist information

    Args:
        cur (psycopg2.cursor class): PostgreSQL cursor that allows executing SQL commands within the ETL connection and execution context.
        filepath ([string]): local file URI that contains metadata from songs and artists in JSON format
    """    
    # open song file
    df = pd.read_json(filepath, lines=True)

    # creating a dictionary to easily send named params to the sql query
    song_data_dict = df[["song_id", "title", "artist_id", "year", "duration"]].to_dict('records')
    # insert song record(s), iterating over the JSON read result: in case at the json file there is more than one 
    list(map(lambda song_data: cur.execute(song_table_insert, song_data), song_data_dict))
        
    # renaming columns to match named params from the sql query
    artist_column_rename = {"artist_name": "name", "artist_location": "location", "artist_latitude": "latitude", "artist_longitude":"longitude"}    
    artist_data_dict = df[["artist_id", "artist_name", "artist_location", "artist_latitude", "artist_longitude"]].rename(columns = artist_column_rename).to_dict('records')
    # insert artist record
    list(map(lambda artist_data: cur.execute(artist_table_insert, artist_data), artist_data_dict))
    


def process_log_file(cur, filepath):
    """processes log file information into 
    
        - upserting users
        - inserting time table
        - inserting songplays

    Args:
        cur (psycopg2.cursor class): PostgreSQL cursor that allows executing SQL commands within the ETL connection and execution context.
        filepath ([string]): local file URI that contains events from the streaming platform 
    """    
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df.page == "NextSong"]

    # convert timestamp column to datetime
    df['start_time'] = pd.to_datetime(df['ts'], unit='ms')
    # create calendar table fields
    df['hour'] = df['start_time'].dt.hour
    df['day'] = df['start_time'].dt.day
    df['week'] = df['start_time'].dt.isocalendar().week
    df['month'] = df['start_time'].dt.month
    df['year'] = df['start_time'].dt.year
    df['weekday'] = df['start_time'].dt.dayofweek > 4 
    
    # select only relevant columns for time calendar table 
    # dropping duplicates 
    time_df = df[["start_time", "hour", "day", "week", "month","year", "weekday"]].drop_duplicates()    
    # insert time records
    list(map(lambda time_data: cur.execute(time_table_insert, time_data), time_df.to_dict("records")))

    
    # columns rename to match sql named params
    user_column_rename = {"userId": "user_id", "firstName": "first_name", "lastName": "last_name"}
    # load user table and remame columns
    user_df = df[["userId", "firstName","lastName", "gender", "level"]].rename(columns = user_column_rename)
    # insert user records
    list(map(lambda user_data: cur.execute(user_table_insert, user_data), user_df.to_dict("records")))

    # insert songplay records
    #select which columns to use
    songplay_selected_columns = ["length", "start_time", "userId", "level", "song", "artist", "sessionId", "location", "userAgent"]
    #rename columns so it matches the sql params
    songplay_column_rename = {"userId":"user_id", "song": "song_title", "artist": "artist_name",  "sessionId": "session_id", "userAgent":"user_agent", "length":"stream_duration"}

    #selecting and renaming columns for the songplay data frame
    songplay_df = df[songplay_selected_columns].rename(columns = songplay_column_rename)

    # creating artist and song id columns
    songplay_df["artist_id"] = None
    songplay_df["song_id"] = None

    for songplay in songplay_df.to_dict("records"):
        
        # get songid and artistid from song and artist tables
        # Here, I'm sending the entire songplay dictionary. 
        # But, since the song_select has named params,
        # it will only use the ones that match. 
        cur.execute(song_select, songplay)
        results = cur.fetchone()        
        if results:
            songplay["song_id"]= results[0]
            songplay["artist_id"] = results[1]

        # insert songplay record        
        cur.execute(songplay_table_insert, songplay)


def process_data(cur, conn, filepath, func):
    """[summary]

    Args:
        cur (psycopg2.cursor class): PostgreSQL cursor that allows executing SQL commands
        conn (psycopg2.connection class): PostgreSQL database connection
        filepath ([type]): local folder URI that the function func is able to process
        func ([type]): processing function that recieves a cursor and a filepath of a file
    """    
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect(config.Config().connection_string(dbname="sparkifydb"))
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()