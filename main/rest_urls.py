from django.urls import path
from main.rest_view import RecordAllGetter,RecordGetter,RecordSetter
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path("get_records/",login_required(RecordAllGetter.as_view())),
	path("get_records/<int:pk>",login_required(RecordGetter.as_view())),
    path("put_records/",login_required(RecordSetter.as_view()))
    ]