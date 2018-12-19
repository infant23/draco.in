from django.contrib import admin

from .models import Article, Tag, Image, Comment

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Comment)