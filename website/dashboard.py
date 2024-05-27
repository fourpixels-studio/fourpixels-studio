from .models import *
from django.shortcuts import render
from djg400.models import *


def dashboard(request):
    context = {
        "title_tag": "Dashboard",
        "newsletters": Newsletter.objects.order_by("-pk"),
        "contacts": Contact.objects.order_by("-pk"),
        "blogs": Blog.objects.order_by("-pk"),
        "remixes": Track.objects.order_by("-pk"),
    }
    return render(request, "dashboard.html", context)
