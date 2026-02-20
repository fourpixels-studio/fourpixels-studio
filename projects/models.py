from django.db import models
from django.urls import reverse
from hitcount.models import HitCount
from django.utils.text import slugify
from website.models import Testimonial
from django.utils.html import mark_safe
from django.contrib.contenttypes.fields import GenericRelation

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
    client = models.CharField(max_length=100, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    what_we_did = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    company_category = models.CharField(max_length=100, blank=True, null=True)
    website_link = models.TextField(blank=True, null=True)
    link_name = models.CharField(max_length=40, blank=True, null=True)
    blog_link = models.TextField(blank=True, null=True)
    app_link = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="projects/logos/", blank=True, null=True)
    highlight = models.BooleanField(default=False, null=True, blank=True)
    image_placeholder = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    highlight = models.BooleanField(default=False, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    cover = models.FileField(upload_to="projects/cover/", blank=True, null=True)
    testimonial = models.ForeignKey(Testimonial, on_delete=models.CASCADE, null=True, blank=True)
    show_in_porfolio = models.BooleanField(default=True)
    similar_projects = models.ManyToManyField("self", blank=True)
    content = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['-pk']
        
    def __str__(self):
        return f"{self.name} - {self.category}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @property
    def get_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})

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
    def get_cover_image(self):
        try:
            cover = self.cover.url
        except:
            cover = self.logo.url
        return cover
        
    @property
    def get_short_description(self):
        if self.what_we_did:
            return self.what_we_did
        elif len(self.description) > 130:
            return f"{self.description[:130]}..."
        return f"{ self.category.name} for {self.name}."
    
    @property
    def get_related_projects(self):
        if self.similar_projects:
            projects = Project.objects.filter(category=self.category, show_in_porfolio=True).exclude(pk=self.pk)
            if projects:
                return projects
            else:
                projects = Project.objects.filter(show_in_porfolio=True).exclude(pk=self.pk)
            return projects
        return None

    @property
    def get_images(self):
        if ProjectMedia.objects.filter(project=self).exists():
            return ProjectMedia.objects.filter(project=self)
        return None
    
    def get_absolute_url(self):
        return f"/projects/{self.slug}/"
        
        
class ProjectMedia(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(blank=True, null=True, upload_to="projects/media/")
    image = models.FileField(blank=True, null=True, upload_to="projects/media/")

    def __str__(self):
        return f"{self.name} - {self.project.name}"
