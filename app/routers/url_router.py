import uuid

from fastapi.routing import APIRouter

from config import settings
from ..db import db_session
from ..repositories import UrlRepository
from ..schemas import UrlRequest

api_router = APIRouter(prefix='/api/url')


@api_router.post('')
async def create_short_url(body: UrlRequest):
    with db_session() as session:
        repository = UrlRepository(session)
        url_obj, created = repository.get_or_create(url=body.url)
        if created:
            url_obj.short_url = uuid.uuid4().hex[:settings.short_url_size].upper()
            session.flush()
        session.expunge(url_obj)

    return {
        'short_url': url_obj.short_url,
    }
