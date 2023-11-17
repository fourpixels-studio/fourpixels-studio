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
    tags = MessageTag.objects.all()
    about_object = AboutSection.objects.all()
    
    tag1 = tags[0].tag
    tag2 = tags[1].tag
    
    about_our_story = about_object[0].content_1
    about_our_mission = about_object[0].content_2
    about_our_vision = about_object[0].content_3
    about_our_team = about_object[0].content_4
    
    services_masters = about_object[1].content_1
    services_websites = about_object[1].content_2
    services_graphic_design = about_object[1].content_3
    services_motion_graphics = about_object[1].content_4
    
    testimonial_form = TestimonialForm(initial={'post_testimonial': True})
    
    # Testimonials
    all_testimonials = Testimonial.objects.order_by('-pk')
    testimonials = [testimonial for testimonial in all_testimonials if testimonial.post_testimonial]

    if request.method == 'POST':
        testimonial_form = TestimonialForm(request.POST)
        if testimonial_form.is_valid():
            testimonial_form.save()
            name = testimonial_form.cleaned_data.get('name')
            department = testimonial_form.cleaned_data.get('department')
            testimonial = testimonial_form.cleaned_data.get('testimonial')
            print(
                f"==== NEW TESTIMONIAL ====\n\nFrom: {name}\nCompany/Department: {department}\nTestimonial: {testimonial}\n\n==== END OF NEW TESTIMONIAL ====")
            messages.success(
                request, ('Thank you!'))
            return redirect('about')
        else:
            testimonial_form = TestimonialForm(initial={'post_testimonial': True})

    
    context = {
        'page_name': page_name,
        'tag1': tag1,
        'tag2': tag2,
        'about_our_story': about_our_story, 
        'about_our_mission': about_our_mission, 
        'about_our_vision': about_our_vision, 
        'about_our_team': about_our_team, 
        'services_masters': services_masters,
        'services_websites': services_websites,
        'services_graphic_design': services_graphic_design,
        'services_motion_graphics': services_motion_graphics,
        'testimonial_form': testimonial_form,
        'testimonials': testimonials,
    }
    return render(request, 'about.html', context)

def contact(request):
    page_name = "- Contact Us"
    tags = MessageTag.objects.all()
    about_object = AboutSection.objects.all()
    
    tag1 = tags[0].tag
    tag2 = tags[1].tag
    
    about_our_story = about_object[0].content_1
    about_our_mission = about_object[0].content_2
    about_our_vision = about_object[0].content_3
    about_our_team = about_object[0].content_4
    
    services_masters = about_object[1].content_1
    services_websites = about_object[1].content_2
    services_graphic_design = about_object[1].content_3
    services_motion_graphics = about_object[1].content_4
    
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            name = contact_form.cleaned_data.get('name')
            message = contact_form.cleaned_data.get('message')
            email = contact_form.cleaned_data.get('email')
            phone_number = contact_form.cleaned_data.get('phone_number')
            user = contact_form.cleaned_data.get('user')
            print(
                f"==== NEW CONTACT ====\n\nFrom: {name} - User: {user}\nMessage: {message}\nEmail: {email}\nPhone Number: {phone_number}\n\n==== END OF NEW CONTACT ====")
            messages.success(
                request, (f'Thank you {name}! We have received your message!'))
            return redirect('contact')
        else:
            contact_form = ContactForm()
    # Contact Logic End

    # Testimonials
    testimonials = Testimonial.objects.order_by('-pk')
    
    context = {
        'page_name': page_name,
        'tag1': tag1,
        'tag2': tag2,
        'about_our_story': about_our_story, 
        'about_our_mission': about_our_mission, 
        'about_our_vision': about_our_vision, 
        'about_our_team': about_our_team, 
        'services_masters': services_masters,
        'services_websites': services_websites,
        'services_graphic_design': services_graphic_design,
        'services_motion_graphics': services_motion_graphics,
        'contact_form': contact_form,
        'testimonials': testimonials,
    }
    return render(request, 'contact.html', context)

def services(request):
    page_name = "- Services"
    tags = MessageTag.objects.all()
    about_object = AboutSection.objects.all()
    
    tag1 = tags[0].tag
    tag2 = tags[1].tag
    
    about_our_story = about_object[0].content_1
    about_our_mission = about_object[0].content_2
    about_our_vision = about_object[0].content_3
    about_our_team = about_object[0].content_4
    
    services_masters = about_object[1].content_1
    services_websites = about_object[1].content_2
    services_graphic_design = about_object[1].content_3
    services_motion_graphics = about_object[1].content_4
    
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            name = contact_form.cleaned_data.get('name')
            message = contact_form.cleaned_data.get('message')
            email = contact_form.cleaned_data.get('email')
            phone_number = contact_form.cleaned_data.get('phone_number')
            user = contact_form.cleaned_data.get('user')
            print(
                f"==== NEW CONTACT ====\n\nFrom: {name} - User: {user}\nMessage: {message}\nEmail: {email}\nPhone Number: {phone_number}\n\n==== END OF NEW CONTACT ====")
            messages.success(
                request, (f'Thank you {name}! We have received your message!'))
            return redirect('contact')
        else:
            contact_form = ContactForm()
    # Contact Logic End

    # Testimonials
    testimonials = Testimonial.objects.order_by('-pk')
    
    context = {
        'page_name': page_name,
        'tag1': tag1,
        'tag2': tag2,
        'about_our_story': about_our_story, 
        'about_our_mission': about_our_mission, 
        'about_our_vision': about_our_vision, 
        'about_our_team': about_our_team, 
        'services_masters': services_masters,
        'services_websites': services_websites,
        'services_graphic_design': services_graphic_design,
        'services_motion_graphics': services_motion_graphics,
        'contact_form': contact_form,
        'testimonials': testimonials,
    }
    return render(request, 'services.html', context)


def get_previous_and_next_blog(blog):
    blogs = Blog.objects.order_by('-pub_date')
    blog_index = list(blogs).index(blog)

    previous_blog = None
    next_blog = None

    if blog_index > 0:
        previous_blog = blogs[blog_index - 1]

    if blog_index < len(blogs) - 1:
        next_blog = blogs[blog_index + 1]

    return previous_blog, next_blog

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    previous_blog, next_blog = get_previous_and_next_blog(blog)

    context = {
        'page_name': f"- {blog.title}",
        'blog': blog,
        'tags': [item.strip() for item in blog.tags.split(',') if item.strip()],
        'previous_blog': previous_blog,
        'next_blog': next_blog,
    }

    return render(request, 'blog_detail.html', context)

def blog_list(request):
    recent_blogs = Blog.objects.order_by('-pk')
    page_name = f"- Blogs"
    context = {
        'page_name': page_name,
        'recent_blogs': recent_blogs,
    }
    return render(request, 'blog_list.html', context)


def newsletter(request):
    page_name = "- Newsletter"

    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            email = newsletter_form.cleaned_data.get('email')
            if Newsletter.objects.filter(email=email).exists():
                print(f"The email: {email} Already exists.")
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