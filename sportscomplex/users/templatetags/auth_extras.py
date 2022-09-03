from urllib import request
from django import template
from django.contrib.auth.models import Group , User

register = template.Library()

@register.filter(name='has_attr')
def has_attr(user, attribute): 
    return hasattr(user, attribute)
