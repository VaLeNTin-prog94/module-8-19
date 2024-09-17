import sqlite3

with sqlite3.connect('not_telegram.db') as db:
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL, 
    email TEXT NOT NULL,
    age INTEGER,
    balance  INTEGER NOT NULL
    )
    ''')
    for i in range(1, 11):
        cursor.execute(" INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,?)",
                       (f"User{i}", f"example1{i}@gmail.com", f"{i * 10}", "1000"))
    cursor.execute("UPDATE Users Set balance=?  Where id%2==0", (500,))
    for id_delete in [i for i in range(1, 11, 3)]:
        cursor.execute("DELETE FROM Users  Where id=?", (id_delete,))
for user in cursor.execute("SELECT username,email,age,balance FROM Users Where age!=60").fetchall():
    print(user)
