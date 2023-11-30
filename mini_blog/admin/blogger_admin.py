from django.contrib import admin
from mini_blog.models import Blogger


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    pass