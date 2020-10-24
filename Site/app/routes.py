from flask import render_template, redirect, request

from app import app, database


@app.route('/', methods=['GET'])
def index():
    clients, orders = database.get_all()['clients'], database.get_all()['orders']
    return render_template('index.html', clients=clients, orders=orders)

@app.route('/products<identifier>', methods=['GET'])
def products(identifier):

    client, order = database.get(identifier)['client'], database.get(identifier)['order']
    return render_template('products.html', client=client, order=order)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        database.add(request.form)
        return redirect('/')
    if request.method == 'GET':
        return render_template('add.html')
