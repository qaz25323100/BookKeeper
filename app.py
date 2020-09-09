from flask import Flask,render_template

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import router
import os

static_dir='app/static'

template_dir = 'app/templates'

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template("index.html", name=name)


@app.route('/login')
def login_page(request=None):
    return render_template("login.html")


if __name__ == "__main__":

    app.run(debug=True)