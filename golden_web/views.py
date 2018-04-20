from django.shortcuts import render

# Create your views here.

# 主页
def index(request):
    return render(request, 'golden_web/index.html')

# 所有数据中心
def data_center(request):
    return render(request, 'golden_web/dataCenter.html')

# 数据中心详情
def show_data(request, dcname):
    return render(request, 'golden_web/datacenter/%s.html' % dcname)

# 服务体系
def service_system(request, name):
    return render(request, 'golden_web/fuwutixi/%s.html' % name)

# 资源方案
def resource(request, name):
    return render(request, 'golden_web/zyfa/%s.html' % name)

def corporation(request):
    return render(request, 'golden_web/corporation.html')

# 百度地图
def baidu_map(request):
    return render(request, 'baiduMap.html')