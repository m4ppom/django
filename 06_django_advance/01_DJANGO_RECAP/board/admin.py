from django.contrib import admin
from .models import Article

class ArticleModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'

admin.site.register(Article, ArticleModelAdmin)
