from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.


class TestViews(TestCase):

    def test_should_show_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response, 'base_templates/register.html')


    def test_should_show_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response, 'base_templates/login.html')

    def test_should_signup_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response, 'base_templates/login.html')


