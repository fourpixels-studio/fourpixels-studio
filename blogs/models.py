from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from hitcount.models import HitCount
from django.utils.text import slugify
from django_resized import ResizedImageField
from django.contrib.contenttypes.fields import GenericRelation


class Blog(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    paragraph_1 = models.TextField(blank=True, null=True)
    paragraph_2 = models.TextField(blank=True, null=True)
    paragraph_3 = models.TextField(blank=True, null=True)
    conclusion = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    cover = models.ImageField(blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    thumbnail = ResizedImageField(size=[1200, 630], crop=['middle', 'center'], quality=75, upload_to='thumbnails/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - Published On: {self.pub_date.strftime('%a, %b %d, %Y')}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def meta_url(self):
        return f"www.fourpixels.studio/blogs/{self.slug}/"

    @property
    def get_url(self):
        return reverse("blog_detail", kwargs={
            "slug": self.slug,
        })

    @property
    def get_hit_count(self):
        if self.hit_count_generic.exists():
            return self.hit_count_generic.first().hits
        return 0

    @property
    def get_share_link(self):
        current_site = settings.MY_SITE
        blog_url = self.get_url
        return f"{current_site}{blog_url}"
