from main.models import Review, Service

def add_service_record_urls(request: object) -> dict:
    """Adds some context to all the pages"""

    review = Review()
    service = Service()
    return {
        "Review":review.get_absolute_url(),
        "Service":service.get_absolute_url_landing()
    }


def is_authenticated(request: object) -> bool:
    """Checks whether user is authed and then 
    if it does it returns True but if not False"""

    if request.user.is_authenticated or request.COOKIES.get("*1%"):
        return {"user_is_authenticated": True}
    return {"user_is_authenticated": False}