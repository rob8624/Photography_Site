from django import template
from django.contrib.auth import get_user_model
from django.template.loader import get_template


register = template.Library()

@register.filter
def semester(Media, gallery):
    return Media.image.filter(album_pictures=gallery)

