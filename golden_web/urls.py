from django.conf.urls import url
from golden_web import views
urlpatterns = [
    url(r'^$', view=views.index, name='index'),
    url(r'^dataCenter/$', view=views.data_center, name='data_center'),
    url(r'^show/(?P<dcname>\w+)/$', view=views.show_data, name='show_data'),
    url(r'^service/(?P<name>\w+)/$', view=views.service_system, name='service_system'),
    url(r'^resource/(?P<name>\w+)/$', view=views.resource, name='resource'),
    url(r'^corporation/$', view=views.corporation, name='corporation'),
    url(r'^baiduMap/$', view=views.baidu_map, name='baidumap'),
]