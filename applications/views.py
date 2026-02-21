from .models import Application
from django.shortcuts import render


def applications_list(request):
    context = {
        "title_tag": "Applications",
        "applications": Application.objects.all(),
    }
    return render(request, 'applications_list.html', context)
