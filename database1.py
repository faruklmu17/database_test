import sqlite3

connection = sqlite3.connect("database.db")

#sql - structured query language
# cursor allows us to perform operations in your database
cursor = connection.cursor()

#create a table in the database called database.db

cursor.execute("CREATE TABLE students (id INTEGER, name TEXT,grade INTEGER)")

#insert some data in the table
cursor.execute("INSERT INTO students VALUES(101,'John',4)")

#commit the change into the database
connection.commit()

#run a query to see the student data
cursor.execute("SELECT * FROM students")

print(cursor.fetchall())

connection.close()
