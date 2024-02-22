from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.contrib import messages
from .models import *

# Email Logic Start
from django.core.mail import EmailMessage


# Image Compression Logic End
def index(request):
    title_tag = "Masters of the Digital Realm | Elevate Your Online Presence"
    meta_descriprion = "Masters of the digital realm, blending creativity and technology into mind-blowing experiences. Graphic gurus, web whisperers, and visual/audio virtuosos. Elevate your online presence with custom web/app development, stunning graphic design, mesmerizing digital art, and epic DJ services."
    meta_keywords = "digital realm, creativity, technology, website development, app development, graphic design, digital art, DJ services, online presence"
    blogs = Blog.objects.all()
    context = {
        'title_tag': title_tag,
        'blogs': blogs,
    }
    return render(request, 'index.html', context)

def about(request):
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
        'title_tag': "About Us",
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
            email = contact_form.cleaned_data.get('email')
            
            contact_form.save()
            name = contact_form.cleaned_data.get('name')
            message = contact_form.cleaned_data.get('message')
            email = contact_form.cleaned_data.get('email')
            phone_number = contact_form.cleaned_data.get('phone_number')
            user = contact_form.cleaned_data.get('user')
            print(
                f"==== NEW CONTACT ====\n\nFrom: {name} - User: {user}\nMessage: {message}\nEmail: {email}\nPhone Number: {phone_number}\n\n==== END OF NEW CONTACT ====")
            
            # Send mail utility start
            subject = 'Thank You for Reaching Out to Four Pixels'
            message = f"Hi {name},\n\nThank you for reaching out to Four Pixels! We're thrilled to receive your message and appreciate your interest in our creative studio.\n\nOur team is dedicated to transforming ideas into captivating digital experiences, and we're excited about the possibility of collaborating with you.\n\nWe have received your inquiry and will review it carefully. Expect to hear back from us soon with more information or to schedule a discussion about your project.\n\nIn the meantime, feel free to explore our portfolio to get a sense of our creative capabilities. If you have any additional information or specific details you'd like to share, please reply to this email, and we'll ensure it's factored into our conversation.\n\nThank you once again for considering Four Pixels. We look forward to the opportunity to create something extraordinary together.\n\nBest regards,\n\nMoses Bartena\nVisual Identity Designer\nFour Pixels Creative Studio\nhello@fourpixels.studio"
            from_email = 'hello@fourpixels.studio'
            recepient_list = [email]

            # Create an EmailMessage instance
            email_message = EmailMessage(
                subject,
                message,
                from_email,
                recepient_list,
            )
            email_message.send()
            # Send mail utility end
            
            messages.success(
                request, (f'Thank you {name}! We have received your message!'))
            return redirect('contact')
        else:
            contact_form = ContactForm()
    # Contact Logic End

    # Testimonials
    testimonials = Testimonial.objects.order_by('-pk')
    
    context = {
        'title_tag': "Contact Us",
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

# Services start
def services(request):
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
        'title_tag': "Services",
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

def services_web_development(request):
    about_object = AboutSection.objects.all()
    web_development_heading = about_object[2].question
    clients = ClientPortoflio.objects.all()

    # Testimonials
    testimonials = Testimonial.objects.order_by('-pk')
    
    context = {
        'title_tag': "Web & App Development Services",
        'clients': clients,
        'testimonials': testimonials,
        'web_development_heading': web_development_heading,
    }
    return render(request, 'services-web-development.html', context)
# Services end

# Blog Logic Start

# Function to get previous and next blog in the blog detail
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

# Function to render out blog details
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    meta_description = blog.meta_description
    meta_keywords = blog.meta_keywords
    
    previous_blog, next_blog = get_previous_and_next_blog(blog)

    context = {
        'title_tag': blog.title,
        'blog': blog,
        'tags': [item.strip() for item in blog.tags.split(',') if item.strip()],
        'previous_blog': previous_blog,
        'next_blog': next_blog,
        "meta_description": meta_description,
        "meta_keywords": meta_keywords,
    }

    return render(request, 'blog-detail.html', context)

# Function to render out all blogs
def blog_list(request):
    recent_blogs = Blog.objects.order_by('-pk')
    context = {
        'title_tag': "Blogs",
        'recent_blogs': recent_blogs,
    }
    return render(request, 'blog-list.html', context)

# Blog Logic End

# Newsletter blog Start
def newsletter(request):
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
        'title_tag': "Newsletter",
        'newsletter_form': newsletter_form,
    }

    return render(request, 'newsletter.html', context)
# Newsletter blog end

# DJ G400 Start
def djg400(request):
    merchandise = Merchandise.objects.order_by("-pk")
    context = {
        'title_tag': "DJ G400",
        'merchandise': merchandise,
    }
    return render(request, 'djg400.html', context)

# Merchandise
def merchandise(request):
    merchandise = Merchandise.objects.order_by("-pk")
    context = {
        'title_tag': "Merchandise",
        'merchandise': merchandise,
    }
    return render(request, 'merchandise.html', context)

# DJ G400 End

def downloadSuccess(request, pk):
    item = get_object_or_404(Object, pk=pk)
    item.download_count = item.download_count + 1
    item.save()
    
    context = {
        'title_tag': "Success!",
        'item': item,
    }
    return render(request, 'download-success.html', context)


def artworks(request):
    return render(request, 'artworks.html', {'title_tag': "Artworks"})


def error_404(request):
    context = {
        'title_tag': "Error 404",
    }
    return render(request,'404.html', context)

def error_500(request):
    context = {
        'title_tag': "Error 505",
    }
    return render(request,'500.html', context)