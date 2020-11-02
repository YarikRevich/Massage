from main.models import ModificatedUser
from django.contrib.auth.models import User
from main.services import create_user_id 


def add_mod_user_data(*args, **kwargs):
    """Adds mod_data for user authed via social media."""

    if not ModificatedUser.objects.filter(user=User.objects.get(username=kwargs["username"])):
        ModificatedUser.objects.create(
            user=User.objects.get(username=kwargs["username"]),
            number_of_user=create_user_id())
    