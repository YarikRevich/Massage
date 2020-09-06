from django.conf.urls import url
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import (Landing,
                Info,
                Account,
                Regestration,
                ServiceList,
                ServiceInfo,
                ReviewPage,
                DeleteReviewClass,
                DeleteRecordClass,
                mailinglist_subscribing,
                logout_user,
                PasswordReset)


urlpatterns = [
    path("", Landing.as_view(), name = Landing.name),
    path("reviews/delete/<int:pk>", DeleteReviewClass.as_view(), name = DeleteReviewClass.name),
    path("reviews/<int:page>", ReviewPage.as_view(), name = ReviewPage.name),
    path("services/info/<int:pk>", ServiceInfo.as_view(), name = ServiceInfo.name),
    path("services/", ServiceList.as_view(), name = ServiceList.name),
    path("info/", Info.as_view(), name = Info.name),
    path("mailinglist-subscribing", mailinglist_subscribing, name="Mailinglist-subscribing"),
    path("account/", Account.as_view(), name = Account.name),
    path("account/regestration", Regestration.as_view(), name = Regestration.name),
    path("account/logout", logout_user, name = "Logout"),
    path("account/delete-record/<int:pk>", DeleteRecordClass.as_view(), name = DeleteRecordClass.name),
    path("account/password-reset/", PasswordReset.as_view(), name = PasswordReset.name),
    path("accounts/", include("django.contrib.auth.urls"))
]
