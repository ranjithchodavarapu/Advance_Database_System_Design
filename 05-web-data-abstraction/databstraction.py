import dataset

db = dataset.connect("sqlite:///shopping_items.db")

def shopping_list_setup():
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


def get_shopping_list():
    items = [dict(item) for item in db['shopping'].find()]
    shopping_list = [{'id':item['id'],'desc':item['description'],'price':item['price'],'quant':item['quantity']} for item in items]
    return shopping_list


def add_item_list(description):
     table  = db['shopping']
     table.insert ({"description": description})


def update_item_list(id,description,price,quantity):
     db['shopping'].update({'id':id, 'description':description,'price':price,'quantity':quantity},['id'])

def delete_items_list(id):
      db['shopping'].delete(id = id)