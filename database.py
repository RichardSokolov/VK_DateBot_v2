import psycopg2
import config

connection = psycopg2.connect(
    host=config.config_data[0],
    user=config.config_data[1],
    password=config.config_data[2],
    database=config.config_data[3]
)

connection.autocommit = True


def create_table_seen_users():
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS seen_users(
            id serial,
            vk_id varchar(50) PRIMARY KEY);"""
        )
    print("[INFO] Table SEEN_USERS was created.")


def insert_data_seen_users(vk_id_candidate):
    print(vk_id_candidate)
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO seen_users (vk_id) 
            VALUES ('{vk_id_candidate}');"""
        )


def select_seen(vk_id_candidate):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT vk_id
                FROM seen_users
                WHERE vk_id ='{vk_id_candidate}' """
        )
        return cursor.fetchone()


def drop_seen_users():
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE  IF EXISTS seen_users CASCADE;"""
        )
        print('[INFO] Table SEEN_USERS was deleted.')


def creating_database():
    create_table_seen_users()


def drop_table():
    drop_seen_users()
