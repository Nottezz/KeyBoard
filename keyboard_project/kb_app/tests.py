from django.test import TestCase
from django.urls import reverse


class GetPagesTestCase(TestCase):
    def test_main_page(self):
        path = reverse("home")
        response = self.client.get(path)
        self.assertEqual(200, response.status_code)
