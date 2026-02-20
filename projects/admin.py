from django.contrib import admin
from .models import Category, Project, ProjectMedia
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Category)
admin.site.register(ProjectMedia)

class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Project, ProjectAdmin)
