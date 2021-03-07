import sqlite3

#Create the database file, here name is MyDataBase.db
dbase = sqlite3.connect("MyDataBase.db") #extension can be anything. i.e .db, .sqlite3, .dbase, .ibrahim etc, preferrably .db

print("Database Opened")

#Close database when you are done with the dbase file
dbase.close()

print("Database Closed")
