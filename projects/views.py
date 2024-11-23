from .models import Project
from blogs.utils import update_views
from website.forms import TestimonialForm
from website.get_items import get_recent_projects
from django.shortcuts import render, get_object_or_404


def projects_list(request):
    context = {
        'title_tag': "Projects",
        'projects': get_recent_projects(),
        'meta_description': "Explore our portfolio of innovative websites and web applications. Discover how we help freelancers, creative professionals, and small businesses elevate their online presence with custom designs, user-centric development, and ongoing support.",
    }
    return render(request, 'projects_list.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
        'title_tag': project.name,
        'meta_keywords': project.category,
        'projects': get_recent_projects(),
        'meta_thumbnail': project.logo.url,
        'testimonial_form': TestimonialForm(),
        'meta_description': project.description,
    }
    update_views(request, project)
    return render(request, 'project_detail.html', context)
