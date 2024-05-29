from .models import Testimonial
from projects.models import Project


def get_testimonials():
    return Testimonial.objects.all()


def get_projects():
    return Project.objects.all()
