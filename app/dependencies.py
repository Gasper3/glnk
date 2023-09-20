import typing as t

from fastapi import HTTPException, Request, status, Depends

from .db import db_session
from .models import Url
from .repositories import UrlRepository, UrlVisitsRepository

__all__ = ['UrlDep']


async def get_url_from_short_url(short_url: str, request: Request):
    with db_session() as session:
        repository = UrlRepository(session)
        url_obj = repository.get_or_none(Url.short_url == short_url)
        if not url_obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail='Url not found'
            )

        UrlVisitsRepository(session).create(
            url=url_obj,
            user_agent=request.headers.get('user-agent'),
            ip_address=request.client.host,
        )
        session.expunge(url_obj)
        return url_obj


UrlDep = t.Annotated[Url, Depends(get_url_from_short_url)]
