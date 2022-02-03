import sqlite3

#connection

connection = sqlite3.connect("shopping_items.db")

cursor = connection.cursor()

#create table

cursor.execute("create table list (id integer primary key, description text)")


# insert the data in to the table
cursor.execute("insert into list (description) values ('onion')")
cursor.execute("insert into list (description) values ('tomatos')")
cursor.execute("insert into list (description) values ('meat')")
cursor.execute("insert into list (description) values ('eggs')")
cursor.execute("insert into list (description) values ('mango')")
cursor.execute("insert into list (description) values ('blueberry')")


#commit and close the database 
connection.commit()
connection.close()

print("completed...")