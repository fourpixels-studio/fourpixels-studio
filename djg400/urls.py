from django.urls import path
from .views import mixes_list, remixes_list, remix_detail, update_audio_download_count, update_video_download_count


urlpatterns = [
    path("", mixes_list, name="mixes_list"),
    path("remixes/", remixes_list, name="remixes_list"),
    path("remix/<slug:slug>/", remix_detail, name="remix_detail"),
    path('update_audio_download_count/<int:track_id>/',
         update_audio_download_count, name='update_audio_download_count'),
    path('update_video_download_count/<int:track_id>/',
         update_video_download_count, name='update_video_download_count'),
]
