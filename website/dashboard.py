from .models import *
from django.shortcuts import render
from djg400.models import *
from blogs.models import Blog
from django.contrib.auth.decorators import login_required


@login_required(login_url='/account/signin/')
def dashboard(request):
    pages = []
    home_page = HomePage.objects.first()
    about_us_page = About.objects.first()
    contact_us_page = Contact.objects.first()
    contact_us_page = Track.objects.first()
    context = {
        "title_tag": "Dashboard",
        "newsletters": Newsletter.objects.order_by("-pk"),
        "contacts": Contact.objects.order_by("-pk"),
        "blogs": Blog.objects.order_by("-pk"),
        "remixes": Track.objects.order_by("-pk"),
    }
    return render(request, "dashboard.html", context)
