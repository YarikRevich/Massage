from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def authenticate(**credentials):
    if credentials.get("username") and credentials.get("password"):
        try:
            if user_instanse := User.objects.get(username=credentials["username"],password=credentials["password"]):
                return user_instanse
        except ObjectDoesNotExist:
            return None
    return None