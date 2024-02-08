from typing import NewType

import psycopg2


PostgresCursor = NewType("PostgresCursor", psycopg2.extensions.cursor)
PostgresConn = NewType("PostgresConn", psycopg2.extensions.connection)

table_drop_events = "DROP TABLE IF EXISTS events CASCADE"
table_drop_actors = "DROP TABLE IF EXISTS actors CASCADE"
table_drop_repos = "DROP TABLE IF EXISTS repos CASCADE"
table_drop_comments = "DROP TABLE IF EXISTS comments CASCADE"
table_drop_commits = "DROP TABLE IF EXISTS commits CASCADE"
table_drop_pull_requests = "DROP TABLE IF EXISTS pull_requests CASCADE"
table_drop_pull_request_reviews = "DROP TABLE IF EXISTS pull_request_reviews CASCADE"

table_create_actors = """
    CREATE TABLE IF NOT EXISTS actors (
        id char(64),
        login text,
        display_login text,
        
        PRIMARY KEY(id)
    )
"""

table_create_events = """
    CREATE TABLE IF NOT EXISTS events (
        id char(64),
        type text,
        actor_id char(64),
        created_at timestamp,
        
        PRIMARY KEY(id),
        CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors(id)
    )
"""

table_create_repos = """
    CREATE TABLE IF NOT EXISTS repos (
        id char(64),
        name text,
        owner_id char(64),
        PRIMARY KEY(id),
        CONSTRAINT fk_owner FOREIGN KEY(owner_id) REFERENCES actors(id)
        
    )
"""

table_create_comments = """
    CREATE TABLE IF NOT EXISTS comments (
        id char(64),
        repo_id char(64),
        user_id char(64),
        comments int,
        total_count int,
        liked int,
        unliked int,
        laugh int,
        hooray int,
        confused int,
        heart int,
        rocket int,
        eyes int,
        created_at timestamp,
        
        
        PRIMARY KEY(id),
        CONSTRAINT fk_repo_comments FOREIGN KEY(repo_id) REFERENCES repos(id),
        CONSTRAINT fk_user_comments FOREIGN KEY(user_id) REFERENCES actors(id)
    )
"""

table_create_commits = """
    CREATE TABLE IF NOT EXISTS commits (
        sha char(256),
        repo_id char(64),
        message text,
        size int,
        author_id char(64),
        
        PRIMARY KEY(sha),
        CONSTRAINT fk_repo_commits FOREIGN KEY(repo_id) REFERENCES repos(id),
        CONSTRAINT fk_author_commits FOREIGN KEY(author_id) REFERENCES actors(id)
        
    )
"""

table_create_pull_requests = """
    CREATE TABLE IF NOT EXISTS pull_requests (
        id char(64),
        repo_id char(64),
        actor_id char(64),
        body text,
        comments int,
        review_comments int,
        commits int,
        additions int,
        deletions int,
        changed_files int,
        created_at timestamp,
        
        PRIMARY KEY(id),
        CONSTRAINT fk_repo_pull_requests FOREIGN KEY(repo_id) REFERENCES repos(id),
        CONSTRAINT fk_actor_pull_requests FOREIGN KEY(actor_id) REFERENCES actors(id)
        
    )
"""

table_create_pull_request_reviews = """
    CREATE TABLE IF NOT EXISTS pull_request_reviews (
        id char(64),
        pull_request_id char(64),
        actor_id char(64),
        body text,
        comments int,
        state text,
        total_count int,
        liked int,
        unliked int,
        laugh int,
        hooray int,
        confused int,
        heart int,
        rocket int,
        eyes int,
        
        PRIMARY KEY(id),
        CONSTRAINT fk_actor_comments FOREIGN KEY(actor_id) REFERENCES actors(id),
        CONSTRAINT fk_pull_request_pull_request_reviews FOREIGN KEY(pull_request_id) REFERENCES pull_requests(id)
        
    )
"""

create_table_queries = [
    table_create_actors,
    table_create_events,
    table_create_repos,
    table_create_comments,
    table_create_commits,
    table_create_pull_requests,
    table_create_pull_request_reviews,
    
]
drop_table_queries = [
    table_drop_events,
    table_drop_actors,
    table_drop_repos,
    table_drop_comments,
    table_drop_commits,
    table_drop_pull_requests,
    table_drop_pull_request_reviews,
]


def drop_tables(cur: PostgresCursor, conn: PostgresConn) -> None:
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur: PostgresCursor, conn: PostgresConn) -> None:
    """
    Creates each table using the queries in `create_table_queries` list.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database.
    - Establishes connection with the sparkify database and gets
    cursor to it.
    - Drops all the tables.
    - Creates all tables needed.
    - Finally, closes the connection.
    """
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=postgres"
    )
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()