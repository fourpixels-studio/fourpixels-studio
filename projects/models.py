from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.html import mark_safe


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
    logo = models.ImageField(
        upload_to="projects/logos/", blank=True, null=True)
    highlight = models.BooleanField(default=False, null=True, blank=True)
    image_placeholder = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    def __str__(self):
        return f"{self.name} - {self.category}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def get_url(self):
        return reverse("project_detail", kwargs={
            "slug": self.slug,
        })

    @property
    def get_short_name(self):
        name = self.name
        split_name = name.split(" ")
        first_name = split_name[0]
        return first_name

    @property
    def get_hit_count(self):
        if self.hit_count_generic.exists():
            return self.hit_count_generic.first().hits
        return 0

    @property
    def get_project_media(self):
        project_media_list = ProjectMedia.objects.filter(project=self)
        media_list = []
        for project_media in project_media_list:
            media_element = None
            if project_media.video:
                media_element = mark_safe(
                    f'<video controls class="img-fluid rounded-4 w-100"><source src="{project_media.video.url}" type="video/mp4"></video>')
            elif project_media.image:
                media_element = mark_safe(
                    f'<img src="{project_media.image.url}" class="img-fluid rounded-4 border w-100"/>')
            media_list.append(
                (
                    project_media.pk, media_element,
                    project_media.name, project_media.description
                )
            )
        return media_list


class ProjectMedia(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(
        blank=True, null=True,
        upload_to="projects/media/")
    image = models.FileField(
        blank=True, null=True,
        upload_to="projects/media/")

    def __str__(self):
        return f"{self.name} - {self.project.name}"
