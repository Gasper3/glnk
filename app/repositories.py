from sa_repository import BaseRepository

from app.types import RequestData

from .models import UrlVisits, Url


class UrlRepository(BaseRepository[Url]):
    MODEL_CLASS = Url

    def get_or_create_with_request_data(
        self, short_url: str, request_data: RequestData, **params
    ) -> tuple[Url, bool]:
        url, created = super().get_or_create(**params)
        if created:
            url.short_url = short_url
            url.add_request_data(request_data)
            self.session.flush()
        return url, created


class UrlVisitsRepository(BaseRepository[UrlVisits]):
    MODEL_CLASS = UrlVisits
