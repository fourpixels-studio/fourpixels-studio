from django.urls import path
from .views import applications_list
from .image_search import image_search
from .image_compression import image_compression
from .bloomberg_news_finder import bloomberg_news_finder
from .qr_code_generator import qr_code_generator, download_qr_code


urlpatterns = [
    path("", applications_list, name="applications_list"),
    path("image-compression/", image_compression, name="image_compression"),
    path("image-search/", image_search, name="image_search"),
    path("Bloomberg-News-Finder/", bloomberg_news_finder, name="bloomberg_news_finder"),
    path("QR-Code-Generator/", qr_code_generator, name="qr_code_generator"),
    path("download/QR-Code-Generator/", download_qr_code, name="download_qr_code"),
]
