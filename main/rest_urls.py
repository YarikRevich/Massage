from django.urls import path,include
from main.rest_view import RecordMetaClass
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

router = DefaultRouter()
router.register("records", RecordMetaClass)

urlpatterns = [
    path("",include(router.urls))
    ]