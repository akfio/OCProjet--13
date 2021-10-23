from django.test import Client

client = Client()


def test_index(client):
    response = client.get('')
    expected = '<h1>Welcome to Holiday Homes</h1>'
    assert expected.encode() in response.content