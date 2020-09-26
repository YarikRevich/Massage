from rest_framework.reverse import reverse
from main.models import Record, Service, DoctorInfo, VisitImage
from rest_framework.response import Response
from main.serializers import RecordSerialize, ServiceSerializer, DoctorInfoSerializer, VisitImageSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter
from django_filters import rest_framework as filters
from rest_framework.parsers import MultiPartParser, FormParser


class RecordMetaClass(ModelViewSet):

    """Can do such actions
    - Show all the records
    - Show equal records
    - Create/Update records
    in Record model

    This class can be used obly by Admin user
    """

    permission_classes = (IsAdminUser,)
    queryset = Record.objects.all()
    serializer_class = RecordSerialize
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ("seen","status")


class ServiceMetaClass(ModelViewSet):
    """Can do such actions
    - Show all the records
    - Show equal records
    - Create/Update records
    in Service model

    This class can be used obly by Admin user
    """

    permission_classes = (IsAdminUser,)
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class DoctorInfoMetaClass(ModelViewSet):
    """Can do such actions
    - Show all the records
    - Show equal records
    - Create/Update records
    in DoctorInfo model

    This class can be used obly by Admin user
    """

    serializer_class = DoctorInfoSerializer
    queryset = DoctorInfo.objects.all()
    permission_classes = (IsAdminUser, )


class VisitImageMetaClass(ModelViewSet):
    """Can do such actions
    - Show all the visitimages
    - Show equal visitimages
    - Create/Update visitimages
    in DoctorInfo model

    This class can be used obly by Admin user
    """

    serializer_class = VisitImageSerializer
    queryset = VisitImage.objects.all()
    permission_classes = (IsAdminUser,)
    

class TestClass(APIView):
    """Just returns a status of server"""

    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        return Response({"status": "ok"})