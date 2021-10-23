from django.test import TestCase
from django.test import Client
from django.urls import reverse


class TestLettingsView(TestCase):
    client = Client()

    def test_profiles_index(self):
        response = self.client.get(reverse('profiles:index'))
        expected = "<h1>Profiles</h1>"
        assert expected.encode() in response.content

"""
    def test_lettings_letting(self):
        response = self.client.get(reverse('profiles:profile', kwargs={'username': 'AirWow'}))
        assert response.status_code == 200
"""

