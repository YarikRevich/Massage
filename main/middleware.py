from binascii import Error


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