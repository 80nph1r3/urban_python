import sqlite3

db_conn = sqlite3.connect("not_telegram.db")
cursor = db_conn.cursor()

cursor.execute(
    "create table if not exists Users (id integer primary key, username text not null, email text not null, age integer, balance integer not null)"
)

for i in range(1, 11):
    cursor.execute(
        f"insert into Users (username, email, age, balance) values ('user{i}', 'example{i}@gmail.com', {i * 10}, 1000)"
    )

for i in range(1, 11, 2):
    cursor.execute(f"update Users set balance = 500 where username = 'user{i}'")

for i in range(1, 11, 3):
    cursor.execute(f"delete from Users where username = 'user{i}'")

cursor.execute("select * from Users where age != 60")
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}")

db_conn.commit()
db_conn.close()
