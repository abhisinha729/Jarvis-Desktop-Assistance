import csv
import sqlite3

conn=sqlite3.connect("jarvis.db")

cursor=conn.cursor() #cursor is the type of variable that  is used to execute variable

# query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
# cursor.execute(query)

# query="INSERT INTO sys_command VALUES(null,'android studio','C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe')"
# cursor.execute(query)
# conn.commit()  #use to save database


# query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100),url VARCHAR(1000))"
# cursor.execute(query)

# query="INSERT INTO web_command VALUES(null,'canva','https://www.canva.com/')"
# cursor.execute(query)
# conn.commit()  #use to save database


# Delete all rows from both tables
# cursor.execute("DELETE FROM sys_command")
# cursor.execute("DELETE FROM web_command")

# conn.commit()
# conn.close()
# print("table created successfully!")

# Get all table names
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()

# for table in tables:
#     cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")



# print("All tables deleted successfully.")

#create table with desired columns
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(id integer primary key,name VARCHAR(200),mobile_no VARCHAR(255),email VARCHAR(255) NULL) ''')

#specify the column indices you want to import (0-based index)
# desired_columns_indices=[0,21]

#read data from csv and insert  into sqlite  table for the desired columns
# query="INSERT INTO contacts VALUES(null,'Papa','9386541863',null)"
# cursor.execute(query)

# commit changes and close connection
# conn.commit()
# conn.close()

#search contact from database 
query='Papa'
query=query.strip().lower()
cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?",('%' + query + '%',query + '%'))
result=cursor.fetchall()
print(result[0][0])