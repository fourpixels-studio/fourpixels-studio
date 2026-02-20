from django.urls import path
from .views import projects_list, project_detail, update_project


urlpatterns = [
    path("", projects_list, name="projects_list"),
    path("<slug:slug>/", project_detail, name="project_detail"),
    path("update/<int:pk>/", update_project, name="update_project"),
]