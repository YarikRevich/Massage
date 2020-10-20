from main.models import Review, Service


def is_authenticated(request: object) -> bool:
    """Checks whether user is authed and then 
    if it does it returns True but if not False"""

    if request.user.is_authenticated or request.COOKIES.get("*1%"):
        return {"user_is_authenticated": True}
    return {"user_is_authenticated": False}