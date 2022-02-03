from bottle import route, run, template
import sqlite3

connection = sqlite3.connect("shopping_items.db")


@route('/index')
def index():
    global connection
    cursor = connection.cursor()
    items = cursor.execute("select id,description from list")
    shopping_list = [{'id':item[0],'desc':item[1]} for item in items]
    return template('shopping_items.tpl',shopping_item = shopping_list)

@route('/delete/<id>')
def delete(id):
    return template('delete.tpl',id = id)

run(host='localhost', port=8080)