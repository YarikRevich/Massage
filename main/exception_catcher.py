from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.http import JsonResponse, HttpResponse, Http404
from main.models import ModificatedUser
from Massage.settings import EXCEPTION_CATCHER
import logging


def exceptions_catcher(class_object):
    """Catches errors and logs them."""

    def _get_username(request):

        if username := request.user.username:
            return username
        try:
            return ModificatedUser.objects.select_related("user").get(number_of_user=request.COOKIES["*1%"]).user.username
        except KeyError:
            return "UserIsNotAuthenticated"


    def _create_error_log(request, error_message) -> None:
        """Creates error log."""

        logger = logging.getLogger(__name__)
        username = _get_username(request)
        logger.error(f"ExceptionPlace: {class_object.__name__}, ErrorMessage: {str(error_message)}, UserLogin: {username}")


    def wrapper(*args, **kwargs):
        try:
            return class_object(*args, **kwargs)
        except Exception as e:
            if EXCEPTION_CATCHER:
                _create_error_log(args[0], e)
                return HttpResponse(status=500)
            return class_object(*args, **kwargs)

    return wrapper