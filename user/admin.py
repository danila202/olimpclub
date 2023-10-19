from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class AdminUser(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','sport_section','position']
    list_filter = ['sport_section']
    fields = ['first_name', 'last_name','email','sport_section','position']


