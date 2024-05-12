from django.shortcuts import render
from .models import Project


def projects_list(request):
    context = {
        'title_tag': "Projects",
        'projects': Project.objects.all(),
    }
    return render(request, 'projects_list.html', context)
