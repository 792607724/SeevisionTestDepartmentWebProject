# coding = utf8
import sys

sys.path.append("../../")
import os

os.path.abspath(".")
from flask import Flask, render_template, request

"""
    @Project:SeevisionTestDepartmentWebProject
    @File:app.py
    @Author:十二点前要睡觉
    @Date:2025/2/16 17:18
"""

app = Flask(__name__)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        # 接受到数据
        # 给用户返回结果
        print(request.form)
        user = request.form.get("user")
        pwd = request.form.get("pwd")
        gender = request.form.get("gender")
        hobby_list = request.form.getlist("hobbit")
        city = request.form.get("city")
        skill_list = request.form.getlist("goodAt")
        more = request.form.get("more")

        print("user:{}\n……more:{}\n".format(user, more))
        # 将用户信息写入文件中实现注册、写入到excel中实现注册、写入到数据库中实现注册

        return "注册成功"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        print(request.form)
        user = request.form.get("username")
        password = request.form.get("password")
        print("user is : {} and password is {}".format(user, password))
        return "登录成功"


@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


# @app.route("/do/reg", methods=["GET"])
# def do_register():
#     # 接受到数据
#     # 给用户返回结果
#     print(request.args)
#     return "注册成功"
#
#
# @app.route("/post/reg", methods=["POST"])
# def post_register():
#     # 接受到数据
#     # 给用户返回结果
#     print(request.form)
#     user = request.form.get("user")
#     pwd = request.form.get("pwd")
#     gender = request.form.get("gender")
#     hobby_list = request.form.getlist("hobbit")
#     city = request.form.get("city")
#     skill_list = request.form.getlist("goodAt")
#     more = request.form.get("more")
#
#     print("user:{}\n……more:{}\n".format(user, more))
#     # 将用户信息写入文件中实现注册、写入到excel中实现注册、写入到数据库中实现注册
#
#     return "注册成功"


if __name__ == '__main__':
    app.run()
