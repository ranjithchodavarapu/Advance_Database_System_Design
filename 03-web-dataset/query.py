import sqlite3

connection = sqlite3.connect("shopping_items.db")
cursor = connection.cursor()

rows = cursor.execute("select id,description from list")
#rows = list(rows)
#dictionary
rows = [{'id':row[0],'desc':row[1]} for row in rows]
print(rows)
#for i in rows:
    #name, kind = i
    #print(f"my kind is {kind} and name is {name}")

print("completed..")
