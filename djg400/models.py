from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Track(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    artist = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    cover = models.ImageField(blank=True, null=True)
    landscape_cover = models.ImageField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    video_download_link = models.TextField(blank=True, null=True)
    audio_download_link = models.TextField(blank=True, null=True)
    audio_download_count = models.PositiveIntegerField(
        default=0, blank=True, null=True)
    video_download_count = models.PositiveIntegerField(
        default=0, blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def get_url(self):
        return reverse("remix_detail", kwargs={
            "slug": self.slug,
        })


class Comment(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name} | {self.content[:100]} | {self.date}'
