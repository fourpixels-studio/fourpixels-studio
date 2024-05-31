from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from .email import send_contact_email
from .get_items import get_testimonials, get_projects
from seo_management.models import SEO
from blogs.utils import update_views
from blogs.models import Blog


def index(request):
    homepage_data = HomePage.objects.first()
    seo = SEO.objects.get(pk=1)
    context = {
        'title_tag': seo.title_tag,
        'meta_description': seo.meta_description,
        'meta_keywords': seo.meta_keywords,
        'meta_thumbnail': seo.meta_thumbnail.url,
        'blogs': Blog.objects.all(),
        'projects': get_projects(),
        'homepage_data': homepage_data,
        'services': Service.objects.all(),
    }
    update_views(request, homepage_data)
    return render(request, 'index.html', context)


def about(request):
    about_data = About.objects.first()
    context = {
        'title_tag': "About Us",
        'about_data': about_data,
        'homepage_data': HomePage.objects.first(),
        'accordions': Accordion.objects.all(),
    }
    update_views(request, about_data)
    return render(request, 'about.html', context)


def contact(request):
    contact_form = ContactForm()
    contact_model = Contact.objects.first()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            email = contact_form.cleaned_data.get('email')
            contact_form.save()
            name = contact_form.cleaned_data.get('name')
            message = contact_form.cleaned_data.get('message')
            email = contact_form.cleaned_data.get('email')
            phone_number = contact_form.cleaned_data.get('phone_number')
            send_contact_email(name, email, phone_number, message)
            messages.success(
                request, (f'Thank you {name}! We have received your message!'))
            return redirect('contact')
        else:
            contact_form = ContactForm()

    context = {
        'title_tag': "Contact Us",
        'contact_form': contact_form,
        'contact_model': contact_model,
        'testimonials': get_testimonials(),
    }
    update_views(request, contact_model)
    return render(request, 'contact.html', context)


def newsletter(request):
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            email = newsletter_form.cleaned_data.get('email')
            if Newsletter.objects.filter(email=email).exists():
                messages.info(
                    request, "Breaking news: Your email is such a trendsetter; it subscribed before subscribing was cool. You're not just on the list; you're the list! 🌟📨")
            else:
                newsletter_form.save()
                messages.success(
                    request, "By hitting that subscribe button, you've just upgraded your inbox to the penthouse suite – 400 miles above the email riffraff. Get ready for a newsletter that's cooler than a polar bear in sunglasses. 😎❄️📧")
            return redirect('index')
    else:
        newsletter_form = NewsletterForm()

    context = {
        'title_tag': "Newsletter",
        'newsletter_form': newsletter_form,
    }

    return render(request, 'newsletter.html', context)


def error_404(request, exception):
    context = {
        'title_tag': "Error 404",
    }
    return render(request, '404.html', context)


def error_500(request):
    context = {
        'title_tag': "Error 505",
    }
    return render(request, '500.html', context)


def testimonials_list(request):
    context = {
        'title_tag': "Testimonials",
        'testimonials': get_testimonials(),
    }
    return render(request, 'testimonials_list.html', context)


def help(request):
    context = {
        'title_tag': "Help",
    }
    return render(request, 'help.html', context)
