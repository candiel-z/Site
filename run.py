from flask import Flask

from app import app, views


if __name__ == '__main__':
    app.run(host='127.0.1.0', port='5999')
