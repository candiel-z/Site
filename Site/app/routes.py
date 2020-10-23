from flask import render_template, redirect, request

from app import app, database


@app.route('/', methods=['GET'])
def index():
    clients = database.get()
    return render_template('index.html', clients=clients)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        database.add(request.form)
        return redirect('/')
    if request.method == 'GET':
        return render_template('add.html')
