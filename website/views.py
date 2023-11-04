from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import *
# from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.conf import settings

def index(request):
    page_name = "- Masters of the Digital Realm"
    context = {
        'page_name', page_name
    }
    return render(request, 'index.html', context)

def about(request):
    page_name = "- About Us"
    context = {
        'page_name', page_name
    }
    return render(request, 'about.html', context)