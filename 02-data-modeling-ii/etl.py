import glob
import json
import os
from typing import List

from cassandra.cluster import Cluster


table_actors_drop = "DROP TABLE actors"
table_event_drop = "DROP TABLE events"
table_repos_drop = "DROP TABLE repositories"


table_actors_create = """
    CREATE TABLE IF NOT EXISTS actors (
        id VARCHAR,
        login text,
        display_login text,
        
        PRIMARY KEY(id)
    )
"""

table_event_create = """
    CREATE TABLE IF NOT EXISTS events
    (
        id VARCHAR,
        type text,
        actor_id text,
        public boolean,
        created_at timestamp,
        
        PRIMARY KEY (
            id,
            type
        )
    )
"""

table_repos_create = """
    CREATE TABLE IF NOT EXISTS repositories (
        id VARCHAR,
        name text,
        owner_id text,
        
        PRIMARY KEY(id),    
    )
"""

create_table_queries = [
    table_actors_create,
    table_event_create,
    table_repos_create,
]

drop_table_queries = [
    table_actors_drop,
    table_event_drop,
    table_repos_drop
]

def drop_tables(session):
    for query in drop_table_queries:
        try:
            rows = session.execute(query)
        except Exception as e:
            print(e)


def create_tables(session):
    for query in create_table_queries:
        # print(query)
        try:
            session.execute(query)
        except Exception as e:
            print(e)


def get_files(filepath: str) -> List[str]:
    """
    Description: This function is responsible for listing the files in a directory
    """

    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, "*.json"))
        for f in files:
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print(f"{num_files} files found in {filepath}")

    return all_files


def process(session, filepath):
    # Get list of files from filepath
    all_files = get_files(filepath)

    for datafile in all_files:
        with open(datafile, "r") as f:
            data = json.loads(f.read())
            for each in data:
                # Print some sample data
                print(each["id"], each["type"], each["actor"]["login"])
                
                # insert data to database
                insert_data(session, each)
                
                

def insert_data(session, each):
    actor_id = str(each["actor"]["id"])
    insert_statement = f"""
                    INSERT INTO actors (
                        id,
                        login,
                        display_login
                    ) VALUES (
                        '{actor_id}', 
                        '{each["actor"]["login"]}',
                        '{each["actor"]["display_login"]}'
                    )
                """
    session.execute(insert_statement)
    
    event_id = str(each["id"])
    insert_statement = f"""
                    INSERT INTO events (
                        id,
                        type,
                        actor_id,
                        created_at
                    ) VALUES (
                        '{event_id}', 
                        '{each["type"]}', 
                        '{each["actor"]["id"]}',
                        '{each["created_at"]}'
                    )
                """
    session.execute(insert_statement)
    
    repo_id = each["repo"]["id"]
    insert_statement = f"""
                    INSERT INTO repositories (
                        id,
                        name,
                        owner_id
                    ) VALUES (
                        '{repo_id}', 
                        '{each["repo"]["name"]}', 
                        '{each["actor"]["id"]}'
                    )
                """
    session.execute(insert_statement)


def insert_sample_data(session):
    query = f"""
    INSERT INTO events (id, type, public) VALUES ('23487929637', 'IssueCommentEvent', true)
    """
    session.execute(query)


def main():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    # Create keyspace
    try:
        session.execute(
            """
            CREATE KEYSPACE IF NOT EXISTS github_events
            WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
            """
        )
    except Exception as e:
        print(e)

    # Set keyspace
    try:
        session.set_keyspace("github_events")
    except Exception as e:
        print(e)

    drop_tables(session)
    create_tables(session)

    process(session, filepath="../data")
    # insert_data(session)

    # Select data in Cassandra and print them to stdout
    query = """
    SELECT * from events WHERE id = '23487929496' AND type = 'DeleteEvent'
    """
    try:
        rows = session.execute(query)
    except Exception as e:
        print(e)

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()