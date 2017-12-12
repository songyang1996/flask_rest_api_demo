# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class BaseModel(object):
    "模型基类"
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Author(BaseModel, db.Model):
    "作者模型类"
    __tablename__ = "authors"
    id=db.Column(db.INTEGER,primary_key=True)
    name=db.Column(db.String(10))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
    }

class Book(BaseModel, db.Model):
    "图书模型类"
    id=db.Column(db.INTEGER,primary_key=True)
    title=db.Column(db.String(10))
    author_id=db.Column(db.INTEGER,db.ForeignKey('authors.id'))
