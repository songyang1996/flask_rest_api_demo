# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request, render_template
author_blueprint = Blueprint("author", __name__)
from models import Author

# @author_blueprint.route("/", methods=["GET"])
# def index():
#     "首页入口"
#     return render_template("author2.html")


@author_blueprint.route("/author", methods=["GET", "POST"])
def author_list():
    "查询全部作者表或者添加的视图"
    if request.method == "GET":
        alist = Author.query.all()

        alist2 = [author.to_dict() for author in alist]

        return jsonify(alist = alist2)

    if request.method == "POST":
        author_name = request.form.get("author_name")
        author = Author()
        author.name = author_name
        author.save()
        return jsonify(msg="ok")

@author_blueprint.route("/author/<id>", methods=["GET", "PUT", "DELETE"])
def author_one(id):
    "根据id进行指定作者操作的视图"
    if request.method == "GET":
        # 根据id查询作者
        author = Author.query.get(id)
        print(id, author)
        return jsonify(author=author.to_dict())

    if request.method == "DELETE":
        # 根据id物理删除作者
        author = Author.query.get(id)
        author.delete()
        return jsonify(msg="ok")

    if request.method == "PUT":
        # 修改作者姓名
        author = Author.query.get(id)
        name = request.form.get("name")
        print(name, author.name)
        author.name = name
        author.save()
        return jsonify(msg="ok")
