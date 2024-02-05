from django.db import models
from django.utils.text import slugify
from django.utils.dateformat import DateFormat
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    paragraph_1 = models.TextField(blank=True, null=True)
    paragraph_2 = models.TextField(blank=True, null=True)
    paragraph_3 = models.TextField(blank=True, null=True)
    conclusion = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    blog_image = models.ImageField(default="blog.jpg", blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} - Published On: {self.pub_date.strftime('%A, %B %d, %Y')}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    @property
    def get_blog_url(self):
        return f"www.4ourpixels.com/{self.slug}/"
    
    @property
    def get_og_image_url(self):
        if self.cover_image:
            return self.cover_image.url
        else:
            default_image_path = 'images/logo.jpg'
            return static(default_image_path)
    @property
    def get_url(self):
        return reverse("blog_detail", kwargs={
            "slug": self.slug,
        })
        
class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(default='', null=True, blank=True)

    profile_pic = models.ImageField(
        null=True,
        blank=True,
        upload_to="customer-images/",
        default='image.jpg',
    )

    def __str__(self):
        return self.username


def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(
            user=instance, name=instance.username, email=instance.email)


models.signals.post_save.connect(create_customer, sender=User)

class Newsletter(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.email

# About Us

class AboutSection(models.Model):
    question = models.CharField(max_length=255, blank=True, null=True)
    content_1 = models.TextField(blank=True, null=True)
    content_2 = models.TextField(blank=True, null=True)
    content_3 = models.TextField(blank=True, null=True)
    content_4 = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.question}"

class MessageTag(models.Model):
    tag = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.tag

class Testimonial(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    testimonial = models.TextField(blank=True, null=True)
    post_testimonial = models.BooleanField(default=True, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(default="testimonial.jpg", upload_to="testimonial-images/", blank=True, null=True)
    def __str__(self):
        return f"{self.name}' Testimonial - Posted On: {self.pub_date.strftime('%A, %B %d, %Y')}"

class Contact(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(default='', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return f'Lead Name: {self.name}'
    
# Merchandise Start
class Merchandise(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    image = models.ImageField(default="merchandise.jpg", upload_to="merchandise-images/", blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
# Client Portoflio End
class ClientPortoflio(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    website_link = models.TextField(blank=True, null=True)
    link_name = models.CharField(max_length=40,blank=True, null=True)
    blog_link = models.TextField(blank=True, null=True)
    app_link = models.TextField(blank=True, null=True)
    
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.company_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.company_name)
        super().save(*args, **kwargs)
        
    def get_website_url(self):
        return self.website_link
# Client Portoflio End