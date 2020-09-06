from django.contrib.auth.models import User
from typing import Union
from django.core.exceptions import ObjectDoesNotExist


def authentication(username: str, password: str) -> Union[bool, object]:
    """Checks whether user's credentials are valid"""

    try:
        return User.objects.get(username=username, password=password)
    except ObjectDoesNotExist:
        return False