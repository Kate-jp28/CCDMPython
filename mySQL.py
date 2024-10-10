import MySQLdb
import csv
#Create a connection
myconnection = MySQLdb.Connection(host = "localhost", user = "root", passwd = "ceit")

#Create a cursor object used to hold connection 
mycursor = myconnection.cursor()

 #now let's start with SQL queries
#mycursor.execute('CREATE DATABASE CEITLIBRARY')
#mycursor.execute('USE CEITLIBRAY')
tablebook = """CREATE TABLE Books(BookID int primary key, title varchar(20), Author varchar(20),Genre varchar(20))"""

tablereaders = """CREATE TABLE Readers (ReadID int primary key, ReaderFName
varchar (10), ReaderSurname varchar(20),
Course varchar(6),BkID int)"""

book1 ="""INSERT INTO books Values(101,"Intro to python", "Tom Jerry", "Programming")"""
reader1 = """INSERT INTO Readers VALUES(201,"Johnny","Walker","CCDM",101)"""
#To execute tablebook
#mycursor.execute(tablebook) #comment out after executing
#mycursor.execute(book1) #comment out after executing

#To execute tablereader
#mycursor.execute(tablereaders) #comment out after executing
#mycursor.execute(reader1)
#mycursor.execute('SHOW DATABASES')
file = open('books.csv')
contents = csv.reader(file)
insertVal = "INSERT INTO book (BookID,title,author,genre) VALUES(?,?,?,?)"
mycursor.executemany(insertVal,contents)
selectall = "select * From book"
rows =mycursor.execute(selectall).fetchall()
for row in rows:
    print(row)


# To fetch data and display output
result = mycursor.fetchall()

#commit changes
myconnection.commit()
#for row in result:
 #   print(row)
