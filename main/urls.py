
from django.urls import path
from .views import Landing, Info, Account, Regestration, ServiceList, ServiceInfo, ReviewPage
from main.decorators import logged_check
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("", logged_check(Landing.as_view()), name="Landing"),
    path("reviews/<int:page>", ReviewPage.as_view(), name="Reviews"),
    path("services/", ServiceList.as_view(), name="Services"),
    path("services/info/<int:pk>", ServiceInfo.as_view(), name="ServiceInfo"),
    path("info/", logged_check(Info.as_view()), name="Info"),
    path("account/", Account.as_view(), name="Account"),
    path("account/regestration", Regestration.as_view(), name="Reg"),
]
