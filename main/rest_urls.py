from django.urls import path,include
from main.rest_view import RecordMetaClass, ServiceMetaClass
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register("records", RecordMetaClass)
router.register("service", ServiceMetaClass)


urlpatterns = [
    path("", include(router.urls)),
    ]