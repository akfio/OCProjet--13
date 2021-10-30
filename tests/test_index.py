from django.test import Client

client = Client()


def test_index(client):
    response = client.get('')
    expected = '<title>Holiday Homes</title>'
    assert expected.encode() in response.content
