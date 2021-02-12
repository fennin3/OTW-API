from django.test import TestCase

from django.contrib import auth
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('enninadmin@gmail.com', 'otwadmin', 'P@ssw0rd1998')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='otwadmin', password='P@ssw0rd1998')