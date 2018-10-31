from django.conf.urls import url
from . import views
from django.urls import include

app_name = 'addBanner'

urlpatterns = [
    url(r'^$', views.AddBanner_list, name='AddBanner_list'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.AddBanner_detail, name='AddBanner_detail'),
]
