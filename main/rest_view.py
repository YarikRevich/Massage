from rest_framework.reverse import reverse
from main.models import Record, Service
from rest_framework.response import Response
from main.serializers import RecordSerialize, ServiceSerializer
from rest_framework import generics
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

    This class can be used obly by Admin user
    """

    permission_classes = (IsAdminUser,)
    queryset = Record.objects.all()
    serializer_class = RecordSerialize
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ("seen","status")

class ServiceMetaClass(ModelViewSet):

    permission_classes = (IsAdminUser,)
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


    