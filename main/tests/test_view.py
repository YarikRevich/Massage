from django.test import TestCase
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from main.views import ServiceInfo

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
