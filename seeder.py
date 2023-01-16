import sqlite3 as sql

DB_PATH = "movies.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE movies(
        
        tittle text,
        url_img text,
        clasification text,
        id_function integer,
        date_time text-
    )""")
    conn.commit()
    conn.close()

def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data=[
        ("Avatar","https://cdn.shopify.com/s/files/1/0057/3728/3618/products/313099306_466556672134552_8738886800381528729_n_480x.progressive.jpg?v=1669136451","B",1234,"2022-03-15 12:05:57"),
        ("Spiderman","https://cdn.shopify.com/s/files/1/0057/3728/3618/products/301983133_1072845516765536_7607702103270945846_n_500x749.jpg?v=1665071762","B",4560,"2021-03-15 12:05:57"),
        ("Batman","https://cdn.shopify.com/s/files/1/0057/3728/3618/products/c6f663c3b042cb061aa74d607183a34c_31928227-8024-4131-bbd8-eb3a67a426ba_500x749.jpg?v=1573587310","B",7890,"2023-03-15 12:05:57")
    ]
    cursor.executemany("""INSERT INTO movies VALUES (?,?,?,?,?)""",data)
    conn.commit()
    conn.close()

#print("Hola mundo")
createDB()
addValues()
    

