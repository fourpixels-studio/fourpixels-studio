from blogs.models import Blog
from django.urls import reverse
from projects.models import Project
from django.contrib.sitemaps import Sitemap


class StaticSitemap(Sitemap):
    def items(self):
        return [
            'applications_list', 'image_compression', 'image_search', 'contact',
            'bloomberg_news_finder', 'qr_code_generator', 'index', 'about', 'projects_list',
        ]

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    def items(self):
        return Blog.objects.all()[:100]


class ProjectSitemap(Sitemap):
    def items(self):
        return Project.objects.all()[:100]
