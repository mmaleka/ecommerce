from django.contrib import admin

from .models import ViewsCount, RegisterCount, CartItemsCount, PostViewsCount

# Register your models here.

class ProductViewsCountAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_address', 'address', 'user', 'product', 'views_count', 'time_stamp', 'updated_at']
    list_filter = ['time_stamp', 'user', 'product']

admin.site.register(ViewsCount, ProductViewsCountAdmin)



class PostViewsCountAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_address', 'address', 'user', 'post', 'views_count', 'time_stamp', 'updated_at']
    list_filter = ['time_stamp', 'user', 'post']

admin.site.register(PostViewsCount, PostViewsCountAdmin)



class RegisterViewsCountAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_address', 'address', 'views_count', 'time_stamp', 'updated_at']
    list_filter = ['time_stamp']

admin.site.register(RegisterCount, RegisterViewsCountAdmin)



class CartItemsCountViewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_address', 'address', 'user', 'cartItems', 'views_count', 'time_stamp', 'updated_at']
    list_filter = ['time_stamp', 'user', 'cartItems']

admin.site.register(CartItemsCount, CartItemsCountViewsAdmin)
