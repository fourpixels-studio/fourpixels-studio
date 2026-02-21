from django.contrib import admin
from .models import Blog, Category
from django_summernote.admin import SummernoteModelAdmin


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
