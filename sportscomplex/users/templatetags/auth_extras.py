from urllib import request
from django import template
from django.contrib.auth.models import Group , User

register = template.Library()

@register.filter(name='has_group')
def has_attr(user, attribute): 
    if hasattr(request.user, attribute) :
        return True
    else:
        return False