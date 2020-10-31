from flask import render_template, redirect, request

from app import app, database


@app.route('/')
def index():
    """"""
    
    return render_template('base.html')

@app.route('/view/<string:sort_type>', methods=['GET'])
def view(sort_type):
    """"""

    data = database.get_all()
    if sort_type == 'id':
        return render_template('view.html', data=data)
    if sort_type == 'first_name':
        return render_template('view.html', data=data)
    if sort_type == 'second_name':
        return render_template('view.html', data=data)
    if sort_type == 'mobile_number':
        return render_template('view.html', data=data)
    if sort_type == 'sum':
        return render_template('view.html', data=data)

@app.route('/view/<int:order_id>', methods=['GET'])
def view_order(order_id):
    """"""

    data = database.get(order_id)
    return render_template('view_order.html', data=data)

@app.route('/add', methods=['GET', 'POST'])
def add_order():
    """"""

    if request.method == 'POST':
        database.add(request.form)
        return redirect('/view/id')
    if request.method == 'GET':
        autoincrement_order_id = 0
        return render_template('add_order.html', autoincrement_order_id=autoincrement_order_id)
