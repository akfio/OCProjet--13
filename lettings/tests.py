from django.test import TestCase
from django.test import Client
from django.urls import reverse


class TestLettingsView(TestCase):
    client = Client()

    def test_lettings_index(self):
        response = self.client.get(reverse('lettings:index'))
        expected = "<h1>Lettings</h1>"
        assert expected.encode() in response.content


"""
    def test_lettings_letting(self):
        response = self.client.get(reverse('lettings:letting', kwargs={'letting_id': 1}))
        assert response.status_code == 200
"""
