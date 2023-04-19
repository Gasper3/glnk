import random
from datetime import datetime

import pytest
from fastapi import Response, status
from fastapi.testclient import TestClient
from httpx import Response

from app.models import Url

from . import factories


class TestUrl:
    def test_create(self, client: TestClient):
        payload = {'url': 'https://www.google.com/'}
        response = client.post('/api/url', json=payload)
        assert response.status_code == status.HTTP_201_CREATED, response.content

    def test_get(self, client: TestClient):
        url: Url = factories.UrlFactory()
        response: Response = client.get(f'/api/url/{url.short_url}')
        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert data['url'] == url.url

    def test_get__not_exists(self, client: TestClient):
        response: Response = client.get(f'/api/url/INVALID')
        assert response.status_code == status.HTTP_404_NOT_FOUND

        data = response.json()
        assert data['detail'] == 'Url not found'

    def test_redirect(self, client: TestClient):
        url: Url = factories.UrlFactory(redirect=True, url='https://www.google.com/')
        response: Response = client.get(f'/api/url/{url.short_url}', follow_redirects=False)
        assert response.status_code == status.HTTP_307_TEMPORARY_REDIRECT, response.content

    def test_create_with_redirect(self, client: TestClient):
        payload = {'url': 'https://www.google.com/', 'redirect': True}
        response = client.post(f'/api/url', json=payload)
        assert response.status_code == status.HTTP_201_CREATED

        data = response.json()

        response_get = client.get(f'/api/url/{data["short_url"]}', follow_redirects=False)
        assert response_get.status_code == status.HTTP_307_TEMPORARY_REDIRECT


class TestStatistics:
    @pytest.fixture()
    def url(self):
        return factories.UrlFactory()

    def test_stats(self, client: TestClient, url: Url):
        visits = factories.UrlVisitsFactory.create_batch(random.randint(1, 10), url=url, created=datetime(2023, 4, 1))
        response = client.get(f'/api/url/{url.short_url}/stats')
        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert data['url'] == url.url

        expected_stats = {
            'monthly': {
                '4': len(visits)
            }
        }
        assert data['stats'] == expected_stats

    def test_monthly(self, client: TestClient, url: Url):
        visits_april = factories.UrlVisitsFactory.create_batch(
            random.randint(1, 10),
            url=url,
            created=datetime(2023, 4, 1)
        )
        visits_march = factories.UrlVisitsFactory.create_batch(
            random.randint(1, 10),
            url=url,
            created=datetime(2023, 3, 1)
        )

        response = client.get(f'/api/url/{url.short_url}/stats/monthly')
        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert data['url'] == url.url

        expected_stats = {
            '3': len(visits_march),
            '4': len(visits_april),
        }
        assert data['monthly'] == expected_stats
