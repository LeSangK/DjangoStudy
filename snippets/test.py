from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class SnippetTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_snippet(self):
        url = "/snippets/new/"
        data = {
            "title": "壊滅の世界から",
            "code": 'print("Hello, World!")',
            "description": "こんにちは！世界",
            "created_by": 1,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "壊滅の世界から")
        self.assertEqual(response.data["code"], 'print("Hello, World!")')
