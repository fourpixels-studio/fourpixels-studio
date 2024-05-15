from django.urls import path
from .views import projects_list, project_detail


urlpatterns = [
    path("", projects_list, name="projects_list"),
    path("<slug:slug>/", project_detail, name="project_detail"),
]
