#!/usr/bin/env python

def prepare():
    from db_utils import connect_to_db, create_tables

    print("Preparing environment ...")
    connection = connect_to_db()
    if connection:
        try:
            create_tables(connection)
        finally:
            connection.close()

        print("Environment successfully prepared.")


def main():
    prepare()


if __name__ == "__main__":
    main()
