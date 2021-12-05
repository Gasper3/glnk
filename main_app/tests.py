from pprint import pprint as pp

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Url


class UrlRESTTestCase(APITestCase):
    def setUp(self) -> None:
        Url.objects.create(url="https://wp.pl", short_url="qWeRt")
        Url.objects.create(url="https://google.com", short_url="asdFGH")

    def test_get_url(self):
        url = reverse("get-url", kwargs={"short_url": "qWeRt"})
        response = self.client.get(url)
        data: dict = response.data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual("https://wp.pl", data.get("url"))

    def test_get_url_404(self):
        url = reverse("get-url", kwargs={"short_url": "not_exist"})
        response = self.client.get(url)

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_create_url(self):
        url = reverse("create-url")
        response = self.client.post(url, {"url": "https://onet.pl"})
        data: dict = response.data

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual("https://onet.pl", data.get("url"))
        self.assertIsNotNone(data.get("short_url"))
        self.assertNotEqual(data.get("short_url"), "")

    def test_create_url_get_existing(self):
        url = reverse("create-url")
        response = self.client.post(url, {"url": "https://google.com"})
        data: dict = response.data

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual("https://google.com", data.get("url"))
        self.assertEqual("asdFGH", data.get("short_url"))

    def test_create_url_check_ip_and_user_agent(self):
        url = reverse("create-url")
        response = self.client.post(url, {"url": "http://asd.pl"}, HTTP_USER_AGENT="ApiClientTestCase")
        created_url: Url = Url.objects.get(url="http://asd.pl")

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual("127.0.0.1", created_url.ip_address)
        self.assertEqual("ApiClientTestCase", created_url.user_agent)
