from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(10))
    pwd = db.Column(db.String(40))
    name = db.Column(db.String(12))
    salary = db.Column(db.Integer)

    