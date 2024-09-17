import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    create table if not exists Products(
    id INTEGER PRIMARY KEY,
    title  TEXT NOT NULL ,
    description TEXT ,
    price int not null
    );
    
    ''')


initiate_db()
def get_all_products():
    return  (cursor.execute("select * from Products").fetchall())


connection.commit()
