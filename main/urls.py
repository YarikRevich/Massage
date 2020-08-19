
from django.urls import path
from main.decorators import logged_check
from django.views.decorators.csrf import csrf_exempt
from .views import (Landing,
                Info,
                Account,
                Regestration,
                ServiceList,
                ServiceInfo,
                ReviewPage,
                DeleteReviewClass,
                DeleteRecordClass)


urlpatterns = [
    path("", logged_check(Landing.as_view()), name = Landing.name),
    path("reviews/delete/<int:pk>", DeleteReviewClass.as_view(), name = DeleteReviewClass.name),
    path("services/", ServiceList.as_view(), name = ServiceList.name),
    path("reviews/<int:page>", ReviewPage.as_view(), name = ReviewPage.name),
    path("services/info/<int:pk>", ServiceInfo.as_view(), name = ServiceInfo.name),
    path("info/", logged_check(Info.as_view()), name = Info.name),
    path("account/", Account.as_view(), name = Account.name),
    path("account/regestration", Regestration.as_view(), name = Regestration.name),
    path("account/delete-record/<int:pk>", DeleteRecordClass.as_view(), name = DeleteRecordClass.name)
]
