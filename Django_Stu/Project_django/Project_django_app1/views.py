import os.path

from django.http import HttpResponse, JsonResponse, Http404, FileResponse
from django.shortcuts import render
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


class Html(View):
    title = "根据客户端的查询请求来响应不同的html"

    def get(self, request):
        """
            获取查询参数label，表示html标签，获取查询参数content，表示标签中的内容
        """
        label = request.GET.get("label", "h1")
        content = request.GET.get("content", "Hello Django")
        html = ("<html><head><title>{0}</title></head><{1}>{2}</{1}></html>"
                .format(self.title, label, content))
        return HttpResponse(html)


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
