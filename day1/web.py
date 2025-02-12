# coding = utf8
import sys

sys.path.append("../../")
import os
from flask import Flask, render_template

os.path.abspath(".")

"""
    @Project:SeevisionTestDepartmentWebProject
    @File:web.py
    @Author:十二点前要睡觉
    @Date:2025/2/9 20:21
"""

app = Flask(__name__)


# print(__name__)

# 创建了网址 /show/info 和 函数index 的对应关系
# 以后用户在浏览器访问 /show/info，网站自动执行 index
@app.route("/show/info")
def index():
    # return "中<h1>国</h1><span style='color:red;'>联通</span>"
    # Flask 内部会自动打开这个文件，并读取内容，将内容给用户返回
    # 默认：去当前项目目录的templates文件夹去找
    return render_template("index.html")


@app.route("/get/news")
def get_news():
    return render_template("get_news.html")


if __name__ == '__main__':
    app.run()
