# -*- coding: utf-8 -*-
import sys
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
sys.path.append('/home/k/kerlaeda/vetlife.klinskih.com/public_html')
from VetLife import app, db

migrate = Migrate(app, db)

# Инициализируем менеджер
manager = Manager(app)
# Регистрируем команду, реализованную в виде потомка класса Command
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
