from django.conf.urls import url
from . import views

app_name = 'wishList'

urlpatterns = [
    url(r'$', views.wishList_detail, name='home'),
    url(r'^update/$', views.wishList_update, name='update'),
    # url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'), ^login/$
]
