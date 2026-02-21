from .import settings
from website.sitemaps import *
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView


sitemaps = {
    "blogs": BlogSitemap,
    "static": StaticSitemap,
    "projects": ProjectSitemap,
}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls")),
    path("blogs/", include("blogs.urls")),
    path("projects/", include("projects.urls")),
    path("hitcount/", include("hitcount.urls")),
    path("applications/", include("applications.urls")),
    path("summernote/", include("django_summernote.urls")),
    path("robots.txt/", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("sitemap.xml/", sitemap, {"sitemaps": sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Four Pixels Studio"
admin.site.index_title = "Four Pixels Studio"
