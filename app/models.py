from flask_sqlalchemy import SQLAlchemy

from app import db


class Client(db.Model):
    """"""

    __tablename__ = "clients"

    primary_key = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, unique=True, nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    second_name = db.Column(db.String(32), nullable=False)
    mobile_number = db.Column(db.String(11), nullable=False)
    summ = db.Column(db.Integer, nullable=False)

    def __init__(self, order_id, first_name, second_name, mobile_number, summ):
        self.order_id = order_id
        self.first_name = first_name
        self.second_name = second_name
        self.mobile_number = mobile_number
        self.summ = summ

    def __repr__(self):
        return f'<order_id: {self.order_id}; first_name: {self.first_name}; second_name: {self.second_name}; mobile_number: {self.mobile_number}>'


class Order(db.Model):
    """"""

    __tablename__ = 'orders'

    primary_key = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    product_name = db.Column(db.String(32), nullable=False)
    product_amount = db.Column(db.Integer, nullable=False)
    summ = db.Column(db.Integer, nullable=False)

    def __init__(self, order_id, product_name, product_amount, summ):
        self.order_id = order_id
        self.product_name = product_name
        self.product_amount = product_amount
        self.summ = summ

    def __repr__(self):
        return f'<order_id: {self.order_id}; product_name: {self.product_name}; product_amount: {self.product_amount}>'


class Product(db.Model):
    """"""

    __tablename__ = 'products'

    primary_key = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(32), unique=True, nullable=False)
    product_price = db.Column(db.Integer, nullable=False)

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def __repr__(self):
        return f'<product_name: {self.product_name}; price: {self.product_price}>'
