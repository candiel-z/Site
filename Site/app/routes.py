from flask import render_template, redirect, request

from app import app, database


@app.route('/', methods=['GET'])
def index():
    data = database.get_all()
    return render_template('index.html', data=data)

@app.route('/show_products<order_id>', methods=['GET'])
def show_products(order_id):

    data = database.get(order_id)
    return render_template('show_products.html', data=data)

@app.route('/add_order', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        database.add(request.form)
        return redirect('/')
    if request.method == 'GET':
        return render_template('add_order.html')
