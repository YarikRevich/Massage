from django.template import Library

register = Library()

@register.filter("transform")
def transform(value,*args, **kwargs):
    if value:
        return str(value)
    return _
    