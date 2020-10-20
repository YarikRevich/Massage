from binascii import Error
from main.models import ModificatedUser
from django.contrib.auth.models import User
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist
from main.services import MemcacheClient


class PathLog:
    """Creates a que with two elements: a previous path and an actual one"""

    paths_que:list = []

    def __init__(self, get_request: object):
        self._get_request = get_request

    def __call__(self ,request: object):

        def _append_new_path() -> None:
            if not "api" in request.get_full_path():
                self.paths_que.append(request.get_full_path())
                if len(self.paths_que) >= 3:
                    del self.paths_que[0]

        _append_new_path()
        
        try:
            request.session["previous_path"] = self.paths_que[0].split("/",2)[2]
        except (IndexError, Error):
            pass
        
        return self._get_request(request)


class VisitLog:
    """A log of user's visits to the site."""

    def __init__(self, get_request: object):
        self._get_request = get_request
        self._memstorage = MemcacheClient()

    def __call__(self, request: object):

        if self._checks_auth(request):
            try:
                user = ModificatedUser.objects.select_related("user").get(number_of_user=request.COOKIES["*1%"]).user
            except KeyError:
                try:
                    user = User.objects.get(username=request.user.username)
                except ObjectDoesNotExist:
                    pass
            if not self._memstorage.check_whether_session_is_the_same(user.username, request):
                ModificatedUser.objects.filter(user=user).update(number_of_visites=F("number_of_visites") + 1)
        return self._get_request(request)


    def _checks_auth(self, request: object):
        return True if (request.COOKIES.get("*1%") or request.user.is_authenticated) else False
