from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from main import app

# 設定你的 app
manager = Manager(app)
# 設定 python manage.py runserver 為啟動 server 指令
manager.add_command('runserver', Server())

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':

    manager.run()