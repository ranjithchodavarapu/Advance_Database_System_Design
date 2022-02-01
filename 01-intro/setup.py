import sqlite3

connection = sqlite3.connect("project.db")
cursor = connection.cursor()

#create the table in the database
cursor.execute("create table pet (id integer primary key, name text, species_id integer)")
cursor.execute("create table species (id integer primary key, kind text)")

#insert the data in to the table

cursor.execute("insert into species (kind) values ('dog')")
cursor.execute("insert into species (kind) values ('cat')")
cursor.execute("insert into species (kind) values ('horse')")
cursor.execute("insert into species (kind) values ('rabbit')")
cursor.execute("insert into species (kind) values ('cat')")

cursor.execute("insert into pet (name,species_id) values ('dora',1)")
cursor.execute("insert into pet (name,species_id) values ('jack',2)")
cursor.execute("insert into pet (name,species_id) values ('jimmy',3)")
cursor.execute("insert into pet (name,species_id) values ('rocky',4)")
cursor.execute("insert into pet (name,species_id) values ('kitty',2)")



#commit and close the database 
connection.commit()
connection.close()

print("completed..")
