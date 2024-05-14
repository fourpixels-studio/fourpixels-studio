from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    website_link = models.TextField(blank=True, null=True)
    link_name = models.CharField(max_length=40, blank=True, null=True)
    blog_link = models.TextField(blank=True, null=True)
    app_link = models.TextField(blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_website_url(self):
        return self.website_link
