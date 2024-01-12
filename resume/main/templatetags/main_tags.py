from django import template
from django.db.models import Count


from main.utils import menu

register = template.Library()


@register.simple_tag
def get_menu():
    return menu

