from django.contrib import admin

from .models import ViewsCount

# Register your models here.

class ProductViewsCountAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_address', 'address', 'user', 'product', 'views_count', 'time_stamp']
    list_filter = ['time_stamp', 'user', 'product']


admin.site.register(ViewsCount, ProductViewsCountAdmin)
