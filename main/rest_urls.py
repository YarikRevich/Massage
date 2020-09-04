from django.urls import path,include
from main.rest_view import RecordMetaClass, ServiceMetaClass, DoctorInfoMetaClass, VisitImageMetaClass
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("records", RecordMetaClass)
router.register("service", ServiceMetaClass)
router.register("about", DoctorInfoMetaClass)
router.register("visitimages", VisitImageMetaClass)

urlpatterns = [
    path("", include(router.urls)),
    ]