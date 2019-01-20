from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'slug', 'created_at', 'updated_at']
    list_filter = ['author', 'title', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
