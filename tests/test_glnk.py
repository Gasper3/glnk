from fastapi import Response, status

from app.models import Url
from . import factories
from httpx import Response


class TestCreateUrl:
    def test_create(self, client):
        payload = {'url': 'https://onet.pl'}
        response = client.post('/api/url', json=payload)
        assert response.status_code == status.HTTP_201_CREATED, response.content

    def test_get(self, client, db_session):
        url: Url = factories.UrlFactory()
        response: Response = client.get(f'/api/url/{url.short_url}')
        assert response.status_code == status.HTTP_200_OK

        data = response.json()
        assert data['url'] == url.url

    def test_get__not_exists(self, client, db_session):
        response: Response = client.get(f'/api/url/INVALID')
        assert response.status_code == status.HTTP_404_NOT_FOUND

        data = response.json()
        assert data['detail'] == 'Url not found'
