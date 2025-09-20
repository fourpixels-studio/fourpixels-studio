import json
from django.shortcuts import render
from blogs.models import Blog
from projects.models import Project
from .models import HomePage, About, Contact
from django.contrib.auth.decorators import login_required


@login_required(login_url='/account/login/')
def dashboard(request):
    projects = Project.objects.all()
    projects_data = json.dumps([
        {"name": project.get_short_name, "get_hit_count": project.get_hit_count}
        for project in projects
    ])

    context = {
        "title_tag": "Dashboard",
        "contacts": Contact.objects.order_by("-pk")[:5],
        "contacts_count": Contact.objects.count(),
        "blogs": Blog.objects.order_by("-pk"),
        "projects": projects,
        "home": HomePage.objects.first(),
        "about": About.objects.first(),
        "contact_page": Contact.objects.first(),
        "projects_data": projects_data,
    }
    return render(request, "dashboard.html", context)
