from django.urls import path
from .views import index, about, contact, djg400, services, newsletter, merchandise, services_web_development, blog_detail, blog_list, downloadSuccess
from .image_search import image_search
from .image_compression import image_compression


urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("djg400/", djg400, name="djg400"),
    path("services/", services, name="services"),
    path("services/app/image-search/", image_search, name="image_search"),
    path("services/app/image-compression/", image_compression, name="image_compression"),
    path("djg400/merchandise/", merchandise, name="merchandise"),
    path("services/web-app-development/", services_web_development, name="services_web_development"),
    path("blog/<slug:slug>/", blog_detail, name="blog_detail"),
    path("blogs/", blog_list, name="blog_list"),
    path('newsletter/', newsletter, name='newsletter'),
    path('download-success/<int:pk>/', downloadSuccess, name='download-success'),
]