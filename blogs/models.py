from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from hitcount.models import HitCount
from django.utils.text import slugify
from django.contrib.sites.models import Site
from django_resized import ResizedImageField
from django.templatetags.static import static
from django.contrib.contenttypes.fields import GenericRelation


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    conclusion = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="blogs")
    cover = models.ImageField(blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    thumbnail = ResizedImageField(size=[1200, 633], crop=['middle', 'center'], quality=75, upload_to='thumbnails/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - Published On: {self.pub_date.strftime('%a, %b %d, %Y')}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

        if self.cover and (not self.thumbnail or self.thumbnail.name != f"{self.cover.name}"):
            self.thumbnail.save(f"{self.cover.name}", self.cover, save=False)
            super(Blog, self).save(update_fields=['thumbnail'])

    @property
    def meta_url(self):
        return self.get_share_link

    @property
    def get_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def get_share_link(self):
        domain = Site.objects.get_current().domain
        return f"https://{domain}{self.get_absolute_url()}"

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    @property
    def get_hit_count(self):
        if self.hit_count_generic.exists():
            return self.hit_count_generic.first().hits
        return 0

    @property
    def get_meta_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        return static('blogs_thumbnail.jpg')

    @property
    def get_hashtags(self):
        main = "FourPixelsStudioBlogs"
        tags = ''
        if self.tags:
            tags = ' '.join(f"#{item.strip().replace(' ', '')}" for item in self.tags.split(','))
        return f"#{self.category.name.strip().replace(' ', '')} {tags} #{main}".strip()
