from blogs.models import Blog
from django.contrib import messages
from blogs.utils import update_views
from seo_management.models import SEO
from django.shortcuts import render, redirect
from .email import send_contact_email, send_testimonial_email
from .forms import NewsletterForm, TestimonialForm, ContactForm
from .get_items import get_testimonials, get_recent_projects, get_project_highlights
from .models import Testimonial, Service, About, Accordion, Contact, HomePage, Newsletter

seo = SEO.objects.get(pk=1)


def index(request):
    homepage_data = HomePage.objects.first()
    context = {
        'title_tag': seo.title_tag,
        'contact_form': ContactForm(),
        'homepage_data': homepage_data,
        'about': About.objects.first(),
        'services': Service.objects.all(),
        'meta_keywords': seo.meta_keywords,
        'testimonials': get_testimonials(),
        'blogs': Blog.objects.order_by("-pk"),
        'meta_thumbnail': seo.meta_thumbnail.url,
        'meta_description': seo.meta_description,
        'get_recent_projects': get_recent_projects()[:6],
        'get_project_highlights': get_project_highlights()[:6],
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
        'meta_thumbnail': seo.meta_thumbnail.url,
    }
    update_views(request, about_data)
    return render(request, 'about.html', context)



def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data.get('name')
            email = contact_form.cleaned_data.get('email')
            message = contact_form.cleaned_data.get('message')
            phone_number = contact_form.cleaned_data.get('phone_number')
            contact_form.save()
            send_contact_email(name, email, phone_number, message)
            messages.success(request, str(f'Thank you {name}! We have received your message!'))
            return redirect('index')
        else:
            if 'captcha' in contact_form.errors:
                messages.error(request, "Please complete the captcha.")
            else:
                for field, errors in contact_form.errors.items():
                    for error in errors:
                        messages.error(request, error)
            contact_form = ContactForm()

    context = {
        'title_tag': "Contact Us",
        'contact_form': contact_form,
        'testimonials': get_testimonials(),
        'meta_thumbnail': seo.meta_thumbnail.url,
    }
    return render(request, 'contact.html', context)


def newsletter(request):
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            email = newsletter_form.cleaned_data.get('email')
            if Newsletter.objects.filter(email=email).exists():
                messages.info(request, "Breaking news: Your email is such a trendsetter; it subscribed before subscribing was cool. You're not just on the list; you're the list! 🌟📨")
            else:
                newsletter_form.save()
                messages.success(request, "By hitting that subscribe button, you've just upgraded your inbox to the penthouse suite – 400 miles above the email riffraff. Get ready for a newsletter that's cooler than a polar bear in sunglasses. 😎❄️📧")
            return redirect('index')
        else:
            for field, errors in newsletter_form.errors.items():
                for error in errors:
                    messages.error(request, error)
            newsletter_form = NewsletterForm()

    context = {
        'title_tag': "Newsletter",
        'newsletter_form': newsletter_form,
        'meta_thumbnail': seo.meta_thumbnail.url,
    }

    return render(request, 'newsletter.html', context)


def error_404(request, exception):
    context = {
        'title_tag': "Error 404",
        'meta_thumbnail': seo.meta_thumbnail.url,
    }
    return render(request, '404.html', context)


def error_500(request):
    context = {
        'title_tag': "Error 505",
        'meta_thumbnail': seo.meta_thumbnail.url,
    }
    return render(request, '500.html', context)


def testimonials_list(request):
    context = {
        'title_tag': "Testimonials",
        'testimonials': get_testimonials(),
        'meta_thumbnail': seo.meta_thumbnail.url,
    }
    return render(request, 'testimonials_list.html', context)


def help(request):
    context = {
        'title_tag': "Help",
        'meta_thumbnail': seo.meta_thumbnail.url,
    }
    return render(request, 'help.html', context)


def submit_testimonial(request):
    if request.method == 'POST':
        testimonial_form = TestimonialForm(request.POST, request.FILES)
        if testimonial_form.is_valid():
            testimonial_form.save()
            message_1 = str("We appreciate you taking the time to share your experience. Your testimonial has been successfully submitted and will be reviewed shortly.")
            message_2 = str("If approved, your testimonial will be published on our website. We value your feedback and thank you for your support!")
            email = testimonial_form.cleaned_data.get('email')
            name = testimonial_form.cleaned_data.get('name')
            if email:
                send_testimonial_email(email, name, message_1, message_1)
            context = {
                "title_tag": "Thank You For The Testimonial",
                "message_1": message_1,
                "message_2": message_2,
                'meta_description': seo.meta_description,
                'meta_keywords': seo.meta_keywords,
                'meta_thumbnail': seo.meta_thumbnail.url,
            }
            return render(request, 'success.html', context)
        else:
            for field, errors in testimonial_form.errors.items():
                for error in errors:
                    messages.error(request, error)
            testimonial_form = TestimonialForm()

    return render(request, 'success.html', {'testimonial_form': testimonial_form})
    
    
def success(request):
    context = {
        'title_tag': "Success",
        'meta_thumbnail': seo.meta_thumbnail.url,
    }
    return render(request, 'success.html', context)
