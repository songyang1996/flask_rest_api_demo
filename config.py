# -*- coding: utf-8 -*-

class Config:
    DEBUG = False

class DevelopConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI='mysql://root:mysql@localhost:3306/test1'
    # python 3 创建迁移文件
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:1099@localhost:3306/test1'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
