"""Project_django_app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import Project_django_app1.views as views
from django.contrib import admin
from django.urls import path, re_path

"""
    浏览器向服务器发起http get请求，django收到请求后执行视图类的as_view方法，该方法会
    返回在类视图中定义的get方法，然后对get请求进行处理
"""
urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.Home.as_view(), name="home"),
    path("personal/<int:id>", views.personal),
    re_path("personal/(\d+).html", views.personal),
    path("arithmetic/", views.arithmetic),
    path("greetings/", views.Greetings.as_view(greetings="Hello Python")),
    path("html/", views.Html.as_view()),
    path("json/", views.Json.as_view()),
    path("download/<path:file_path>", views.file_download, name="file_download"),
    # path("html5/", views.Html5.as_view()),
    path("html5/<label>/", views.Html5.as_view(), name="html5"),
    # 新增代码，在url中使用正则表达式
    re_path("blog/(\d+).html", views.blog),

]

