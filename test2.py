# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

# 配置类
from config import DevelopConfig
app.config.from_object(DevelopConfig)

# 注册模型类
from models import db
db.init_app(app)

# 管理命令包
from flask_script import Manager
manager = Manager(app)

# 迁移命令
from flask_migrate import Migrate, MigrateCommand
Migrate(app,db)
manager.add_command("db", MigrateCommand)

# 注册蓝图
from api_v1.author_views import author_blueprint
app.register_blueprint(author_blueprint, url_prefix="/api/v1")

if __name__ == '__main__':
# app.run(host:'127.0.0.1', port=8000, debug=True)
    manager.run()
