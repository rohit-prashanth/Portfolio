from django.contrib import admin
from .models import ContactMeTable


@admin.register(ContactMeTable)
class UserContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','info')
