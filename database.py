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
    print("Data Inserted in the table: ") 
    global cursor
    data=cursor.execute('''SELECT * FROM HOUSES''')
    for row in data: 
        print(row) 

def delete_db():
    os.remove('''database.db''')

#close the connection
def close_db():
    global conn
    conn.close()