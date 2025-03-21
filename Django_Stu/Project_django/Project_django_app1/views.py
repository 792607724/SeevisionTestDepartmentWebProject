import os.path

from django.http import HttpResponse, JsonResponse, Http404, FileResponse, HttpResponseRedirect, \
    HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


# Create your views here.
#
class Home(View):

    def get(self, request):
        return render(request, 'home.html')


def personal(request, id):
    if request.method == "GET":
        return HttpResponse(str(id))


class Greetings(View):
    greetings = "Hello Django"

    def get(self, request):
        return HttpResponse(self.greetings)


class Json(View):
    def get(self, request):
        data = {"author": "Guangtao"}
        # # 响应数据中包含非ASCII字符，需要将ensure_ascii设置为False
        # json_data = json.dumps(data, ensure_ascii=False)
        # # 通过HttpResponse的content_type参数来指定MIME类型
        # return HttpResponse(json_data, content_type="application/json")

        # 也可以直接通过JsonResponse来响应Json格式的数据
        return JsonResponse(data, json_dumps_params={"ensure_ascii": False})


# 新增arithmetic视图
def arithmetic(request):
    """
        获取url中查询参数action：+-*/（加减乘除）
    """
    action = request.GET.get('action', "+")

    """
        获取url中的查询参数a和b，作为左右操作数
    """
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))

    commands = {"+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
                "/": lambda x, y: x / y, }
    if action == "/" and b == 0:
        result = 0
    else:
        result = commands.get(action, lambda x, y: 0)(b, a)
    return HttpResponse(str(result))


def file_download(request, file_path):
    file_path = "./Project_django_app1/download/" + file_path
    print(os.path.basename)
    ext = os.path.basename(file_path).split(".")[-1].lower()
    print("ext: {}".format(ext))
    print("file_path: {}".format(file_path))
    print("os.path: {}".format(os.path.exists(file_path)))
    if ext in ["txt", "dox", "doxs", "xlsx"]:
        try:
            response = FileResponse(open(file_path, "rb"))
            response["Content-Type"] = "application/octet-stream"
            response["Content-Disposition"] = "attachment; filename=" + os.path.basename(file_path)
            return response
        except FileNotFoundError:
            raise Http404("文件未找到")


"""
    临时重定向：
    302：对于Get、Head等幂等请求，会根据服务端响应Location字段中的url重新发起请求
    对于Post请求，大部分浏览器会将请求方式改为Get
    307：对于Get、Head等幂等请求，会根据服务端响应的Location字段中的url重新发起请求
    对于Post请求，会询问客户端是否对新url再次发起Post请求
    
    永久重定向：
    301：对于Get、Head等幂等请求，会根据服务端响应的Location字段中的url重新发起请求
    对于Post请求，部分浏览器会将请求方式改为Get
"""


class Html(View):
    title = "根据客户端的查询请求来响应不同的html"

    def get(self, request):
        # # 临时重定向
        # # 直接传递硬编码的url
        # return HttpResponseRedirect("/html5/")

        # # 永久重定向
        # # 直接传递完整的url
        # return HttpResponsePermanentRedirect("http://127.0.0.1:8080/html5/")

        # # 根据需求，进行临时重定向或者永久重定向
        # return redirect("/html5/", permanent=True)

        # 通过reverse反向解析并传递参数
        print("==================================")
        html5_url = reverse("html5", kwargs={"label": "article"})
        print("html5_url: {}".format(html5_url))
        return HttpResponseRedirect(html5_url)


class Html5(View):
    title = "根据客户端的查询请求来响应不同的html"

    def get(self, request, label):
        html5_url = reverse("html5", kwargs={"label": "article"})
        print("html5_url: {}".format(html5_url))
        """
            获取查询参数label，表示html标签，获取查询参数content，表示标签中的内容
        """
        # label = request.GET.get("label", "h1")
        content = request.GET.get("content", "Hello Django")
        html = ("<html><head><title>{0}</title></head><{1}>{2}</{1}></html>"
                .format(self.title, label, content))
        return HttpResponse(html)


def blog(request, page_id):
    if request.method == "GET":
        return render(request, "blog.html", {"page_id": page_id})
