import sqlite3


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
