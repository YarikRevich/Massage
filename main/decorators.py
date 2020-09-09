from django.contrib.auth.models import User
from main.models import ModificatedUser
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.contrib.messages import add_message, ERROR


def is_authenticated(func):

    def wrapper(form_object, request, *args, **kwargs) -> object:
        """Checks whether user is athenticated.
        If it does, returns the func, but if not 
        returns the ERROR message
        """

        if request.user.is_authenticated or request.COOKIES.get("*1%"):
            return func(form_object, request, *args, **kwargs)
        add_message(request, ERROR, "Вы не авторизованы")
        return redirect("Reviews", page=1)

    return wrapper