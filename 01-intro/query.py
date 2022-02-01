import sqlite3

connection = sqlite3.connect("pets.db")
cursor = connection.cursor()

rows = cursor.execute("select name, kind from pet, species where species_id = species.id").fetchall()
#rows = list(rows)
print(rows)
#for i in rows:
    #name, kind = i
    #print(f"my kind is {kind} and name is {name}")

print("completed..")
