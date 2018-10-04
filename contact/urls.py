from django.conf.urls import url
from . import views

app_name = 'contact'

urlpatterns = [
    url(r'', views.contact_view, name='contact_view'),
]
