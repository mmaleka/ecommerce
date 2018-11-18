from django.contrib import admin
from .models import AddBanner, AddBannerImage

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class AddBannerImageInline(admin.TabularInline):
    model = AddBannerImage
    extra = 3

class AddBannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at', 'add_is_active']
    list_filter = ['name', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [AddBannerImageInline]


admin.site.register(AddBanner, AddBannerAdmin)
