
from .views import idc_list, idc_detail
from .views import idc_list_v2, idc_detail_v2
from .views import IdcList, IdcDetail
from .views import IdcListV4, IdcDetailV4
from .views import IdcListV5, IdcDetailV5

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r"^$", idc_list),
    url(r"^(?P<pk>[0-9]+)/$", idc_detail),
]

urlpatterns = [
    url(r"^$", idc_list_v2, name="idc_list"),
    url(r"^(?P<pk>[0-9]+)/$", idc_detail_v2, name="idc_detail"),
]

urlpatterns = [
    url(r"^$", IdcList.as_view(), name="idc_list"),
    url(r"^(?P<pk>[0-9]+)/$", IdcDetail.as_view(), name="idc_detail"),
]

urlpatterns = [
    url(r"^$", IdcListV4.as_view(), name="idc_list"),
    url(r"^(?P<pk>[0-9]+)/$", IdcDetailV4.as_view(), name="idc_detail"),
]

urlpatterns = [
    url(r"^$", IdcListV5.as_view(), name="idc_list"),
    url(r"^(?P<pk>[0-9]+)/$", IdcDetailV5.as_view(), name="idc_detail"),
]

################################### 版本6 ########################################
from . import views
idc_list = views.IdcListViewset.as_view({
    'get' : 'list',
    'post' : 'create',
})

idc_detail = views.IdcListViewset.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'delete' : 'destroy',
})
urlpatterns = [
    url(r"^$", idc_list, name="idc_list"),
    url(r"^(?P<pk>[0-9]+)/$", idc_detail, name="idc_detail"),
]

################################### 版本7 ########################################
from . import views
from rest_framework.routers import DefaultRouter


route = DefaultRouter()
route.register('idcs', views.IdcListViewsetV7)
urlpatterns = [
    url(r"^", include(route.urls))
]





# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])