from app import db
from app.models import Client, Order, Product


def add_order(form):
    """"""

    order_id, first_name, second_name, mobile_number, product_names, product_amounts = get_order_data(form)

    summ = 0

    if len(product_names) == len(product_amounts):
        for i in range(len(product_names)):
            price = Product.query.filter(Product.product_name == product_names[i]).first().product_price
            summ += price
            order = Order(order_id, product_names[i], product_amounts[i], price)
            db.session.add(order)

    client = Client(order_id, first_name, second_name, mobile_number, summ)

    db.session.add(client)
    db.session.commit()

def get_order_data(form):
    """"""

    order_id = form.order_id.data
    first_name = form.first_name.data
    second_name = form.second_name.data
    mobile_number = form.mobile_number.data

    product_names = form.product_name.raw_data
    product_amounts = form.product_amount.raw_data

    return order_id, first_name, second_name, mobile_number, product_names, product_amounts

def add_product(form):
    """"""

    product_name = form.product_name.data
    product_price = form.product_price.data

    product = Product(product_name, product_price)

    db.session.add(product)
    db.session.commit()

def delete_product(form):
    """"""

    del_name = form.del_name.data

    Product.query.filter(Product.product_name == del_name).delete()
    db.session.commit()
