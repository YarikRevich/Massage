from rest_framework import serializers
from main.models import Record, Service
from phone_field import PhoneField

class RecordSerialize(serializers.ModelSerializer):
    """
    This serializer shows us a serialized 'Record' model

    """


    class Meta:
        model = Record
        fields = (
            "id",
            "author",
            "name",
            "description",
            "time",
            "phone",
            "status",
            "seen",
            "url"
            )
        
    
    author = serializers.CharField(read_only=True)
    phone = serializers.CharField(read_only=True)


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = (
            "id",
            "name",
            "photo",
            "description",
            "price",
            "currency",
        )
