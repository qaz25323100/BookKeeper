from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import os

static_dir='app/static'

template_dir = 'app/templates'

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'


import router


# if __name__ == "__main__":

#     app.run(debug=True)