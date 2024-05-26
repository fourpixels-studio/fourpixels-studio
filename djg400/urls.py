from django.urls import path
from .views import mixes_list, remixes_list, remix_detail, update_download_count


urlpatterns = [
    path("", mixes_list, name="mixes_list"),
    path("remixes/", remixes_list, name="remixes_list"),
    path("remix/<slug:slug>/", remix_detail, name="remix_detail"),
    path('update_download_count/<int:track_id>/',
         update_download_count, name='update_download_count'),
]
