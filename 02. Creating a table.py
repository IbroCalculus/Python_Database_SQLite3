import sqlite3

#Create the database file, here name is MyDataBase.db
dbase = sqlite3.connect("MyDataBase.db") #extension can be anything. i.e .db, .sqlite3, .dbase, .ibrahim etc, preferrably .db

print("Database Opened")

#Create a table named employee_records. The table will consist of:
# ID (int), NAME (text), DIVISION (text) and STARS (int) column
#NB: You can create multiple tables in a database
#PRIMATY KEY means unique data i.e 1,2,3... NO REPEATATION and there cannot be more than one primary key
#NOT NULL means the field should not remain empty.
#Can't create same table more than ones, hence error, hence the statement: IF NOT EXISTS
dbase.execute (""" CREATE TABLE IF NOT EXISTS employee_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    STARS INT NOT NULL
)
""")

#Test text
print("Table Created")


#Close database when you are done with the dbase file
dbase.close()
print("Database Closed")
