from .models import Testimonial
from projects.models import Project


def get_testimonials():
    return Testimonial.objects.all()


def get_recent_projects():
    return Project.objects.filter(show_in_porfolio=True)


def get_project_highlights():
    return Project.objects.filter(highlight=True, show_in_porfolio=True)
