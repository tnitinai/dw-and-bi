import glob
import json
import os
from typing import List

import psycopg2 ## library to communicate to Progresql


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


def process(cur, conn, filepath):
    # Get list of files from filepath
    all_files = get_files(filepath)

    for datafile in all_files:
        with open(datafile, "r") as f:
            data = json.loads(f.read())
            for each in data:
                # Print some sample data
                
                if each["type"] == "IssueCommentEvent":
                    print(
                        each["id"], 
                        each["type"],
                        each["actor"]["id"],
                        each["actor"]["login"],
                        each["repo"]["id"],
                        each["repo"]["name"],
                        each["created_at"],
                        each["payload"]["issue"]["url"],
                    )
                else:
                    print(
                        each["id"], 
                        each["type"],
                        each["actor"]["id"],
                        each["actor"]["login"],
                        each["repo"]["id"],
                        each["repo"]["name"],
                        each["created_at"],
                    )

                # Insert data into tables here
                insert_statement = f"""
                    INSERT INTO actors (
                        id,
                        login,
                        display_login
                    ) VALUES (
                        {each["actor"]["id"]}, 
                        '{each["actor"]["login"]}',
                        '{each["actor"]["display_login"]}'
                    )
                    ON CONFLICT (id) DO NOTHING
                """
                # print(insert_statement)
                cur.execute(insert_statement)

                # Insert data into tables here
                insert_statement = f"""
                    INSERT INTO events (
                        id,
                        type,
                        actor_id,
                        created_at
                    ) VALUES (
                        '{each["id"]}', 
                        '{each["type"]}', 
                        '{each["actor"]["id"]}',
                        '{each["created_at"]}'
                    )
                    ON CONFLICT (id) DO NOTHING
                """
                # print(insert_statement)
                cur.execute(insert_statement)

                conn.commit()
                
                # Insert data into repos table
                insert_statement = f"""
                    INSERT INTO repos (
                        id,
                        name,
                        owner_id
                    ) VALUES (
                        '{each["repo"]["id"]}', 
                        '{each["repo"]["name"]}', 
                        '{each["actor"]["id"]}'
                    )
                    ON CONFLICT (id) DO NOTHING
                """
                # print(insert_statement)
                cur.execute(insert_statement)

                conn.commit()
                
                # Insert data into comments table
                if(each["type"] == "IssueCommentEvent"):
                    insert_statement = f"""
                        INSERT INTO comments (
                            id,
                            repo_id,
                            user_id,
                            total_count,
                            liked,
                            unliked,
                            laugh,
                            hooray,
                            confused,
                            heart,
                            rocket,
                            eyes
                        ) VALUES (
                            '{each["payload"]["issue"]["id"]}', 
                            '{each["repo"]["id"]}', 
                            '{each["actor"]["id"]}',
                            each["payload"]["issue"]["body"]["reactions"]["total_count"],
                            each["payload"]["issue"]["body"]["reactions"]["+1"],
                            each["payload"]["issue"]["body"]["reactions"]["-1"],
                            each["payload"]["issue"]["body"]["reactions"]["laugh"],
                            each["payload"]["issue"]["body"]["reactions"]["hooray"],
                            each["payload"]["issue"]["body"]["reactions"]["confused"],
                            each["payload"]["issue"]["body"]["reactions"]["heart"],
                            each["payload"]["issue"]["body"]["reactions"]["rocket"],
                            each["payload"]["issue"]["body"]["reactions"]["eyes"]
                            
                        )
                        ON CONFLICT (id) DO NOTHING
                    """
                    # print(insert_statement)
                    cur.execute(insert_statement)

                    conn.commit()



def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=postgres"
    )
    cur = conn.cursor()

    process(cur, conn, filepath="../data")

    conn.close()


if __name__ == "__main__":
    main()