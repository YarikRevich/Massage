from django.test import TestCase
from rest_framework.test import APITestCase
from django.shortcuts import reverse
from rest_framework import status
from main.models import Record
from django.contrib.auth.models import User


class APIRecordTest(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        for index in range(0,10):
            
            new_record = Record.objects.create(
                author="Test%d" % (index),
                name="Test%d" % (index),
                description="Test%d" % (index),
                phone= "00000000%d" % (index)
            )

            new_record.save()
    
        new_user = User.objects.create_superuser(username="Test", password="Test1234")
        new_record.save()

    def get_record(self, pk) -> object:
        return Record.objects.get(pk=pk)


    def test_get_all_records(self) -> None:
        self.client.login(username="Test", password="Test1234")
        data = self.client.get("http://localhost:8000/ru/api/records")
        print(data)
        self.assertTrue(data.data.get("results"))
        self.assertEqual(data.status_code, status.HTTP_200_OK)
        