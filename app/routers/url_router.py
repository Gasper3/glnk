from fastapi import Request, status
from fastapi.routing import APIRouter

from ..db import db_session
from ..dependencies import UrlDep
from ..repositories import UrlRepository, UrlVisitsRepository
from ..schemas import UrlRequest
from ..utils import generate_short_url

api_router = APIRouter(prefix='/api/url')


@api_router.post('', status_code=status.HTTP_201_CREATED)
async def create_short_url(body: UrlRequest, request: Request):
    with db_session() as session:
        repository = UrlRepository(session)
        url_obj, created = repository.get_or_create(url=body.url)
        if created:
            url_obj.short_url = generate_short_url()
            url_obj.user_agent = request.headers.get('user-agent')
            url_obj.ip_address = request.client.host
            session.flush()
        session.expunge(url_obj)

    return {
        'short_url': url_obj.short_url,
    }


@api_router.get('/{short_url}')
async def get_url(request: Request, url_obj: UrlDep):
    with db_session() as session:
        UrlVisitsRepository(session).create(
            url=url_obj,
            user_agent=request.headers.get('user-agent'),
            ip_address=request.client.host
        )
        session.expunge(url_obj)

    return {
        'url': url_obj.url
    }
