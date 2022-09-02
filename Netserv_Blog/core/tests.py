from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.

class TestModels(TestCase):
    def test_user_registration(self):
        user = User.objects.create_user("abc", "abc@ngnetserv.com", "samplepass")
        self.client.force_login(user = user)
        response = self.client.get(reverse('add_post'))
        self.assertEqual(response.status_code, 200)

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


