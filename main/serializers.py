from rest_framework import serializers
from main.models import Record, Service
from phone_field import PhoneField

class RecordSerialize(serializers.ModelSerializer):
    """
    This serializer shows us a serialized 'Record' model

    """

    author = serializers.ReadOnlyField(source="author.username")
    

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
        
    
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    phone = serializers.CharField(max_length=100,read_only=True)

    # def update(self,instanse,data):
    #     instanse.author = instanse.author
    #     instanse.name = data.get("name",instanse.name)
    #     instanse.phone = instanse.phone
    #     instanse.status = data.get("status",instanse.status)
    #     instanse.seen = data.get("seen",instanse.seen)
    #     instanse.save()
    #     return instanse
