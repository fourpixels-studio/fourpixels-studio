from django.contrib import admin
from django.urls import path, include
from .import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from website.views import error_404, error_500

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configure admin titles
admin.site.site_header = "Four Pixels Admin"

# Tab/Site Title
admin.site.site_header = "Four Pixels"

admin.site.index_title = "Four Pixels - Admin"

handler404 = error_404
handler500 = error_500