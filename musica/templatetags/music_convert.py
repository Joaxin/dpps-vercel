from django import template

register = template.Library()

@register.filter
def url_convert(value):
    return value.replace("&","%26").strip();