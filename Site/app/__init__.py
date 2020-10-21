from flask import Flask

from config.config import Config
from app.database import Database


database = Database()

app = Flask(__name__)
app.config.from_object(Config)
