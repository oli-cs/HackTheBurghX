import sqlite3

global conn
global cursor

#connect to the database nand create a cursor object
def connect_db():
    global conn
    conn = sqlite3.connect('cache.db', timeout=10)
    global cursor
    cursor = conn.cursor()

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
    print(5) 
    for row in data: 
        print(row) 

#close the connection
def close_db():
    global conn
    conn.close()