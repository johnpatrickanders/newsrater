from django.contrib import admin
from .models import Article, Rating

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['title', 'length', 'source']
        }),
        ('Date information', {
            'fields': ['pub_date'],
            'classes': ['collapse']
        }),
    ]

class RatingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['article', 'user', 'source']
        }),
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Rating, RatingAdmin)
