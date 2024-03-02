import sqlite3
import os

global conn
global cursor

#connect to the database nand create a cursor object
def connect_db():
    global conn
    conn = sqlite3.connect('database.db', timeout=10)
    global cursor
    cursor = conn.cursor()

#create table
def create_db():
    global cursor
    cursor.execute('''CREATE TABLE "Houses" (
        "id"	INTEGER,
        "agency"	TEXT NOT NULL,
        "beds"	INTEGER NOT NULL,
        "baths"	INTEGER NOT NULL,
        "price"	INTEGER NOT NULL,
        "address"	TEXT NOT NULL,
        "image"	TEXT NOT NULL,
        "desc"	TEXT NOT NULL,
        PRIMARY KEY("id")
        )''')

#insert data into the table
def insert_into_db(id:int, agency:str, beds:int, baths:int, price:int, address:str, image:str, desc:str):
    global cursor  
    cursor.execute('''INSERT INTO HOUSES VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (id, agency, beds, baths, price, address, image, desc))   
    conn.commit() 

#display all data
def display_db_data():
    global cursor
    data=cursor.execute('''SELECT * FROM HOUSES''')
    for row in data: 
        print(row) 

#get all the ids of houses
def get_ids():
    global cursor
    id = []
    data=cursor.execute('''SELECT ID FROM HOUSES''')
    for row in data:
        id.append(row[0])
    return id

#get a row corresponding to a specified house ID
def get_info(id:int):
    global cursor
    data=cursor.execute('''SELECT * FROM HOUSES WHERE ID = (?)''', [id])
    for row in data:
        return row

#delete the entire database
def delete_db():
    os.remove('''database.db''')

#close the connection
def close_db():
    global conn
    conn.close()


"""connect_db()
create_db()
insert_into_db(6,"agency",9,2,189,"radford", "image....", "cool description woah")
display_db_data()
delete_db()
close_db()"""

connect_db()
#insert_into_db(14,"agency",9,2,189,"radford", "image....", "cool description woah")
get_ids()
get_info(8)
close_db()