from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

import os

static_dir='app/static'

template_dir = 'app/templates'

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

Bootstrap(app)

app.secret_key = 'a4c77ebc7f052ff2d2fdd693a60008d1'  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# login = LoginManager(app)  
# login.login_view = 'login'

import router

from app.Entity import model
