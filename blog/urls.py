from django.conf.urls import url
from . import views
from django.urls import include



app_name = 'blog'

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # url(r'^(?P<category_slug>[-\w]+)/$', views.post_list_by_catergory, name='post_list_by_catergory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
]
