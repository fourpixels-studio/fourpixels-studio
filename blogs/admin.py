from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Blog


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Blog, BlogAdmin)
