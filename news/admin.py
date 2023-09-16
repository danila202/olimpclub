from django.contrib import admin
from .models import News


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ['title','author','publish','status']
    list_filter = ['publish','created','status','author']
    ordering = ['status','publish']
    search_fields = ['title', 'body']
