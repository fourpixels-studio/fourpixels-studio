from django.urls import path
from .views import applications_list, image_search, image_compression


urlpatterns = [
    path("", applications_list, name="applications_list"),
    path("image-compression/", image_compression, name="image_compression"),
    path("image-search/", image_search, name="image_search"),
]
