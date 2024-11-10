from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class SignUpTest(TestCase):
    def setup(self) -> None:
        self.username = 'SupaDupa1337'
        self.email = 'user-70ca8443-f6b3-4888-8aeb-96810e1f4669@mailslurp.biz'
        self.first_name = 'Master'
        self.last_name = 'Hacker'
        self.password1 = 'SUp3RH@x0r'
        self.password2 = 'SUp3RH@x0r'

    def signup_form(self):
        response = self.client.post(reverse('signup', data = {
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password1': self.password1,
            'password2': self.password2
        }))