from fastapi import Request, status
from fastapi.routing import APIRouter
from starlette import responses

from .. import schemas
from ..db import db_session
from ..dependencies import UrlDep
from ..repositories import UrlRepository
from ..utils import common_responses, generate_short_url, url_dep_responses

api_router = APIRouter(prefix='/api/url')


@api_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShortUrlResponse,
    responses={**common_responses},
)
async def create_short_url(body: schemas.UrlRequest, request: Request):
    with db_session() as session:
        repository = UrlRepository(session)
        request_data = {
            'user_agent': request.headers.get('user-agent'),
            'ip_address': request.client.host,
        }

        url_obj, _ = repository.get_or_create_with_request_data(
            url=body.url,
            redirect=body.redirect,
            short_url=generate_short_url(),
            request_data=request_data,
        )
        session.expunge(url_obj)

    return {'short_url': url_obj.short_url}


@api_router.get(
    '/{short_url}', responses={**url_dep_responses}, response_model=schemas.UrlResponse
)
async def get_url(request: Request, url_obj: UrlDep):
    if url_obj.redirect:
        return responses.RedirectResponse(url=url_obj.url)

    return {'url': url_obj.url}
