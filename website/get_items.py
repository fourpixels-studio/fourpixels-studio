from .models import Testimonial


def get_testimonials():
    return Testimonial.objects.all()
