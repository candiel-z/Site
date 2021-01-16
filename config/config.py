from pathlib import Path


class Config(object):
    PROJECT_ROOT = Path.cwd().parent
    DEBUG = True
    DATABASE = 'database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{PROJECT_ROOT}\\{DATABASE}'
