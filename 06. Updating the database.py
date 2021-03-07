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

#Add data to database using a function with parameters
def insert_record(ID,NAME,DIVISION,STARS):
    dbase.execute(""" INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
        VALUES(?,?,?,?)""",(ID,NAME,DIVISION,STARS))
    # Alternatively, use: dbase.execute(""" INSERT INTO employee_records(*) """) where * signifies ALL
    # or specify the particular fields to insert into if not all
    # But NOT NULL -> every field must have values, hence All i.e ID,NAME,DIVISION,STARS

    #Apply changes to db using commit
    dbase.commit()
    print("Changes applied")

##insert_record(3,"Suleiman","Engineer",9)

#Function to display data from database
def read_data():
    data = dbase.execute(""" SELECT ID, NAME, DIVISION, STARS FROM employee_records """)
    # alternatively, dbase.execute(""" * FROM employee_records """), order same as defined when table created
    for record in data:
        print("ID: "+ str(record[0]))
        print("NAME: "+ str(record[1]))
        print("DIVISION: "+ str(record[2]))
        print("STARS: "+ str(record[3])+"\n")
        
print("ALL DATA FROM DATABASE, UNORDERED")
read_data()
print("\n\n")

#Function to dislay only name and division data from database
def read_Name_division_data():
    data1 = dbase.execute(""" SELECT NAME, DIVISION FROM employee_records """)
    for record in data1:
        print("NAME: "+ str(record[0]) + "; " + "DIVISION " + record[1])

print("NAME AND DIVISION DATA FROM DATABASE, UNORDERED")
read_Name_division_data()
print("\n\n")

#Function to display data from database with order by name
def read_data_order_by_name():
    data = dbase.execute(""" SELECT ID, NAME, DIVISION, STARS FROM employee_records ORDER BY NAME """)
    # alternatively, dbase.execute(""" * FROM employee_records """), order same as defined when table created
    for record in data:
        print("ID: "+ str(record[0]))
        print("NAME: "+ str(record[1]))
        print("DIVISION: "+ str(record[2]))
        print("STARS: "+ str(record[3])+"\n")
        

print("ALL DATA FROM DATABASE, ORDERED BY NAME")
read_data_order_by_name()
print("\n\n")

#Function to display data from 3 of database
def read_data_row_three():
    data = dbase.execute(""" SELECT ID, NAME, DIVISION, STARS FROM employee_records """)
    # alternatively, dbase.execute(""" * FROM employee_records """), order same as defined when table created  

    datalist = list(data)
    print("values in database: "+ str(datalist))
    print("values in data row 3: "+ str(datalist[2]))
    print("ID: " + str(datalist[2][0]))
    print("NAME: " + str(datalist[2][1]))
    print("DIVISION: " + str(datalist[2][2]))
    print("STARS: " + str(datalist[2][3]))
    
    
print("Values of data in row 3 of the database")
read_data_row_three()
print("\n\n")

#Function to update database
def update_record():
    dbase.execute(""" UPDATE employee_records set DIVISION="ELECTRONICS" WHERE ID=2 """)
    dbase.commit()

update_record()
print("database updated")
  
#Close database when you are done with the dbase file
dbase.close()
print("Database Closed")




