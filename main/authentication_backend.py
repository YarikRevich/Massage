from django.contrib.auth.models import User
from social_django.models import UserSocialAuth
from typing import Union
from django.core.exceptions import ObjectDoesNotExist


def authentication(username: str, password: str = None, admin: bool = False) -> Union[None, object]:
    """Checks whether user's credentials are valid"""

    if not admin:
        users = User.objects.filter(username=username)
        if len(users) > 1:
            for user in users:
                if UserSocialAuth.objects.filter(user=user):
                    pass
                else:
                    user_to_login = user
            return user_to_login
        try:
            return User.objects.get(username=username, password=password)
        except ObjectDoesNotExist:
            return None
    users = User.objects.filter(username=username)
    if len(users) > 1:
        for user in users:
            if UserSocialAuth.objects.filter(user=user):
                pass
            else:
                user_to_login = user
        return user_to_login
    try:            
        return User.objects.get(username=username)
    except ObjectDoesNotExist:
        return None
