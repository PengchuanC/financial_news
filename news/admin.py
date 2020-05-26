from django.contrib import admin

# Register your models here.
from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'infopubldate', 'infopubltime', 'media', 'newscategory', 'infotitle', 'infoshorttitle',
        'abstract', 'content', 'author', 'linkaddress', 'category', 'infolevel',
    ]