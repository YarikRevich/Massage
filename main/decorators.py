import functools
from django.shortcuts import redirect
from django.http import HttpResponse


def logged_check(func) -> "func or an 'Account' page":
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


def rest_api_method_check(func) -> "func or HttpResponse":
    """
    This func checks wether HTTP method is in 'methods' list.
    If it does it returns func but if doesn't HttpResponse with error message
    """

    @functools.wraps(func)
    def _wrapper(request,st=None,pk=None,*args, **kwargs):
        methods = ["get","post","put"]
        if request.method.lower() in methods:
            return func(request,pk=pk,st=st)
        return HttpResponse(f"This HTTP.method is not correct,(chosen HTTP.method is {request.method})")
    return _wrapper