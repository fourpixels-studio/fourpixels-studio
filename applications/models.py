from django.db import models
from django.urls import reverse
from django.conf import settings
from django_resized import ResizedImageField


class Application(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    link_name = models.CharField(max_length=100, blank=True, null=True)
    cover = models.ImageField(blank=True, null=True, upload_to="applications/")
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    meta_thumbnail = ResizedImageField(size=[1200, 630], crop=['middle', 'center'], quality=75, upload_to='thumbnails/', blank=True, null=True)
    img_md = ResizedImageField(size=[1280, 720], quality=95, upload_to='resized/', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.cover and (not self.meta_thumbnail or self.meta_thumbnail.name != f"{self.cover.name}"):
            self.cover.save(f"{self.cover.name}", self.cover, save=False)
            super().save(update_fields=['meta_thumbnail'])

        if self.cover and (not self.img_md or self.img_md.name != f"{self.cover.name}"):
            self.cover.save(f"{self.cover.name}", self.cover, save=False)
            super().save(update_fields=['img_md'])

    @property
    def get_url(self):
        if self.pk == 1:
            return reverse("image_compression")
        if self.pk == 2:
            return reverse("image_search")
        if self.pk == 3:
            return reverse("bloomberg_news_finder")
        if self.pk == 4:
            return reverse("qr_code_generator")
