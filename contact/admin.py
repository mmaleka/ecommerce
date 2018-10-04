from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'message', 'created']

    list_filter = ['first_name', 'last_name', 'created']


admin.site.register(Contact, ContactAdmin)
