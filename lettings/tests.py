from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import Letting, Address


class TestLettingsView(TestCase):
    client = Client()

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(number=5, street='okok', city='lille',
                                             state=59, zip_code=5900, country_iso_code='FRA')
        cls.title = Letting.objects.create(address=cls.address, title="Test")

    def test_lettings_index(self):
        response = self.client.get(reverse('lettings:index'))
        expected = "<title>Lettings</title>"
        assert expected.encode() in response.content

    def test_lettings_letting(self):
        response = self.client.get(reverse('lettings:letting',
                                           kwargs={'letting_id': self.title.id}))
        expected = "<title>" + str(self.title) + "</title>"
        assert expected.encode() in response.content
