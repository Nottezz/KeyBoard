from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class GetPagesTestCase(TestCase):
    def test_main_page(self):
        path = reverse("keyboards:home")
        response = self.client.get(path)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertTemplateUsed(response, "kb_app/home.html")
        self.assertIn("kb_app/home.html", response.template_name)

    def test_catalog_page(self):
        path = reverse("keyboards:keyboard_list")
        response = self.client.get(path)
        self.assertEqual(200, response.status_code)
