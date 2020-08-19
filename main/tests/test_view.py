from django.test import TestCase
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from main.views import ServiceInfo
from main.backends import authenticate
from main.models import Service

class ServiceInfoViewTest(TestCase):
    """Test to check all the functionality of ServiceInfo and RecordForm"""

    @classmethod
    def setUpTestData(cls):
        """Creates new User with such credentials as 'Test' and 'test1234'"""

        user = User.objects.create_user(username="Test", password="test1234")
        user.save()
        service = Service.objects.create(name="Test",description="Test",price=10000,currency="EUR")
        service.save()
        cls.service = Service.objects.get(name="Test")

    def test_record_add(self):
        """Makes a test record
        -> Login to web-site with previously made user's credentials
        -> Makes a test POST request to the page with name 'ServiceInfo' and with pk parrametr
        -> Checks whether gotten status_code is equal to written

        """

        login = self.client.login(username="Test", password="test1234")
        resp = self.client.post(self.service.get_absolute_url(), data={"description":"-","service_name":"Test"})
        self.assertEqual(resp.status_code,200)

    def test_html_template(self):
        """Checks whether the userd template is appropriate"""

        resp = self.client.get(self.service.get_absolute_url())
        self.assertTemplateUsed(resp, "main/serviceinfo.html")

class AuthTest(TestCase):
    """Test for the ckecking of the custom made authenticate backend"""

    @classmethod
    def setUpTestData(cls):
        """Creates new User entry with such credentials as 'yarik' and 'yarik1234'"""

        new_user = User.objects.create(username="yarik",password="yarik1234")
        new_user.save()

    def test_authentification(self):
        """Uses previously made user's credentials to authenticate previously made user
           and checks whether the gotten response is True
        """

        user = authenticate(username="yarik",password="yarik1234")
        self.assertTrue(user)