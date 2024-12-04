from django import template

register = template.Library()

@register.filter
def contains(text, substring):
    return substring in text
