from django.conf.urls import url
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from main.exception_catcher import exceptions_catcher
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
                PasswordReset,
                PasswordResetConfirm)


urlpatterns = [
    path("", exceptions_catcher(Landing.as_view()), name = Landing.name),
    path("reviews/delete/<int:pk>", exceptions_catcher(DeleteReviewClass.as_view()), name = DeleteReviewClass.name),
    path("reviews/<int:page>", exceptions_catcher(ReviewPage.as_view()), name = ReviewPage.name),
    path("services/info/<int:pk>", exceptions_catcher(ServiceInfo.as_view()), name = ServiceInfo.name),
    path("services/", exceptions_catcher(ServiceList.as_view()), name = ServiceList.name),
    path("info/", exceptions_catcher(Info.as_view()), name = Info.name),
    path("mailinglist-subscribing", mailinglist_subscribing, name="Mailinglist-subscribing"),
    path("account/", exceptions_catcher(Account.as_view()), name = Account.name),
    path("account/regestration", exceptions_catcher(Regestration.as_view()), name = Regestration.name),
    path("account/logout", exceptions_catcher(logout_user), name = "Logout"),
    path("account/delete-record/<int:pk>", exceptions_catcher(DeleteRecordClass.as_view()), name = DeleteRecordClass.name),
    path("accounts/reset/<uidb64>/<token>/", exceptions_catcher(PasswordResetConfirm.as_view()), name= PasswordResetConfirm.name),
    path("account/password-reset/", exceptions_catcher(PasswordReset.as_view()), name = PasswordReset.name),
]
