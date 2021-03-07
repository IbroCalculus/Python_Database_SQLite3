import sqlite3

#Reference: Python for everybody, Timestamp: about 09:00:35
#For this, we use DB Browser for SQLite

#CREATE DATABASE
'''
    First, create a database. E.g: testData.db (Done visually in in SQLite. Otherwise
    CREATE DATABASE testData
'''

#CREATE TABLE IN DATABASE Users
''' 
    Visually; Self-explainable
    
    otherwise:

    CREATE TABLE Users (
        "Name" TEXT,
        "Email" TEXT,
    );
    
    Available datatype: TEXT, INTEGER, BLOB, REAL, NUMERIC
'''

#INSERT DATA INTO TABLE
'''
    VISUALLY ON SQLite, Go to "Browse Data" Tab, Click on New Record
     
     otherwise: Navigate to "Execute SQL" tab:
     
    INSERT INTO Users (Name, Email) VALUES ("Ibrahim", "ibrahim@email.com");
                    or
    INSERT INTO Users VALUES ("Aboy", "aboy@email.com");
    click the RUN/PLAY icon to submit the changes   
'''

#DELETE A ROW IN A TABLE based on selection criteria
'''
    VISUALLY: Go to "Browse Data" Tab, Highlight the record, Click on Delete record.
    
    otherwise: Navigate to "Execute SQL" tab:
    
    DELETE FROM Users WHERE "Email"="suleiman@email.com";
    
    NB: If duplicates, it deletes all
    
'''

#DELETE ALL RECORDS IN THE DATABASE
'''
    DELETE FROM Users;
'''

#UPDATE TABLE RECORD
'''
    UPDATE Users SET Name="AAboy", Email="aaboy@email.com" WHERE Name="Aboy";
'''

#RETRIEVE ALL RECORDS FROM A TABLE
'''
    SELECT * FROM Users;
'''

#RETRIEVE A PARTICULAR COLUMN FROM A TABLE
'''
    SELECT Name FROM Users;
'''

#RETRIEVE A PARTICULAR COLUMN WITH CONDITION
'''
    SELECT Name FROM Users where Name="Aboy";
'''

#RETRIEVE DISTINCT
'''
The SELECT DISTINCT statement is used to return only distinct (different) values.
Inside a table, a column often contains many duplicate values; and sometimes you only want to list the different (distinct) values.
    SELECT DISTINCT * FROM Users;
    SELECT DISTINCT Name FROM Users;
    SELECT DISTINCT count(Name) FROM Users;         #Count the number of distinct values
'''

#SORTING
'''
    SELECT * FROM Users ORDER BY Name DESC; //ASC
'''