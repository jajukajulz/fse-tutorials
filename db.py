# usage: python db.py
import sqlite3

# create database or connect to existing db
connection = sqlite3.connect('fintechdb2.db') 

# check database was successfully created
print(connection.total_changes)
print("Opened database successfully")

# create a cursor object so you can send SQL commands to your database
cursor = connection.cursor()

# create table
cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER, name TEXT, age INTEGER)")

# insert data
cursor.execute("INSERT INTO example VALUES (1, 'alice', 20)")
cursor.execute("INSERT INTO example VALUES (2, 'bob', 30)")
cursor.execute("INSERT INTO example VALUES (3, 'eve', 40)")

# save the changes to your database you need to use the commit function
connection.commit()

# read and output data from your database
cursor.execute("SELECT * FROM example")
rows = cursor.fetchall()
for row in rows:
    print(row)

# delete data
# cursor.execute("DELETE FROM example WHERE id = 1")

# update data
# cursor.execute("UPDATE example SET age = 31 WHERE id = 2")

# close the connection to your database
connection.close()
