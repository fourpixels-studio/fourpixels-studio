from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("djg400/", djg400, name="djg400"),
    path("services/", services, name="services"),
    path("djg400/merchandise/", merchandise, name="merchandise"),
    path("services/web-app-development/", services_web_development, name="services_web_development"),
    path("blog/<slug:slug>/", blog_detail, name="blog_detail"),
    path("blogs/", blog_list, name="blog_list"),
    path('newsletter/', newsletter, name='newsletter'),
    path('artworks/', artworks, name='artworks'),
    path('download-success/<int:pk>/', downloadSuccess, name='download-success'),
    path('testimonials/', testimonials_list, name='testimonials_list'),
    path('help/', help, name='help'),
]
