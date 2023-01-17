import sqlite3 as sql

DB_PATH2 = "databases\\users.db"

def createDbUsers():
    conn = sql.connect(DB_PATH2)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE users(
        
        name text,
        last_name text,
        password text,
        email text,
        phone integer
    )""")
    conn.commit()
    conn.close()

createDbUsers()