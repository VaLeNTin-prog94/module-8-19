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
    # for i in range(1, 11):
    #     cursor.execute(" INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,?)",
    #                    (f"User{i}", f"example1{i}@gmail.com", f"{i * 10}", "1000"))
    # cursor.execute("UPDATE Users Set balance=?  Where id%2!=0", (500,))
    # for id_delete in [i for i in range(1, 11, 3)]:
    #     cursor.execute("DELETE FROM Users  Where id=?", (id_delete,))
    cursor.execute("delete from Users where id=6 ")
total_users = cursor.execute('select count(*) from Users').fetchone()[0]
all_balances= cursor.execute('select sum(balance) from Users').fetchone()[0]
print(all_balances/total_users)
