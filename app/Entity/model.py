from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand

from main import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import Keeper,User,Kinda
# from . import InsertData

# InsertData.insert_data()



