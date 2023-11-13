from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import *
from django.contrib import messages
from .models import *
from django.http import JsonResponse
import json
import datetime
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


def newsletter(request):
    page_name = "- Newsletter"

    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            email = newsletter_form.cleaned_data.get('email')
            if Newsletter.objects.filter(email=email).exists():
                messages.info(
                    request, "Breaking news: Your email is such a trendsetter; it subscribed before subscribing was cool. You're not just on the list; you're the list! 🌟📨")
            else:
                newsletter_form.save()
                print(f"New email subscription: \n{email}")
                messages.success(
                    request, "By hitting that subscribe button, you've just upgraded your inbox to the penthouse suite – 400 miles above the email riffraff. Get ready for a newsletter that's cooler than a polar bear in sunglasses. 😎❄️📧")
            return redirect('index')
    else:
        newsletter_form = NewsletterForm()

    context = {
        'page_name': page_name,
        'newsletter_form': newsletter_form,
    }

    return render(request, 'newsletter.html', context)