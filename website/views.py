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
    blogs = Blog.objects.all()
    context = {
        'page_name': page_name,
        'blogs': blogs,
    }
    return render(request, 'index.html', context)

def about(request):
    page_name = "- About Us"
    context = {
        'page_name': page_name,
    }
    return render(request, 'about.html', context)

def blog_detail(request, slug):
    recent_blogs = Blog.objects.order_by('-pk')
    blog = get_object_or_404(Blog, slug=slug)
    page_name = f"- {blog.title}"
    tags = [
        item.strip()
        for item in blog.tags.split(',')
        if item.strip()
    ]
    context = {
        'page_name': page_name,
        'recent_blogs': recent_blogs,
        'blog': blog,
        'tags': tags,
    }
    return render(request, 'blog.html', context)