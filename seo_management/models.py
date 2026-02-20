from django.db import models


class SEO(models.Model):
    title_tag = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_thumbnail = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.title_tag} {self.pk}"
