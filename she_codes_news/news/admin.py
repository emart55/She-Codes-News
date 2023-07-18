from django.contrib import admin
from .models import NewsStory

class NewsStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')

admin.site.register(NewsStory, NewsStoryAdmin)
