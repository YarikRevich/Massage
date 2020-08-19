from django.test import TestCase
from main.forms import RegForm
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from main.backends import authenticate

class RegFormTest(TestCase):
    """Test made to check the functionality of RegForm"""

    def test_reg_user(self):
        """Cheks the saving mechanism of the prviously described form"""

        data = {
            "username":"Test",
            "email":"test@gmail.com",
            "first_name":"Tester",
            "last_name":"Testerovich",
            "phone":45545452454,
            "password1":"test1234",
            "password2":"test1234"}
            
        form = RegForm(data=data)
        form.is_valid()
        self.assertTrue(form.save())



