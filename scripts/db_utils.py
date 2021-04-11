def connect_to_db(retry_count=0):
    import os
    from mysql.connector import connect, Error, errorcode
    from decouple import config
    from time import sleep

    hostname = os.getenv("HOSTNAME")
    if not hostname:
        hostname = "localhost"
    user = config("MYSQL_USER", "admin")
    password = config("MYSQL_PASSWORD", "password2+")
    database = config("MYSQL_DATABASE", "weather")

    try:
        return connect(host=hostname, user=user, password=password, database=database)
    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        elif err.errno == errorcode.CR_CONN_HOST_ERROR:
            print("Host not accessible or not ready")
            if retry_count < 5:
                sleep(10)
                return connect_to_db(retry_count+1)
        else:
            print(err)


def execute(cursor, sql, params=None):
    cursor.execute(sql, params)


def create_tables(connection):
    from mysql.connector import Error, errorcode

    print("Creating tables ...")

    TABLES = {}

    from weather_data import TABLE_NAME, CREATE_TABLE_SQL
    TABLES[TABLE_NAME] = CREATE_TABLE_SQL

    cursor = connection.cursor()

    for table_name in TABLES:
        try:
            execute(cursor, TABLES[table_name])
            print("  Table '{0}' created.".format(table_name))
        except Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("  Table '{0}' already exists.".format(table_name))
            else:
                print("  Error creating table '{0}' > {1}".format(table_name, err.msg))
                exit(1)

    cursor.close()

    print("Tables successfully created.")
