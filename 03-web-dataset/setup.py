import dataset

#connection
db = dataset.connect("sqlite:///shopping_items.db")


try:
    db.begin()
    db['list'].drop()
    table  = db['shopping']
    items = [
        {"description":"onion","price":2,"quantity":"2lb"},
        {"description":"tomatos","price":1,"quantity":"3lb"},
        {"description":"meat","price":6,"quantity":"1lb"},
        {"description":"eggs","price":5,"quantity":"1doz"},
        {"description":"mango","price":4,"quantity":"3lb"},
        {"description":"blueberry","price":5,"quantity":"1box"}

    ]
    table.insert_many(items)
    db.commit()

except Exception as e:
    db.rollback()

print("executed")