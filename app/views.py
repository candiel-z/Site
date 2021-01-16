from flask import render_template, redirect, request

from app import app, db
from app.models import Client, Order, Product
from app.forms import AddOrderForm, AddProductForm, DeleteProductForm
from app.database import *


@app.route('/')
def index():
    """"""

    return render_template('index.html')

@app.route('/view', methods=['GET'])
def view():
    """"""

    order_id = request.args.get('order_id')
    sort_type = request.args.get('sort_type')

    if order_id and sort_type:
        return redirect('/view?sort_type=id')
    elif order_id:
        client = Client.query.filter(Client.order_id==order_id).first()
        orders = Order.query.filter(Order.order_id==order_id).all()
        return render_template('view_order.html', client=client, orders=orders)
    elif sort_type:
        if sort_type == 'id':
            clients = Client.query.order_by(Client.order_id).all()
            return render_template('view.html', clients=clients)
        if sort_type == 'first_name':
            clients = Client.query.order_by(Client.first_name).all()
            return render_template('view.html', clients=clients)
        if sort_type == 'second_name':
            clients = Client.query.order_by(Client.second_name).all()
            return render_template('view.html', clients=clients)
        if sort_type == 'mobile_number':
            clients = Client.query.order_by(Client.mobile_number).all()
            return render_template('view.html', clients=clients)
        if sort_type == 'sum':
            clients = Client.query.order_by(Client.summ).all()
            return render_template('view.html', clients=clients)
    else:
        return redirect('/view?sort_type=id')

@app.route('/add', methods=['GET', 'POST'])
def add():
    """"""

    add_order_form = AddOrderForm()
    next_order_id = Client.query.order_by(Client.order_id.desc()).first()
    if not next_order_id:
        next_order_id = 0
    else: 
        next_order_id = next_order_id.order_id + 1

    if request.method == 'POST' and add_order_form.validate():
        add_order(add_order_form)
        return redirect('/view?sort_type=id')  
    elif request.method == 'GET':
        return render_template('add_order.html', next_order_id=next_order_id, form=add_order_form)
    else:
        return render_template('add_order.html', next_order_id=next_order_id, form=add_order_form)

@app.route('/products', methods=['GET', 'POST'])
def products():
    """"""

    add_product_form = AddProductForm()
    del_product_form = DeleteProductForm()

    products = Product.query.all()

    if request.method == 'POST':
        if add_product_form.add_submit.data and add_product_form.validate_on_submit():
            add_product(add_product_form)
            return redirect('/products')
        if del_product_form.del_submit.data and del_product_form.validate_on_submit():
            delete_product(del_product_form)
            return redirect('/products')
    elif request.method == 'GET':
        return render_template('products.html', products=products, add_form=add_product_form, del_form=del_product_form)
    else:
        return render_template('products.html', products=products, add_form=add_product_form, del_form=del_product_form)
