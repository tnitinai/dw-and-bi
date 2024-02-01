from typing import NewType

import psycopg2


PostgresCursor = NewType("PostgresCursor", psycopg2.extensions.cursor)
PostgresConn = NewType("PostgresConn", psycopg2.extensions.connection)

table_drop_events = "DROP TABLE IF EXISTS events"
table_drop_actors = "DROP TABLE IF EXISTS actors"

table_create_actors = """
    CREATE TABLE IF NOT EXISTS actors (
        id int,
        login text,
        name text,
        email text,
        display_login text,
        qravatar_id text,
        url text,
        avatar_url text,
        html_url text,
        followers_url text,
        following_url text,
        gists_url text,
        starred_url text,
        subscription_url,
        organization_url,
        repos_url,
        events_url,
        received_events_id,
        type,
        site_admin bool,
        PRIMARY KEY(id)
    )
"""

table_create_events = """
    CREATE TABLE IF NOT EXISTS events (
        id text,
        type text,
        actor_id int,
        repo_id,
        repo_name,
        repo_url,
        PRIMARY KEY(id),
        CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors(id)
    )
"""

table_create_push = """
    CREATE TABLE IF NOT EXISTS pushes (
        id,
        event_id,
        size int,
        distinct_size int,
        ref,
        head,
        before,
        public bool,
        created_at datetime,
    )
"""

table_create_commits = """
    CREATE TABLE IF NOT EXISTS commits (
        sha,
        push_id,
        message,
        district,
        url,
        autor_id
    )
"""

table_create_issue_comment_events = """
    CREATE TABLE IF NOT EXISTS issue_comment_events (
        id,
        event_id,
        url,
        repository_url,
        labels_url,
        comments_url,
        events_url,
        html_url,
        node_id,
        number,
        title,
        user_id,
        state,
        locked bool,
        created_at,
        updated_at,
        closed_at,
        author_association,
        active_lock_reason,
        body,
        reaction_url,
        reaction_total_count,
        reaction_liked_count,
        reaction_disliked_count,
        reaction_laugh,
        reaction_hooray,
        reaction_confused,
        reaction_heart,
        reaction_rocket,
        reaction_eyes,
        timeline_url,
        preformed_via_github_app,
        state_reason,
        public,
        org_id
    )
"""

table_create_labels = """
    CREATE TABLE IF NOT EXISTS labels (
        id,
        issue_comment_event_id,
        node_id,
        url,
        name,
        color,
        default,
        description
        reaction_url,
        reaction_total_count,
        reaction_liked_count,
        reaction_disliked_count,
        reaction_laugh,
        reaction_hooray,
        reaction_confused,
        reaction_heart,
        reaction_rocket,
        reaction_eyes,
        preformed_via_github_app,
    )
"""

table_create_assignees = """
    CREATE TABLE IF NOT EXISTS assignees (
        id,
        issue_comment_event_id
    )
"""

table_create_milestones = """
    CREATE TABLE IF NOT EXISTS milestones (
        id,
        issue_comment_event_id,
        url,
        html_url,
        labels_url,
        node_id,
        number,
        title,
        description,
        creator_id,
        open_issues,
        state,
        created_at,
        updated_at,
        due_on,
        closed_at
    )
"""

table_create_comments = """
    CREATE TABLE IF NOT EXISTS comments (
        id,
        issue_comment_event_id,
        url,
        html_url,
        issue_url,
        node_url,
        user_id,
        created_at,
        updated_at,
        author_association,
        body,
        rea
    )
"""

create_table_queries = [
    table_create_actors,
    table_create_events,
]
drop_table_queries = [
    table_drop_events,
    table_drop_actors,
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