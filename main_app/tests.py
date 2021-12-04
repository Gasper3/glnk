from pprint import pprint as pp

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Url


class UrlRESTTestCase(APITestCase):
    def setUp(self) -> None:
        Url.objects.create(url="wp.pl", short_url="qWeRt")
        Url.objects.create(url="google.com", short_url="asdFGH")

    def test_get_url(self):
        url = reverse("get-url", kwargs={"short_url": "qWeRt"})
        response = self.client.get(url)
        data: dict = response.data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual("wp.pl", data.get("url"))

    def test_get_url_404(self):
        url = reverse("get-url", kwargs={"short_url": "not_exist"})
        response = self.client.get(url)

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_create_url(self):
        url = reverse("create-url")
        response = self.client.post(url, {"url": "onet.pl"})
        data: dict = response.data

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data.get("url"), "onet.pl")
        self.assertIsNotNone(data.get("short_url"))
        self.assertNotEqual(data.get("short_url"), "")

    def test_create_url_get_existing(self):
        url = reverse("create-url")
        response = self.client.post(url, {"url": "google.com"})
        data: dict = response.data

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual("google.com", data.get("url"))
        self.assertEqual("asdFGH", data.get("short_url"))
