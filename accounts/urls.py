from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^register_view/$', views.register_view, name='register_view'),
    url(r'^logout/$', views.logout_view, name="logout_view"),
    url(r'^profile_view/$', views.profile_view, name="profile_view"),
]
