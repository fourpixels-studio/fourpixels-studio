from django.db import models
from django.utils.text import slugify
from django.utils.dateformat import DateFormat
from django.contrib.auth.models import User

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
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} - Published On: {self.pub_date.strftime('%A, %B %d, %Y')}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
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