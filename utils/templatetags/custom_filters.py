from django import template
from django.utils import timezone
from django.utils.timesince import timesince

register = template.Library()


@register.filter(name='round_timesince')
def round_timesince(value):
    """
    Rounds the timesince to the largest unit.
    """
    if value:
        now = timezone.now()
        return timesince(value, now).split(', ')[0]
    return ''
