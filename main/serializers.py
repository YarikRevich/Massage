from rest_framework import serializers
from main.models import Record, Service, DoctorInfo
from phone_field import PhoneField

class RecordSerialize(serializers.ModelSerializer):
    """This serializer shows us a serialized Record model"""

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
    """Serializes info from Service model"""

    class Meta:
        model = Service
        fields = (
            "id",
            "name",
            "name_de",
            "photo",
            "description",
            "description_de",
            "price",
            "currency",
        )


class DoctorInfoSerializer(serializers.ModelSerializer):
    """Serializes info from DoctorInfo model"""

    class Meta:
        model = DoctorInfo
        fields = (
            "id",
            "about_text",
            "about_text_de"
        )
