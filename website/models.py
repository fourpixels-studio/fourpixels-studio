from django.db import models
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation


class Newsletter(models.Model):
    email = models.EmailField(blank=True, null=True)
    date_added = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    consent = models.BooleanField(default=True, null=True, blank=False)

    def __str__(self):
        return self.email


class Testimonial(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    testimonial = models.TextField(blank=True, null=True)
    post_testimonial = models.BooleanField(default=True, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to="testimonial-images/", blank=True, null=True)

    def __str__(self):
        return f"{self.name}' Testimonial - Posted On: {self.pub_date.strftime('%A, %B %d, %Y')}"


class Contact(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    @property
    def get_hit_count(self):
        if self.hit_count_generic.exists():
            return self.hit_count_generic.first().hits
        return 0

    def __str__(self):
        return f'{self.name} | {self.message[:100]} | {self.date}'


class HomePage(models.Model):
    hero_h1 = models.CharField(max_length=150, blank=True, null=True)
    hero_p = models.CharField(max_length=150, blank=True, null=True)
    hero_btn_primary = models.CharField(max_length=25, blank=True, null=True)
    hero_btn_secondary = models.CharField(max_length=25, blank=True, null=True)
    card_1_icon = models.CharField(max_length=70, blank=True, null=True)
    card_1_title = models.CharField(max_length=25, blank=True, null=True)
    card_1_paragraph = models.TextField(blank=True, null=True)
    card_2_icon = models.CharField(max_length=70, blank=True, null=True)
    card_2_title = models.CharField(max_length=25, blank=True, null=True)
    card_2_paragraph = models.TextField(blank=True, null=True)
    card_3_icon = models.CharField(max_length=70, blank=True, null=True)
    card_3_title = models.CharField(max_length=25, blank=True, null=True)
    card_3_paragraph = models.TextField(blank=True, null=True)
    about_us_h1 = models.CharField(max_length=50, blank=True, null=True)
    about_us_p = models.TextField(blank=True, null=True)
    about_us_button = models.CharField(max_length=20, blank=True, null=True)
    about_us_image = models.ImageField(
        upload_to="homepage/", blank=True, null=True)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    @property
    def get_hit_count(self):
        if self.hit_count_generic.exists():
            return self.hit_count_generic.first().hits
        return 0

    def __str__(self):
        return "Home Page"


class Service(models.Model):
    icon = models.CharField(max_length=70, blank=True, null=True)
    title = models.CharField(max_length=25, blank=True, null=True)
    paragraph = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Accordion(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    @property
    def get_hit_count(self):
        if self.hit_count_generic.exists():
            return self.hit_count_generic.first().hits
        return 0

    def __str__(self):
        return "About Us"
