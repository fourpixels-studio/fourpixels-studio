from .models import Testimonial, Blog
from projects.models import Project


def get_testimonials():
    return Testimonial.objects.all()


def get_previous_and_next_blog(blog):
    blogs = Blog.objects.order_by('-pub_date')
    blog_index = list(blogs).index(blog)
    previous_blog = None
    next_blog = None

    if blog_index > 0:
        previous_blog = blogs[blog_index - 1]

    if blog_index < len(blogs) - 1:
        next_blog = blogs[blog_index + 1]

    return previous_blog, next_blog


def get_projects():
    return Project.objects.all()
