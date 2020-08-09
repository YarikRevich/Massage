from rest_framework import serializers
from main.models import Record, Service
from phone_field import PhoneField


class RecordSerialize(serializers.ModelSerializer):
    """
    This serializer shows us a serialized 'Record' model

    """

    class Meta:
        model = Record
        fields = ("id",
            "author",
            "name",
            "description",
            "time",
            "phone",
            "status",
            "seen")
        
    author = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    phone = serializers.CharField(max_length=100,required=False)
