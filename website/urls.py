from django.urls import path, re_path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("blogs/", views.blog_list, name="blog_list"),
    path('newsletter/', views.newsletter, name='newsletter'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)