from django.shortcuts import render

def page_no_found(request):
    return render(request, 'erro.html', {'erro': 404, 'info': '别迷失了方向'})


def page_erro(request):
    return render(request, 'erro.html', {'erro': 500, 'info': '服务器挂掉了'})


def permission_denied(request):
    return render(request, 'erro.html', {'erro': 403, 'info': '服务器不能处理此请求'})