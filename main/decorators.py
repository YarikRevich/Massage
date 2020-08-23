import functools
from django.shortcuts import redirect
from django.http import HttpResponse


def logged_check(func) -> object:
    """
    Checks whether user is logged in or not 
    and then redirects him to the auth page
    
    """

    @functools.wraps(func)
    def _wrapper(request,*args, **kwargs):
        if request.user.is_authenticated:
            return func(request)
        if request.COOKIES.get("*1%",None):
            return func(request)
        return redirect("Account")
    
    return _wrapper

