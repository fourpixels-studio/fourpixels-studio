from django.shortcuts import render, get_object_or_404
from .models import Project
from website.get_items import get_projects
from blogs.utils import update_views


def projects_list(request):
    context = {
        'title_tag': "Projects",
        'projects': get_projects(),
    }
    return render(request, 'projects_list.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
        'title_tag': project.name,
        'meta_thumbnail': project.logo.url,
        'meta_keywords': project.category,
        'meta_description': project.description,
        'projects': get_projects(),
    }
    update_views(request, project)
    return render(request, 'project_detail.html', context)
