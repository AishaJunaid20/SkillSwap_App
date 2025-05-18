# import sqlite3

# conn = sqlite3.connect('skillswap.db', check_same_thread=False)
# c = conn.cursor()

# def create_tables():
#     c.execute('''CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY, 
#         username TEXT UNIQUE, 
#         password TEXT
#     )''')
    
#     c.execute('''CREATE TABLE IF NOT EXISTS skills (
#         id INTEGER PRIMARY KEY,
#         user_id INTEGER,
#         skill_name TEXT,
#         price INTEGER,
#         barter INTEGER,
#         FOREIGN KEY(user_id) REFERENCES users(id)
#     )''')
#     conn.commit()

import sqlite3

conn = sqlite3.connect('skillswap.db', check_same_thread=False)
c = conn.cursor()

def create_tables():
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, 
        username TEXT UNIQUE, 
        password TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        skill_name TEXT,
        price INTEGER,
        barter INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL
    )''')

    conn.commit()
