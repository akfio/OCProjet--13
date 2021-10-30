from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User


class TestProfilesView(TestCase):
    client = Client()

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.profile = Profile.objects.create(user=cls.user, favorite_city="Lille")

    def test_profiles_index(self):
        response = self.client.get(reverse('profiles:index'))
        expected = "<title>Profiles</title>"
        assert expected.encode() in response.content

    def test_profiles_letting(self):
        response = self.client.get(reverse('profiles:profile', kwargs={'username': self.user}))
        expected = "<title>" + str(self.user) + "</title>"
        assert expected.encode() in response.content
