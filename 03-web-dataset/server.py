from bottle import route, run, template,post,get,redirect,request,response
import dataset

db = dataset.connect("sqlite:///shopping_items.db")

@route("/")
def get_list():
    items = [dict(item) for item in db['shopping'].find()]
    shopping_list = [{'id':item['id'],'desc':item['description'],'price':item['price'],'quant':item['quantity']} for item in items]
    return template('shopping_items.tpl',shopping_item = shopping_list)


@get("/add")
def get_add():
    return template('add_item.tpl')

@post('/add')
def post_add():
    description = request.forms.get("description")
    table  = db['shopping']
    table.insert ({"description": description})
    redirect('/')

@route("/edit/<id>")
def get_edit(id):
    items = [dict(item) for item in db['shopping'].find(id=id)]
    if len(items) != 1:
        redirect('/')
    item = items[0]
    return template('edit_item.tpl', id=item['id'], description=item['description'],price=item['price'],quantity=item['quantity'])


@post("/edit/<id>")
def post_edit(id):
    description = request.forms.get("description")
    price = request.forms.get("price")
    quantity = request.forms.get("quantity")
    db['shopping'].update({'id':id, 'description':description,'price':price,'quantity':quantity},['id'])
    redirect("/")

@route('/delete/<id>')
def get_delete(id):
    db['shopping'].delete(id = id)
    redirect('/')

run(host='localhost', port=8080)