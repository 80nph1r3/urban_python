import sqlite3
from types import LambdaType


def initiate_db(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        """
        create table if not exists Products(
            id integer primary key,
            title text not null,
            description text not null,
            price integer not null
        );
    """
    )
    cursor.execute(
        """
        create table if not exists Users(
            id integer primary key,
            username text not null,
            email text not null,
            age integer not null,
            balance integer not null
        )
    """
    )


async def get_all_products() -> list:
    db_conn = sqlite3.connect("bot.db")
    cursor = db_conn.cursor()
    initiate_db(cursor)
    db_conn = sqlite3.connect("bot.db")
    cursor = db_conn.cursor()
    cursor.execute("select * from Products")
    results = cursor.fetchall()
    db_conn.commit()
    db_conn.close()
    return results


async def add_user(username: str, email: str, age: int) -> None:
    db_conn = sqlite3.connect("bot.db")
    cursor = db_conn.cursor()
    initiate_db(cursor)
    cursor.execute("select max(id) from Users;")
    last_id = cursor.fetchone()[0]
    id = last_id + 1 if last_id else 1
    cursor.execute(
        f"""
        insert into users values (
         {id}, '{username}', '{email}', {age}, 1000
        );
    """
    )
    db_conn.commit()
    db_conn.close()


async def is_included(username: str) -> bool:
    db_conn = sqlite3.connect("bot.db")
    cursor = db_conn.cursor()
    initiate_db(cursor)
    cursor.execute(f"select * from Users where username='{username}'")
    result = True
    if cursor.fetchone() is None:
        result = False
    db_conn.close()
    return result
