from flask import render_template, redirect, request

from app import app, database


@app.route('/', methods=['GET', 'POST'])
def index():
    orders = database.get()
    return render_template('index.html', orders=orders)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        mobile_number = request.form.get('mobile_number')
        database.add(name=name, surname=surname, mobile_number=mobile_number)
        return redirect('/')
    if request.method == 'GET':
        return render_template('add.html')
