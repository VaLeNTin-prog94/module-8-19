import sqlite3

connection = sqlite3.connect('Users.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    create table if not exists Users(
    id INTEGER PRIMARY KEY,
    username   TEXT NOT NULL ,
    email  text not null,
    age int not null,
    balance  int not null
    );

    ''')


initiate_db()


def is_included(username):
    if cursor.execute("select *from Users Where username=?",
                      (username,)).fetchone() is None:
        return True
    else:
        return False


def add_user(username, email, age):
    if is_included(username):
        cursor.execute(" INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,?)",
                       (f"{username}", f"{email}", f"{age}", "1000"))
        connection.commit()


def get_all_products():
    return (cursor.execute("select * from Users").fetchall())


connection.commit()
