from django.template import Library

register = Library()

@register.filter("transform")
def transform(value: object,*args, **kwargs) -> str or None:
    if value:
        return str(value)
    return _
    

@register.filter("add_picture")
def get_service_photo(folder_name: str, image_name: str,*args, **kwargs) -> str:
    return "%s/%s" % (folder_name, image_name)