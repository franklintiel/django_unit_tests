from django.test import TestCase
from .backends import BaseAuthentication
from django.contrib.auth.models import User

# Create your tests here.


class AuthenticationTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='john.admin', first_name='John',
                                        last_name='Doe', email='info@domain.com')
        self.user.set_password('admin123')
        self.user.save()

    def tearDown(self):
        if self.user != None:
            self.user.delete()

    def get_backend_auth_class(self):
        return BaseAuthentication()

    def test_login_ok(self):
        auth = self.get_backend_auth_class()
        user = auth.authenticate(username='john.admin',
                                 password='admin123')
        self.assertIsNotNone(user)

    def test_login_invalid_fields(self):
        auth = self.get_backend_auth_class()
        user = auth.authenticate(username=None, password=None)
        self.assertIsNone(user)

    def test_login_invalid_username(self):
        auth = self.get_backend_auth_class()
        user = auth.authenticate(username='jfstef', password='asdfasdf')
        self.assertIsNone(user)

    def test_login_invalid_password(self):
        auth = self.get_backend_auth_class()
        user = auth.authenticate(username='john.admin', password='asdfasdf')
        self.assertIsNone(user)

    def test_login_invalid_token(self):
        auth = self.get_backend_auth_class()
        user = auth.authenticate(username='test', password='test')
        token: str = auth.get_token(user=user)
        self.assertIsNone(token)
        self.assertIsNone(user)

    def test_login_inactive_user(self):
        auth = self.get_backend_auth_class()
        self.user.is_active = False
        self.user.save()
        user = auth.authenticate(username='john.admin', password='admin123')
        self.assertIsNone(user)

    def test_token_valid(self):
        auth = self.get_backend_auth_class()
        user = auth.authenticate(username='john.admin', password='admin123')
        token: str = auth.get_token(user=user)
        self.assertIsNotNone(token)
        self.assertIsNotNone(user)
