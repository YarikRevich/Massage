from django.contrib.auth.models import User
from typing import Union
from django.core.exceptions import ObjectDoesNotExist


def authentication(username: str, password: str = None, admin: bool = False) -> Union[None, object]:
    """Checks whether user's credentials are valid"""

    try:
        if not admin:
            return User.objects.get(username=username, password=password)
        return User.objects.get(username=username)
    except ObjectDoesNotExist:
        return None
